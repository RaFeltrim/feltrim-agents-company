from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import structlog
import uvicorn
from contextlib import asynccontextmanager

from config import settings
from models import (
    HealthResponse, OrchestratorStatus, CNPJValidationRequest,
    CNPJValidationResponse, TestExecutionRequest, TestExecutionResponse
)
from orchestrator import orchestrator
from proxy import service_proxy
from datetime import datetime
import httpx
import asyncio
from fastapi import WebSocket, WebSocketDisconnect

# Configuração de logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Platform-One Orchestrator starting up")
    yield
    # Shutdown
    logger.info("Platform-One Orchestrator shutting down")
    await service_proxy.close()

app = FastAPI(
    title="Platform-One Orchestrator",
    description="Orquestrador principal para integração CNPJ-QA-Training e Fabrica-de-Testes",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Verificação de saúde do orquestrador"""
    try:
        status = await orchestrator.get_orchestrator_status()

        # Determinar status geral
        all_healthy = all(
            service.status in ["healthy", "running"]
            for service in [
                status.platform_one, status.postgres, status.redis,
                status.cnpj_qa_training, status.fabrica_backend, status.fabrica_frontend
            ]
        )

        return HealthResponse(
            status="healthy" if all_healthy else "degraded",
            timestamp=datetime.utcnow(),
            version="1.0.0",
            services={
                "platform_one": status.platform_one.status,
                "postgres": status.postgres.status,
                "redis": status.redis.status,
                "cnpj_qa_training": status.cnpj_qa_training.status,
                "fabrica_backend": status.fabrica_backend.status,
                "fabrica_frontend": status.fabrica_frontend.status,
            }
        )
    except Exception as e:
        logger.error("Health check failed", error=str(e))
        raise HTTPException(status_code=500, detail="Health check failed")

@app.get("/status", response_model=OrchestratorStatus)
async def get_orchestrator_status():
    """Obtém status detalhado de todos os serviços"""
    try:
        return await orchestrator.get_orchestrator_status()
    except Exception as e:
        logger.error("Status check failed", error=str(e))
        raise HTTPException(status_code=500, detail="Failed to get orchestrator status")

@app.post("/cnpj/validate", response_model=CNPJValidationResponse)
async def validate_cnpj(request: CNPJValidationRequest, background_tasks: BackgroundTasks):
    """Workflow completo de validação CNPJ"""
    try:
        result = await orchestrator.validate_cnpj_workflow(
            request.cnpj,
            request.validate_receita
        )

        return CNPJValidationResponse(
            cnpj=result["cnpj"],
            is_valid=result["validation"]["is_valid"],
            formatted_cnpj=result["validation"].get("formatted_cnpj"),
            receita_data=result["validation"].get("receita_data"),
            error_message=result["validation"].get("error_message")
        )
    except Exception as e:
        logger.error("CNPJ validation failed", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tests/execute", response_model=TestExecutionResponse)
async def execute_test(request: TestExecutionRequest, background_tasks: BackgroundTasks):
    """Executa workflow de testes"""
    try:
        result = await orchestrator.execute_test_workflow(
            request.test_type,
            request.parameters or {}
        )

        return TestExecutionResponse(
            execution_id=result.get("execution_id", ""),
            status=result.get("status", "unknown"),
            results=result.get("results"),
            error_message=result.get("error_message")
        )
    except Exception as e:
        logger.error("Test execution failed", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/webhooks/register")
async def register_webhook(event_type: str, webhook_url: str):
    """Registra um webhook para notificações de eventos"""
    try:
        await orchestrator.register_webhook_listener(event_type, webhook_url)
        return {"message": f"Webhook registered for event: {event_type}"}
    except Exception as e:
        logger.error("Webhook registration failed", error=str(e))
        raise HTTPException(status_code=500, detail="Failed to register webhook")

@app.get("/services/{service_name}/health")
async def get_service_health(service_name: str):
    """Obtém saúde de um serviço específico"""
    try:
        if service_name == "platform-one":
            return {
                "name": "platform-one",
                "status": "healthy",
                "timestamp": datetime.utcnow().isoformat()
            }

        service_info = await service_proxy.check_service_health(service_name)
        return service_info.dict()
    except Exception as e:
        logger.error("Service health check failed", service=service_name, error=str(e))
        raise HTTPException(status_code=500, detail=f"Failed to check {service_name} health")

# --- AI Agents Proxy Routes ---

AI_SERVICE_URL = "http://ai-agent-service:3002"
AI_WS_URL = "ws://ai-agent-service:3002"

@app.post("/ai/generate")
async def ai_generate(request: dict):
    """Proxy HTTP para o serviço de agentes de IA"""
    try:
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(f"{AI_SERVICE_URL}/generate", json=request)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error("AI Agent generation failed", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/ai/ws")
async def ai_websocket_proxy(websocket: WebSocket):
    """Proxy WebSocket para receber os logs/pensamentos da IA em tempo real"""
    import websockets
    
    await websocket.accept()
    
    try:
        async with websockets.connect(f"{AI_WS_URL}/ws") as target_ws:
            # Tarefa para ler do cliente e mandar pro target (opcional, só pings)
            async def client_to_target():
                try:
                    while True:
                        data = await websocket.receive_text()
                        await target_ws.send(data)
                except:
                    pass
                    
            # Tarefa para ler do target e mandar pro cliente
            async def target_to_client():
                try:
                    while True:
                        data = await target_ws.recv()
                        await websocket.send_text(data)
                except:
                    pass
            
            await asyncio.gather(
                client_to_target(),
                target_to_client()
            )
    except Exception as e:
        logger.error("AI WebSocket proxy failed", error=str(e))
    finally:
        try:
            await websocket.close()
        except:
            pass

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info"
    )