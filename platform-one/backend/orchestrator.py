import asyncio
from typing import Dict, Any, List
import structlog
from datetime import datetime
from config import settings
from models import ServiceStatus, OrchestratorStatus, WebhookEvent
from proxy import service_proxy

logger = structlog.get_logger()

class PlatformOrchestrator:
    def __init__(self):
        self.webhook_listeners: Dict[str, List[str]] = {}
        self.service_status_cache: Dict[str, Any] = {}
        self.last_status_check = None

    async def get_orchestrator_status(self) -> OrchestratorStatus:
        """Obtém status completo do orquestrador"""
        # Status dos serviços externos
        external_services = await service_proxy.check_all_services()

        # Status do Platform-One (este serviço)
        platform_status = {
            "name": "platform_one",
            "url": f"http://localhost:{settings.port}",
            "status": ServiceStatus.RUNNING,
            "last_check": datetime.utcnow(),
            "response_time": 0.0
        }

        # Status do PostgreSQL e Redis (simulado por enquanto)
        postgres_status = {
            "name": "postgres",
            "url": settings.database_url,
            "status": ServiceStatus.HEALTHY,  # Em produção, verificar conexão real
            "last_check": datetime.utcnow(),
            "response_time": 0.1
        }

        redis_status = {
            "name": "redis",
            "url": settings.redis_url,
            "status": ServiceStatus.HEALTHY,  # Em produção, verificar conexão real
            "last_check": datetime.utcnow(),
            "response_time": 0.05
        }

        return OrchestratorStatus(
            platform_one=platform_status,
            postgres=postgres_status,
            redis=redis_status,
            cnpj_qa_training=external_services.get("cnpj_qa_training"),
            fabrica_backend=external_services.get("fabrica_backend"),
            fabrica_frontend=external_services.get("fabrica_frontend")
        )

    async def validate_cnpj_workflow(self, cnpj: str, validate_receita: bool = False) -> Dict[str, Any]:
        """Workflow completo de validação CNPJ"""
        logger.info("Starting CNPJ validation workflow", cnpj=cnpj)

        try:
            # Passo 1: Validar CNPJ via CNPJ-QA-Training
            validation_result = await service_proxy.call_cnpj_validation(cnpj, validate_receita)

            # Passo 2: Se válido, executar testes relacionados
            if validation_result.get("is_valid"):
                test_params = {
                    "cnpj": cnpj,
                    "validation_type": "receita" if validate_receita else "basic"
                }

                # Executar testes no Fabrica-de-Testes
                test_result = await service_proxy.call_test_execution("cnpj_validation", test_params)

                # Aguardar resultados (simplificado)
                await asyncio.sleep(2)  # Em produção, polling ou webhook
                test_details = await service_proxy.get_test_results(test_result["execution_id"])

                result = {
                    "cnpj": cnpj,
                    "validation": validation_result,
                    "tests": test_details,
                    "workflow_status": "completed"
                }
            else:
                result = {
                    "cnpj": cnpj,
                    "validation": validation_result,
                    "tests": None,
                    "workflow_status": "validation_failed"
                }

            # Passo 3: Notificar via webhook se configurado
            await self._notify_webhook_listeners("cnpj_validation_completed", result)

            return result

        except Exception as e:
            logger.error("CNPJ validation workflow failed", error=str(e))
            await self._notify_webhook_listeners("cnpj_validation_failed", {"cnpj": cnpj, "error": str(e)})
            raise

    async def execute_test_workflow(self, test_type: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Workflow de execução de testes"""
        logger.info("Starting test execution workflow", test_type=test_type)

        try:
            # Executar teste via Fabrica-de-Testes
            execution_result = await service_proxy.call_test_execution(test_type, parameters)

            # Aguardar conclusão e obter resultados
            await asyncio.sleep(5)  # Em produção, implementar polling inteligente
            final_result = await service_proxy.get_test_results(execution_result["execution_id"])

            # Notificar conclusão
            await self._notify_webhook_listeners("test_execution_completed", final_result)

            return final_result

        except Exception as e:
            logger.error("Test execution workflow failed", error=str(e))
            await self._notify_webhook_listeners("test_execution_failed", {"test_type": test_type, "error": str(e)})
            raise

    async def register_webhook_listener(self, event_type: str, webhook_url: str):
        """Registra um listener de webhook para um tipo de evento"""
        if event_type not in self.webhook_listeners:
            self.webhook_listeners[event_type] = []
        self.webhook_listeners[event_type].append(webhook_url)
        logger.info("Webhook listener registered", event_type=event_type, url=webhook_url)

    async def _notify_webhook_listeners(self, event_type: str, data: Dict[str, Any]):
        """Notifica listeners de webhook sobre um evento"""
        if event_type not in self.webhook_listeners:
            return

        webhook_event = WebhookEvent(
            event_type=event_type,
            service="platform-one",
            data=data,
            timestamp=datetime.utcnow()
        )

        # Em produção, implementar notificações assíncronas
        for webhook_url in self.webhook_listeners[event_type]:
            try:
                # Simular notificação (em produção, usar httpx para POST)
                logger.info("Webhook notification", event_type=event_type, url=webhook_url, data=data)
            except Exception as e:
                logger.error("Webhook notification failed", url=webhook_url, error=str(e))

# Instância global
orchestrator = PlatformOrchestrator()