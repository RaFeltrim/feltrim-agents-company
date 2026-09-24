import httpx
import asyncio
from typing import Dict, Any, Optional
import structlog
from config import settings
from models import ServiceStatus, ServiceInfo
from datetime import datetime

logger = structlog.get_logger()

class ServiceProxy:
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=30.0)
        self.services = {
            "cnpj_qa_training": settings.cnpj_qa_url,
            "fabrica_backend": settings.fabrica_backend_url,
            "fabrica_frontend": settings.fabrica_frontend_url,
        }

    async def check_service_health(self, service_name: str) -> ServiceInfo:
        """Verifica a saúde de um serviço específico"""
        url = self.services.get(service_name)
        if not url:
            return ServiceInfo(
                name=service_name,
                url="",
                status=ServiceStatus.ERROR,
                error_message="Service URL not configured"
            )

        try:
            start_time = asyncio.get_event_loop().time()
            response = await self.client.get(f"{url}/health")
            response_time = asyncio.get_event_loop().time() - start_time

            if response.status_code == 200:
                status = ServiceStatus.HEALTHY
                error_message = None
            else:
                status = ServiceStatus.UNHEALTHY
                error_message = f"HTTP {response.status_code}"

        except Exception as e:
            status = ServiceStatus.ERROR
            error_message = str(e)
            response_time = None

        return ServiceInfo(
            name=service_name,
            url=url,
            status=status,
            last_check=datetime.utcnow(),
            response_time=response_time,
            error_message=error_message
        )

    async def check_all_services(self) -> Dict[str, ServiceInfo]:
        """Verifica a saúde de todos os serviços"""
        tasks = []
        for service_name in self.services.keys():
            tasks.append(self.check_service_health(service_name))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        service_status = {}
        for i, service_name in enumerate(self.services.keys()):
            if isinstance(results[i], Exception):
                service_status[service_name] = ServiceInfo(
                    name=service_name,
                    url=self.services[service_name],
                    status=ServiceStatus.ERROR,
                    error_message=str(results[i])
                )
            else:
                service_status[service_name] = results[i]

        return service_status

    async def call_cnpj_validation(self, cnpj: str, validate_receita: bool = False) -> Dict[str, Any]:
        """Chama a validação CNPJ no serviço CNPJ-QA-Training"""
        url = f"{settings.cnpj_qa_url}/validate"
        payload = {"cnpj": cnpj, "validate_receita": validate_receita}

        try:
            response = await self.client.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error("CNPJ validation failed", error=str(e))
            raise

    async def call_test_execution(self, test_type: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Executa testes através do Fabrica-de-Testes"""
        url = f"{settings.fabrica_backend_url}/tests/execute"
        payload = {"test_type": test_type, "parameters": parameters}

        try:
            response = await self.client.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error("Test execution failed", error=str(e))
            raise

    async def get_test_results(self, execution_id: str) -> Dict[str, Any]:
        """Obtém resultados de testes"""
        url = f"{settings.fabrica_backend_url}/tests/results/{execution_id}"

        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error("Get test results failed", error=str(e))
            raise

    async def close(self):
        """Fecha o cliente HTTP"""
        await self.client.aclose()

# Instância global
service_proxy = ServiceProxy()