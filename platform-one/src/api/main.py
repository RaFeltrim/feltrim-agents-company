
from typing import Optional, List
from pydantic import BaseModel
from fastapi import HTTPException, Query

from fastapi import FastAPI
from src.cnpj_validator.cnpj_validator import CNPJValidator

# Instância global do validador
validator = CNPJValidator()

app = FastAPI(
	title="API de Validação de CNPJ",
	description="""
## API para Validação e Consulta de CNPJ

### Funcionalidades

| Recurso | Descrição |
|---------|-----------|
| **Validação** | Verifica dígitos verificadores e formato |
| **Formatação** | Converte CNPJ para formato padrão |
| **Consulta** | Busca dados na Receita Federal |
| **Novo Formato** | Suporte ao CNPJ alfanumérico (2026+) |

### Tipos de Validação

1. **Básica** - Valida dígitos verificadores
2. **Numérica** - Detalhes do cálculo dos DVs
3. **Formato** - Verifica pontuação e separadores
4. **Novo Formato** - CNPJs com letras (A-Z) na raiz

### CNPJs para Teste

| CNPJ | Válido | Observação |
|------|--------|------------|
| `11222333000181` | Sim | CNPJ válido (matriz) |
| `11222333000262` | Sim | CNPJ válido (filial) |
| `11111111111111` | Não | Dígitos repetidos |
| `12345678901234` | Não | DVs incorretos |

---
*Projeto de treinamento em QA*
	""",
	version="2.1.0",
	contact={
		"name": "Rafael Feltrim",
		"url": "https://github.com/RaFeltrim/CNPJ-QA-Training",
	},
	license_info={
		"name": "MIT",
		"url": "https://opensource.org/licenses/MIT",
	},
	openapi_tags=[
		{
			"name": "Status",
			"description": "Verificação de saúde da API",
		},
		{
			"name": "Validação Básica",
			"description": "Validação simples de CNPJ",
		},
		{
			"name": "Validação Detalhada",
			"description": "Validação com detalhes (numérica e formato)",
		},
		{
			"name": "Novo Formato (2026+)",
			"description": "CNPJ alfanumérico com letras na raiz",
		},
		{
			"name": "Consulta Receita Federal",
			"description": "Busca dados cadastrais",
		},
		{
			"name": "Utilitários",
			"description": "Formatação e ferramentas auxiliares",
		},
	]
)

class NewFormatValidationResponse(BaseModel):
	valid: bool
	is_alphanumeric: bool
	is_matriz: Optional[bool] = None
	cnpj_formatted: str
	cnpj_clean: str
	root_valid: bool
	order_valid: bool
	dv_valid: bool
	parts: Optional[dict] = None
	errors: Optional[list] = []

class GenerateCNPJResponse(BaseModel):
	cnpj_formatted: str
	cnpj_clean: str
	raiz: str
	is_alphanumeric: bool

class BasicValidationResponse(BaseModel):
	valid: bool
	cnpj_clean: str
	cnpj_formatted: str
	is_matriz: bool
	errors: List[str] = []

class DetailedValidationResponse(BaseModel):
	valid: bool
	cnpj_clean: str
	cnpj_formatted: str
	is_matriz: bool
	root_valid: bool
	order_valid: bool
	dv_valid: bool
	parts: Optional[dict] = None
	errors: List[str] = []

@app.get(
	"/api/v1/validate/alphanumeric",
	tags=["Validação Detalhada"],
	summary="Validação Alfanumérica (2026+)",
	response_model=NewFormatValidationResponse
)
async def validate_alphanumeric(
	cnpj: str = Query(..., description="CNPJ alfanumérico ou numérico", examples=["AB.CDE.123/0001-45"])
):
	result = NewAlphanumericCNPJValidator.validate(cnpj)
	cnpj_clean = NewAlphanumericCNPJValidator.remove_formatting(cnpj)

	root_valid = False
	order_valid = False
	dv_valid = False

	if len(cnpj_clean) >= 8:
		root_result = NewAlphanumericCNPJValidator.validate_root_chars(cnpj_clean)
		root_valid = root_result.get('valid', False)

	if len(cnpj_clean) >= 12:
		order_result = NewAlphanumericCNPJValidator.validate_order_digits(cnpj_clean)
		order_valid = order_result.get('valid', False)

	if root_valid and order_valid and len(cnpj_clean) == 14:
		dv_result = NewAlphanumericCNPJValidator.validate_check_digits(cnpj_clean)
		dv_valid = dv_result.get('valid', False)

	return NewFormatValidationResponse(
		valid=result.get('valid', False),
		is_alphanumeric=result.get('is_alphanumeric', False),
		is_matriz=result.get('is_matriz'),
		cnpj_formatted=result.get('cnpj_formatted', ''),
		cnpj_clean=result.get('cnpj_clean', ''),
		root_valid=root_valid,
		order_valid=order_valid,
		dv_valid=dv_valid,
		parts=result.get('parts'),
		errors=result.get('errors', [])
	)

@app.get(
	"/api/v1/generate/alphanumeric",
	tags=["Utilitários"],
	summary="Gerar CNPJ Alfanumérico",
	response_model=GenerateCNPJResponse
)
async def generate_alphanumeric_cnpj(
	raiz: Optional[str] = Query(
		None,
		description="Raiz personalizada (até 8 caracteres A-Z/0-9)",
		examples=["TESTECNP"],
		max_length=8
	),
	only_letters: bool = Query(
		False,
		description="Gerar raiz apenas com letras (A-Z)"
	),
	only_numbers: bool = Query(
		False,
		description="Gerar raiz apenas com números (formato tradicional)"
	),
	filial: bool = Query(
		False,
		description="Gerar como filial (ordem > 0001)"
	),
):
	import random

	if only_letters and only_numbers:
		raise HTTPException(
			status_code=400,
			detail="Não é possível usar only_letters e only_numbers simultaneamente"
		)

	if raiz:
		raiz_clean = raiz.upper().replace('.', '').replace('-', '').replace('/', '')
		if len(raiz_clean) > 8:
			raise HTTPException(status_code=400, detail="Raiz deve ter no máximo 8 caracteres")
		invalid = [c for c in raiz_clean if c not in NewAlphanumericCNPJValidator.VALID_ROOT_CHARS]
		if invalid:
			raise HTTPException(status_code=400, detail=f"Caracteres inválidos: {invalid}")
	elif only_letters:
		raiz_clean = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))
	elif only_numbers:
		raiz_clean = ''.join(random.choices('0123456789', k=8))
	else:
		chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		raiz_clean = (
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') +
			random.choice('0123456789') +
			''.join(random.choices(chars, k=6))
		)
		raiz_clean = ''.join(random.sample(raiz_clean, len(raiz_clean)))

	if filial:
		ordem = f"{random.randint(2, 9999):04d}"
	else:
		ordem = "0001"

	base = raiz_clean.ljust(8, '0')[:8] + ordem
	dv1 = NewAlphanumericCNPJValidator.calculate_first_digit(base)
	dv2 = NewAlphanumericCNPJValidator.calculate_second_digit(base + str(dv1))

	cnpj_clean = base + str(dv1) + str(dv2)
	cnpj_formatted = NewAlphanumericCNPJValidator.format_cnpj(cnpj_clean)
	validation = NewAlphanumericCNPJValidator.validate(cnpj_clean)

	return GenerateCNPJResponse(
		cnpj_formatted=cnpj_formatted,
		cnpj_clean=cnpj_clean,
		raiz=cnpj_clean[:8],
		is_alphanumeric=validation.get('is_alphanumeric', False)
	)
"""
API REST para Validação de CNPJ com Swagger/OpenAPI

Execute com: uvicorn src.api.main:app --reload
Acesse o Swagger em: http://localhost:8000/docs
"""

import sys
import os

# Adiciona o diretório src ao path para importações
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from cnpj_validator.validators.new_alphanumeric_validator import NewAlphanumericCNPJValidator
from cnpj_validator.validators.numeric_validator import NumericCNPJValidator
from cnpj_validator.validators.alphanumeric_validator import AlphanumericCNPJValidator
from cnpj_validator import CNPJValidator, ReceitaFederalAPI, ReceitaFederalAPIError
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from enum import Enum

# ... (demais modelos, configurações e endpoints migrados do main.py legado)

# =============================
# CONFIGURAÇÃO DA API
# =============================

API_VERSION = "2.1.0"

app = FastAPI(
	title="API de Validação de CNPJ",
	description="""
## API para Validação e Consulta de CNPJ

### Funcionalidades

| Recurso | Descrição |
|---------|-----------|
| **Validação** | Verifica dígitos verificadores e formato |
| **Formatação** | Converte CNPJ para formato padrão |
| **Consulta** | Busca dados na Receita Federal |
| **Novo Formato** | Suporte ao CNPJ alfanumérico (2026+) |

### Tipos de Validação

1. **Básica** - Valida dígitos verificadores
2. **Numérica** - Detalhes do cálculo dos DVs
3. **Formato** - Verifica pontuação e separadores
4. **Novo Formato** - CNPJs com letras (A-Z) na raiz

### CNPJs para Teste

| CNPJ | Válido | Observação |
|------|--------|------------|
| `11222333000181` | Sim | CNPJ válido (matriz) |
| `11222333000262` | Sim | CNPJ válido (filial) |
| `11111111111111` | Não | Dígitos repetidos |
| `12345678901234` | Não | DVs incorretos |

---
*Projeto de treinamento em QA*
	""",
	version=API_VERSION,
	contact={
		"name": "Rafael Feltrim",
		"url": "https://github.com/RaFeltrim/CNPJ-QA-Training",
	},
	license_info={
		"name": "MIT",
		"url": "https://opensource.org/licenses/MIT",
	},
	openapi_tags=[
		{
			"name": "Status",
			"description": "Verificação de saúde da API",
		},
		{
			"name": "Validação Básica",
			"description": "Validação simples de CNPJ",
		},
		{
			"name": "Validação Detalhada",
			"description": "Validação com detalhes (numérica e formato)",
		},
		{
			"name": "Novo Formato (2026+)",
			"description": "CNPJ alfanumérico com letras na raiz",
		},
		{
			"name": "Consulta Receita Federal",
			"description": "Busca dados cadastrais",
		},
		{
			"name": "Utilitários",
			"description": "Formatação e ferramentas auxiliares",
		},
	]
)

# Endpoint raiz para status
@app.get("/", tags=["Status"])
async def root():
	return {"status": "ok", "message": "API de Validação de CNPJ está rodando!"}

@app.get("/status", tags=["Status"])
async def status():
	return {"status": "ok", "message": "API de Validação de CNPJ está rodando!"}

@app.get("/validate/basic/{cnpj}", tags=["Validação"], summary="Validação Básica", response_model=BasicValidationResponse)
async def validate_basic(cnpj: str):
	result = validator.validate(cnpj, validate_format=False)
	return BasicValidationResponse(
		valid=result.get('valid', False),
		cnpj_clean=result.get('cnpj_clean', ''),
		cnpj_formatted=result.get('cnpj_formatted', ''),
		is_matriz=result.get('numeric_validation', {}).get('is_matriz', False),
		errors=result.get('errors', [])
	)

@app.get("/validate/detailed/{cnpj}", tags=["Validação"], summary="Validação Detalhada", response_model=DetailedValidationResponse)
async def validate_detailed(cnpj: str):
	result = validator.validate(cnpj, validate_format=True)
	return DetailedValidationResponse(
		valid=result.get('valid', False),
		cnpj_clean=result.get('cnpj_clean', ''),
		cnpj_formatted=result.get('cnpj_formatted', ''),
		is_matriz=result.get('numeric_validation', {}).get('is_matriz', False),
		root_valid=result.get('alphanumeric_validation', {}).get('root_valid', False),
		order_valid=result.get('alphanumeric_validation', {}).get('order_valid', False),
		dv_valid=result.get('alphanumeric_validation', {}).get('dv_valid', False),
		parts=result.get('alphanumeric_validation', {}).get('parts'),
		errors=result.get('errors', [])
	)


# =============================================================================
# EXECUÇÃO
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)  # Porta diferente da API do CNPJ-QA-Training
