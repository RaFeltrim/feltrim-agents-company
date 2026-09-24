"""
Testes Unitários para AlphanumericCNPJValidator
Seguindo princípios de Shift Left Testing
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cnpj_validator.validators.alphanumeric_validator import AlphanumericCNPJValidator


class TestAlphanumericValidatorFormat:
	"""Testes de validação de formato"""
    
	def test_validate_format_correct(self):
		"""Deve validar formato correto XX.XXX.XXX/XXXX-XX"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate_format(cnpj)
		assert result['valid'] is True
		assert result['errors'] == []
    
	def test_validate_format_without_formatting(self):
		"""Deve rejeitar CNPJ sem formatação"""
		cnpj = "11222333000181"
		result = AlphanumericCNPJValidator.validate_format(cnpj)
		assert result['valid'] is False
		assert "sem formatação" in result['errors'][0]
    
	def test_validate_format_wrong_separators(self):
		"""Deve rejeitar CNPJ com separadores incorretos"""
		cnpj = "11-222-333-0001-81"
		result = AlphanumericCNPJValidator.validate_format(cnpj)
		assert result['valid'] is False
		assert "Formato inválido" in result['errors'][0]
    
	def test_validate_format_missing_dots(self):
		"""Deve rejeitar CNPJ sem pontos"""
		cnpj = "11222333/0001-81"
		result = AlphanumericCNPJValidator.validate_format(cnpj)
		assert result['valid'] is False
    
	def test_validate_format_missing_slash(self):
		"""Deve rejeitar CNPJ sem barra"""
		cnpj = "11.222.333.0001-81"
		result = AlphanumericCNPJValidator.validate_format(cnpj)
		assert result['valid'] is False
    
	def test_validate_format_missing_dash(self):
		"""Deve rejeitar CNPJ sem traço"""
		cnpj = "11.222.333/000181"
		result = AlphanumericCNPJValidator.validate_format(cnpj)
		assert result['valid'] is False
    
	def test_validate_format_non_string(self):
		"""Deve rejeitar entrada não string"""
		result = AlphanumericCNPJValidator.validate_format(123)
		assert result['valid'] is False
		assert "string" in result['errors'][0]


class TestAlphanumericValidatorSpecialCharacters:
	"""Testes de validação de caracteres especiais"""
    
	def test_validate_special_characters_valid(self):
		"""Deve aceitar apenas números e separadores válidos"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate_special_characters(cnpj)
		assert result['valid'] is True
    
	def test_validate_special_characters_with_letters(self):
		"""Deve rejeitar CNPJ com letras"""
		cnpj = "11.222.333/0001-8A"
		result = AlphanumericCNPJValidator.validate_special_characters(cnpj)
		assert result['valid'] is False
		assert "A" in result['errors'][0]
    
	def test_validate_special_characters_with_symbols(self):
		"""Deve rejeitar CNPJ com símbolos inválidos"""
		cnpj = "11.222.333/0001-81@"
		result = AlphanumericCNPJValidator.validate_special_characters(cnpj)
		assert result['valid'] is False
		assert "@" in result['errors'][0]
    
	def test_validate_special_characters_with_spaces(self):
		"""Deve rejeitar CNPJ com espaços"""
		cnpj = "11.222.333/0001 81"
		result = AlphanumericCNPJValidator.validate_special_characters(cnpj)
		assert result['valid'] is False
		assert " " in result['errors'][0]
    
	def test_validate_special_characters_non_string(self):
		"""Deve rejeitar entrada não string"""
		result = AlphanumericCNPJValidator.validate_special_characters(None)
		assert result['valid'] is False


class TestAlphanumericValidatorSeparatorPositions:
	"""Testes de validação de posições dos separadores"""
    
	def test_validate_separator_positions_correct(self):
		"""Deve validar separadores nas posições corretas"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate_separator_positions(cnpj)
		assert result['valid'] is True
    
	def test_validate_separator_positions_wrong_first_dot(self):
		"""Deve rejeitar primeira ponto na posição errada"""
		cnpj = "112.22.333/0001-81"
		result = AlphanumericCNPJValidator.validate_separator_positions(cnpj)
		assert result['valid'] is False
    
	def test_validate_separator_positions_wrong_second_dot(self):
		"""Deve rejeitar segundo ponto na posição errada"""
		cnpj = "11.2222.33/0001-81"
		result = AlphanumericCNPJValidator.validate_separator_positions(cnpj)
		assert result['valid'] is False
	def test_validate_separator_positions_wrong_slash(self):
		"""Deve rejeitar barra na posição errada"""
		cnpj = "11.222.333-0001/81"
		result = AlphanumericCNPJValidator.validate_separator_positions(cnpj)
		assert result['valid'] is False
	def test_validate_separator_positions_wrong_dash(self):
		"""Deve rejeitar traço na posição errada"""
		cnpj = "11.222.333/00-0181"
		result = AlphanumericCNPJValidator.validate_separator_positions(cnpj)
		assert result['valid'] is False
	def test_validate_separator_positions_wrong_length(self):
		"""Deve rejeitar CNPJ com tamanho incorreto"""
		cnpj = "11.222.333/0001-8"
		result = AlphanumericCNPJValidator.validate_separator_positions(cnpj)
		assert result['valid'] is False
		assert "Tamanho incorreto" in result['errors'][0]


class TestAlphanumericValidatorMatrizFilial:
	"""Testes de validação de código matriz/filial"""
    
	def test_validate_matriz_filial_matriz(self):
		"""Deve identificar código de matriz (0001)"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate_matriz_filial(cnpj)
		assert result['valid'] is True
		assert result['info']['type'] == 'matriz'
		assert result['info']['code'] == '0001'
    
	def test_validate_matriz_filial_filial_002(self):
		"""Deve identificar filial 0002"""
		cnpj = "11.222.333/0002-62"
		result = AlphanumericCNPJValidator.validate_matriz_filial(cnpj)
		assert result['valid'] is True
		assert result['info']['type'] == 'filial'
		assert result['info']['code'] == '0002'
		assert result['info']['number'] == 2
    
	def test_validate_matriz_filial_filial_high_number(self):
		"""Deve identificar filial com número alto"""
		cnpj = "11.222.333/0999-99"
		result = AlphanumericCNPJValidator.validate_matriz_filial(cnpj)
		assert result['valid'] is True
		assert result['info']['type'] == 'filial'
		assert result['info']['number'] == 999
    
	def test_validate_matriz_filial_invalid_0000(self):
		"""Deve rejeitar código 0000"""
		cnpj = "11.222.333/0000-00"
		result = AlphanumericCNPJValidator.validate_matriz_filial(cnpj)
		assert result['valid'] is False
		assert "0000" in result['errors'][0]
    
	def test_validate_matriz_filial_invalid_format(self):
		"""Deve rejeitar CNPJ com formato incorreto"""
		cnpj = "11222333000181"
		result = AlphanumericCNPJValidator.validate_matriz_filial(cnpj)
		assert result['valid'] is False


class TestAlphanumericValidatorWhitespace:
	"""Testes de validação de espaços em branco"""
    
	def test_validate_whitespace_no_spaces(self):
		"""Deve validar CNPJ sem espaços"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate_whitespace(cnpj)
		assert result['valid'] is True
		assert result['errors'] == []
    
	def test_validate_whitespace_leading_space(self):
		"""Deve detectar espaço no início"""
		cnpj = " 11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate_whitespace(cnpj)
		assert "início ou fim" in result['warnings'][0]
    
	def test_validate_whitespace_trailing_space(self):
		"""Deve detectar espaço no fim"""
		cnpj = "11.222.333/0001-81 "
		result = AlphanumericCNPJValidator.validate_whitespace(cnpj)
		assert "início ou fim" in result['warnings'][0]
    
	def test_validate_whitespace_internal_space(self):
		"""Deve rejeitar espaço interno"""
		cnpj = "11.222.333 /0001-81"
		result = AlphanumericCNPJValidator.validate_whitespace(cnpj)
		assert result['valid'] is False
		assert "espaços em branco" in result['errors'][0]
    
	def test_validate_whitespace_tab(self):
		"""Deve rejeitar tabulação"""
		cnpj = "11.222.333/0001-81\t"
		result = AlphanumericCNPJValidator.validate_whitespace(cnpj)
		assert result['valid'] is False
		assert "tabulações" in result['errors'][0]
    
	def test_validate_whitespace_newline(self):
		"""Deve rejeitar quebra de linha"""
		cnpj = "11.222.333/0001-81\n"
		result = AlphanumericCNPJValidator.validate_whitespace(cnpj)
		assert result['valid'] is False
		assert "quebras de linha" in result['errors'][0]


class TestAlphanumericValidatorExtractParts:
	"""Testes de extração de partes do CNPJ"""
    
	def test_extract_parts_valid_cnpj(self):
		"""Deve extrair partes de CNPJ válido"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.extract_parts(cnpj)
        
		assert result['valid'] is True
		assert result['raiz'] == "11222333"
		assert result['ordem'] == "0001"
		assert result['dv'] == "81"
		assert result['formatted'] == cnpj
	def test_extract_parts_invalid_format(self):
		"""Deve rejeitar formato inválido"""
		cnpj = "11222333000181"
		result = AlphanumericCNPJValidator.extract_parts(cnpj)
        
		assert result['valid'] is False
		assert 'error' in result


class TestAlphanumericValidatorCompleteValidation:
	"""Testes de validação completa alfanumérica"""
    
	def test_validate_complete_valid_cnpj(self):
		"""Deve validar CNPJ formatado corretamente"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate(cnpj)
        
		assert result['valid'] is True
		assert result['errors'] == []
		assert result['parts'] is not None
		assert result['filial_info']['type'] == 'matriz'
	def test_validate_complete_empty_cnpj(self):
		"""Deve rejeitar CNPJ vazio"""
		cnpj = ""
		result = AlphanumericCNPJValidator.validate(cnpj)
        
		assert result['valid'] is False
		assert "vazio" in result['errors'][0]
	def test_validate_complete_with_spaces(self):
		"""Deve detectar espaços e continuar validação"""
		cnpj = " 11.222.333/0001-81 "
		result = AlphanumericCNPJValidator.validate(cnpj)
        
		assert "início ou fim" in result['warnings'][0]
	def test_validate_complete_wrong_format(self):
		"""Deve rejeitar formato incorreto"""
		cnpj = "11-222-333-0001-81"
		result = AlphanumericCNPJValidator.validate(cnpj)
        
		assert result['valid'] is False
		assert len(result['errors']) > 0
	def test_validate_complete_with_invalid_characters(self):
		"""Deve rejeitar caracteres inválidos"""
		cnpj = "11.222.333/0001-8A"
		result = AlphanumericCNPJValidator.validate(cnpj)
        
		assert result['valid'] is False
		assert any("inválidos" in error for error in result['errors'])
	def test_validate_complete_invalid_matriz_code(self):
		"""Deve rejeitar código matriz/filial inválido"""
		cnpj = "11.222.333/0000-81"
		result = AlphanumericCNPJValidator.validate(cnpj)
        
		assert result['valid'] is False

class TestAlphanumericValidatorEdgeCases:
	"""Testes de casos extremos"""
    
	@pytest.mark.parametrize("cnpj", [
		"00.000.000/0001-91",  # Zeros na raiz
		"99.999.999/9999-99",  # Todos noves
		"12.345.678/0001-95",  # Sequencial
	])
	def test_various_valid_formats(self, cnpj):
		"""Deve validar diferentes formatos válidos"""
		result = AlphanumericCNPJValidator.validate_format(cnpj)
		assert result['valid'] is True
	def test_cnpj_with_unicode(self):
		"""Deve rejeitar caracteres Unicode"""
		cnpj = "11.222.333/0001-81★"
		result = AlphanumericCNPJValidator.validate_special_characters(cnpj)
		assert result['valid'] is False

# Testes para integração com Zephyr
class TestZephyrIntegrationAlphanumeric:
	"""Testes marcados para Zephyr Scale"""
    
	@pytest.mark.zephyr("CNPJ-T010")
	def test_cnpj_formato_correto(self):
		"""
		Zephyr Test Case: CNPJ-T010
		Descrição: Validar formato correto de CNPJ
		Prioridade: Alta
		"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate(cnpj)
		assert result['valid'] is True
    
	@pytest.mark.zephyr("CNPJ-T011")
	def test_cnpj_formato_incorreto(self):
		"""
		Zephyr Test Case: CNPJ-T011
		Descrição: Rejeitar formato incorreto de CNPJ
		Prioridade: Alta
		"""
		cnpj = "11-222-333-0001-81"
		result = AlphanumericCNPJValidator.validate(cnpj)
		assert result['valid'] is False
    
	@pytest.mark.zephyr("CNPJ-T012")
	def test_cnpj_identificar_matriz(self):
		"""
		Zephyr Test Case: CNPJ-T012
		Descrição: Identificar corretamente código de matriz
		Prioridade: Média
		"""
		cnpj = "11.222.333/0001-81"
		result = AlphanumericCNPJValidator.validate_matriz_filial(cnpj)
		assert result['valid'] is True
		assert result['info']['type'] == 'matriz'
    
	@pytest.mark.zephyr("CNPJ-T013")
	def test_cnpj_identificar_filial(self):
		"""
		Zephyr Test Case: CNPJ-T013
		Descrição: Identificar corretamente código de filial
		Prioridade: Média
		"""
		cnpj = "11.222.333/0002-62"
		result = AlphanumericCNPJValidator.validate_matriz_filial(cnpj)
		assert result['valid'] is True
		assert result['info']['type'] == 'filial'


if __name__ == "__main__":
	pytest.main([__file__, "-v", "--tb=short"])
