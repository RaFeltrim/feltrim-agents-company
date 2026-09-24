"""
Testes Unitários para NumericCNPJValidator
Seguindo princípios de Shift Left Testing
"""

import pytest
import sys
import os

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cnpj_validator.validators.numeric_validator import NumericCNPJValidator

# ...existing code...
