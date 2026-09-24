"""
Testes para o cliente da API da Receita Federal
"""

import pytest
from unittest.mock import patch, MagicMock
import json

from cnpj_validator.receita_federal_api import (
	ReceitaFederalAPI,
	CNPJData,
	ReceitaFederalAPIError,
)

# ...existing code...
