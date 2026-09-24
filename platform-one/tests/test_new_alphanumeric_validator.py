"""
Testes para o validador de CNPJ Alfanumérico (Novo Formato)

Testa a validação de CNPJs com letras na raiz, conforme previsto
pela Receita Federal para implementação a partir de 2026.
"""

import pytest
from cnpj_validator.validators.new_alphanumeric_validator import NewAlphanumericCNPJValidator


class TestNewAlphanumericCNPJValidator:
	"""Testes para o validador de CNPJ alfanumérico"""
	# ...existing code...
