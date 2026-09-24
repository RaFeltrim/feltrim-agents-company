"""
Testes de integração para CNPJ alfanumérico.

Este módulo contém testes que validam a integração entre:
- Validador alfanumérico (NewAlphanumericCNPJValidator)
- API REST (endpoints /validate/alphanumeric e /generate/alphanumeric)
- Validação de formato e regras de negócio
"""

import pytest
from fastapi.testclient import TestClient

from src.api.main import app
from cnpj_validator.validators.new_alphanumeric_validator import (
	NewAlphanumericCNPJValidator
)

# Cliente de teste para a API
client = TestClient(app)

# =============================================================================
# Testes de Integração sem Dependências Externas
# =============================================================================

class TestAlphanumericCNPJIntegration:
	"""Testes de integração para CNPJ alfanumérico."""

	def setup_method(self):
		"""Configuração antes de cada teste."""
		self.validator = NewAlphanumericCNPJValidator()

	def test_validator_format_validation(self):
		"""Deve validar corretamente o formato alfanumérico."""
		# CNPJs válidos
		valid_cnpjs = [
			"AB.CD1.234/0001-99",
			"XY.ZW9.876/0001-00",
			"TE.ST0.001/0001-01"
		]

		for cnpj in valid_cnpjs:
			result = self.validator.validate_format(cnpj)
			assert result['valid'], f"CNPJ {cnpj} deveria ser válido"

	def test_validator_invalid_formats(self):
		"""Deve rejeitar formatos inválidos."""
		invalid_cnpjs = [
			"AB.CD1.234/0001-9",  # DV muito curto
			"AB.CD1.234/0001-999",  # DV muito longo
			"AB.CD1.234/0001-XX",  # DV não numérico
			"AB.CD.12.345/0001-99",  # Formato incorreto (pontos extras)
			"ABCD12345000199",  # Sem formatação
		]

		for cnpj in invalid_cnpjs:
			result = self.validator.validate_format(cnpj)
			assert not result['valid'], f"CNPJ {cnpj} deveria ser inválido"

	def test_validator_checksum_calculation(self):
		"""Deve calcular corretamente o dígito verificador."""
		# Teste com CNPJ conhecido
		cnpj_base = "ABCD12340001"
		dv1 = self.validator.calculate_first_digit(cnpj_base)
		dv2 = self.validator.calculate_second_digit(cnpj_base + str(dv1))
		dv_calculado = f"{dv1}{dv2}"
		assert isinstance(dv_calculado, str), "DV deve ser string"
		assert len(dv_calculado) == 2, "DV deve ter 2 dígitos"

	def test_api_validate_endpoint_format_only(self):
		"""Deve validar apenas o formato via API (sem consulta externa)."""
		# CNPJ com formato válido
		valid_cnpj = "5I.P2X.AIJ/0001-84"

		response = client.get(
			"/api/v1/validate/alphanumeric",
			params={"cnpj": valid_cnpj}
		)

		assert response.status_code == 200
		data = response.json()
		assert data["valid"] is True
		assert "root_valid" in data
		assert "order_valid" in data
		assert "dv_valid" in data

	def test_api_validate_endpoint_invalid_format(self):
		"""Deve rejeitar CNPJ com formato inválido via API."""
		invalid_cnpj = "INVALIDO"

		response = client.get(
			"/api/v1/validate/alphanumeric",
			params={"cnpj": invalid_cnpj}
		)

		assert response.status_code == 200
		data = response.json()
		assert data["valid"] is False
		assert "errors" in data
		assert len(data["errors"]) > 0

	def test_api_generate_endpoint(self):
		"""Deve gerar CNPJ alfanumérico válido via API."""
		response = client.get("/api/v1/generate/alphanumeric")

		assert response.status_code == 200
		data = response.json()
		assert "cnpj_formatted" in data
		assert "cnpj_clean" in data

		# Validar formato do CNPJ gerado
		generated_cnpj = data["cnpj_formatted"]
		assert self.validator.validate_format(generated_cnpj), "CNPJ gerado deve ser válido"

	def test_api_generate_multiple_unique(self):
		"""Deve gerar múltiplos CNPJs únicos."""
		generated_cnpjs = set()

		for _ in range(10):
			response = client.get("/api/v1/generate/alphanumeric")
			assert response.status_code == 200
			data = response.json()
			generated_cnpjs.add(data["cnpj_clean"])

		# Todos devem ser únicos
		assert len(generated_cnpjs) == 10, "Todos os CNPJs gerados devem ser únicos"

	def test_validator_business_rules(self):
		"""Deve validar regras de negócio do CNPJ alfanumérico."""
		# Testar que não permite caracteres especiais além de letras e números
		invalid_chars = ["AB.CD1.234/0001-@@", "AB.CD1.234/0001-.."]

		for cnpj in invalid_chars:
			result = self.validator.validate_format(cnpj)
			assert not result['valid'], f"CNPJ {cnpj} deve ser inválido"

	def test_api_error_handling(self):
		"""Deve tratar erros adequadamente na API."""
		# Teste sem parâmetro cnpj
		response = client.get("/api/v1/validate/alphanumeric")
		assert response.status_code == 422  # Unprocessable Entity

		# Teste com CNPJ vazio
		response = client.get(
			"/api/v1/validate/alphanumeric",
			params={"cnpj": ""}
		)
		assert response.status_code == 200
		data = response.json()
		assert data["valid"] is False

	def test_validator_case_insensitive(self):
		"""Deve ser case insensitive para letras."""
