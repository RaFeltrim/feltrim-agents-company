from pydantic import BaseModel
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum

class ServiceStatus(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"
    ERROR = "error"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

class ServiceInfo(BaseModel):
    name: str
    url: str
    status: ServiceStatus
    last_check: Optional[datetime]
    response_time: Optional[float]
    error_message: Optional[str]

class OrchestratorStatus(BaseModel):
    platform_one: ServiceInfo
    postgres: ServiceInfo
    redis: ServiceInfo
    cnpj_qa_training: ServiceInfo
    fabrica_backend: ServiceInfo
    fabrica_frontend: ServiceInfo

class WebhookEvent(BaseModel):
    event_type: str
    service: str
    data: Dict[str, Any]
    timestamp: datetime

class CNPJValidationRequest(BaseModel):
    cnpj: str
    validate_receita: bool = False

class CNPJValidationResponse(BaseModel):
    cnpj: str
    is_valid: bool
    formatted_cnpj: Optional[str]
    receita_data: Optional[Dict[str, Any]]
    error_message: Optional[str]

class TestExecutionRequest(BaseModel):
    test_type: str
    parameters: Optional[Dict[str, Any]] = {}
    webhook_url: Optional[str] = None

class TestExecutionResponse(BaseModel):
    execution_id: str
    status: str
    results: Optional[Dict[str, Any]]
    error_message: Optional[str]

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    services: Dict[str, ServiceStatus]