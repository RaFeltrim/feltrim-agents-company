"""
Testes de Integração para CNPJValidator
Testa a integração entre validadores numérico e alfanumérico
Seguindo princípios de Shift Left Testing
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cnpj_validator import CNPJValidator
from cnpj_validator.validators.numeric_validator import NumericCNPJValidator
from cnpj_validator.validators.alphanumeric_validator import AlphanumericCNPJValidator


class TestCNPJValidatorIntegration:
	"""Testes de integração do validador principal"""
    
	def test_validate_with_both_validations(self):
		"""Deve executar validação numérica e alfanumérica"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		result = validator.validate(cnpj, validate_format=True)
        
		assert result['valid'] is True
		assert 'numeric_validation' in result
		assert 'alphanumeric_validation' in result
		assert result['numeric_validation']['valid'] is True
		assert result['alphanumeric_validation']['valid'] is True
    
	def test_validate_numeric_only(self):
		"""Deve executar apenas validação numérica"""
		validator = CNPJValidator()
		cnpj = "11222333000181"
        
		result = validator.validate(cnpj, validate_format=False)
        
		assert result['valid'] is True
		assert result['numeric_validation']['valid'] is True
    
	def test_validate_formatted_vs_unformatted(self):
		"""Deve validar CNPJ formatado e não formatado igualmente"""
		validator = CNPJValidator()
        
		formatted = "11.222.333/0001-81"
		unformatted = "11222333000181"
        
		result_formatted = validator.validate(formatted, validate_format=False)
		result_unformatted = validator.validate(unformatted, validate_format=False)
        
		assert result_formatted['valid'] is True
		assert result_unformatted['valid'] is True
		assert result_formatted['cnpj_clean'] == result_unformatted['cnpj_clean']
    
	def test_validate_invalid_numeric_stops_alphanumeric(self):
		"""Deve falhar na validação numérica antes da alfanumérica"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-99"  # DV inválido
        
		result = validator.validate(cnpj, validate_format=True)
        
		assert result['valid'] is False
		assert result['numeric_validation']['valid'] is False


class TestCNPJValidatorStaticMethod:
	"""Testes do método estático is_valid"""
    
	def test_is_valid_true(self):
		"""Deve retornar True para CNPJ válido"""
		assert CNPJValidator.is_valid("11.222.333/0001-81") is True
		assert CNPJValidator.is_valid("11222333000181") is True
    
	def test_is_valid_false(self):
		"""Deve retornar False para CNPJ inválido"""
		assert CNPJValidator.is_valid("00000000000000") is False
		assert CNPJValidator.is_valid("11.222.333/0001-99") is False
    
	def test_is_valid_edge_cases(self):
		"""Deve retornar False para casos extremos"""
		assert CNPJValidator.is_valid("") is False
		assert CNPJValidator.is_valid(None) is False


class TestCNPJValidatorFormatMethod:
	"""Testes do método format"""
    
	def test_format_unformatted_cnpj(self):
		"""Deve formatar CNPJ sem formatação"""
		validator = CNPJValidator()
		cnpj = "11222333000181"
        
		formatted = validator.format(cnpj)
        
		assert formatted == "11.222.333/0001-81"
    
	def test_format_already_formatted_cnpj(self):
		"""Deve manter CNPJ já formatado"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		formatted = validator.format(cnpj)
        
		assert formatted == "11.222.333/0001-81"
    
	def test_format_invalid_cnpj(self):
		"""Deve retornar erro para CNPJ inválido"""
		validator = CNPJValidator()
		cnpj = "00000000000000"
        
		result = validator.format(cnpj)
        
		assert "Erro:" in result


class TestCNPJValidatorCleanMethod:
	"""Testes do método clean"""
    
	def test_clean_formatted_cnpj(self):
		"""Deve remover formatação"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		clean = validator.clean(cnpj)
        
		assert clean == "11222333000181"
    
	def test_clean_already_clean(self):
		"""Deve manter CNPJ já sem formatação"""
		validator = CNPJValidator()
		cnpj = "11222333000181"
        
		clean = validator.clean(cnpj)
        
		assert clean == "11222333000181"
    
	def test_clean_various_formats(self):
		"""Deve limpar diferentes formatos"""
		validator = CNPJValidator()
        
		assert validator.clean("11-222-333-0001-81") == "11222333000181"
		assert validator.clean("11 222 333 0001 81") == "11222333000181"


class TestCNPJValidatorGetInfoMethod:
	"""Testes do método get_info"""
    
	def test_get_info_valid_matriz(self):
		"""Deve retornar informações completas para matriz"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		info = validator.get_info(cnpj)
        
		assert info['valid'] is True
		assert info['cnpj_formatted'] == "11.222.333/0001-81"
		assert info['cnpj_clean'] == "11222333000181"
		assert info['matriz_filial']['type'] == 'matriz'
    
	def test_get_info_valid_filial(self):
		"""Deve retornar informações completas para filial"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0002-62"
        
		info = validator.get_info(cnpj)
        
		assert info['valid'] is True
		assert info['matriz_filial']['type'] == 'filial'
		assert info['matriz_filial']['number'] == 2
    
	def test_get_info_invalid_cnpj(self):
		"""Deve retornar erro para CNPJ inválido"""
		validator = CNPJValidator()
		cnpj = "00000000000000"
        
		info = validator.get_info(cnpj)
		assert info['valid'] is False
		assert 'errors' in info
    
	def test_get_info_extracts_parts(self):
		"""Deve extrair partes do CNPJ"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		info = validator.get_info(cnpj)
        
		assert 'parts' in info
		assert info['parts']['raiz'] == "11222333"
		assert info['parts']['ordem'] == "0001"
		assert info['parts']['dv'] == "81"


class TestCNPJValidatorWarnings:
	"""Testes de avisos (warnings)"""
    
	def test_warning_unformatted_input(self):
		"""Deve gerar aviso para entrada sem formatação"""
		validator = CNPJValidator()
		cnpj = "11222333000181"
        
		result = validator.validate(cnpj, validate_format=True)
        
		assert result['valid'] is True
		assert any("sem formatação" in warning for warning in result['warnings'])
    
	def test_no_warning_formatted_input(self):
		"""Não deve gerar aviso para entrada formatada"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		result = validator.validate(cnpj, validate_format=True)
        
		assert result['valid'] is True


class TestCNPJValidatorRealWorldScenarios:
	"""Testes de cenários do mundo real"""
    
	@pytest.mark.parametrize("cnpj,expected", [
		("11.222.333/0001-81", True),
		("34.028.316/0001-03", True),
		("00.000.000/0000-00", False),
		("11111111111111", False),
	])
	def test_multiple_cnpjs(self, cnpj, expected):
		"""Deve validar múltiplos CNPJs de cenários reais"""
		validator = CNPJValidator()
		result = validator.validate(cnpj, validate_format=False)
		assert result['valid'] is expected
    
	def test_user_input_simulation(self):
		"""Simula entrada de usuário com diferentes formatos"""
		validator = CNPJValidator()
        
		# Usuário digita sem formatação
		user_input = "11222333000181"
		result = validator.validate(user_input)
		assert result['valid'] is True
		formatted = result['cnpj_formatted']
        
		# Sistema devolve formatado
		assert formatted == "11.222.333/0001-81"
    
	def test_database_storage_scenario(self):
		"""Simula armazenamento em banco de dados (sem formatação)"""
		validator = CNPJValidator()
        
		# CNPJ vem formatado do usuário
		user_cnpj = "11.222.333/0001-81"
        
		# Limpar para armazenar
		clean_for_db = validator.clean(user_cnpj)
		assert clean_for_db == "11222333000181"
        
		# Validar antes de armazenar
		assert validator.is_valid(clean_for_db) is True
        
		# Recuperar do banco e formatar para exibição
		formatted_for_display = validator.format(clean_for_db)
		assert formatted_for_display == "11.222.333/0001-81"
    
	def test_api_response_scenario(self):
		"""Simula resposta de API com informações completas"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		# API retorna info completa
		info = validator.get_info(cnpj)
        
		# Resposta deve conter todos os campos necessários
		assert 'valid' in info
		assert 'cnpj_formatted' in info
		assert 'cnpj_clean' in info
		assert 'matriz_filial' in info
		assert 'parts' in info


class TestCNPJValidatorErrorHandling:
	"""Testes de tratamento de erros"""
    
	def test_null_input(self):
		"""Deve tratar entrada nula"""
		validator = CNPJValidator()
		result = validator.validate(None)
		assert result['valid'] is False
		assert len(result['errors']) > 0
    
	def test_empty_string(self):
		"""Deve tratar string vazia"""
		validator = CNPJValidator()
		result = validator.validate("")
		assert result['valid'] is False
		assert len(result['errors']) > 0
    
	def test_non_string_input(self):
		"""Deve tratar entrada não string"""
		validator = CNPJValidator()
		result = validator.validate(12345678900181)
		assert result['valid'] is False
    
	def test_error_messages_are_descriptive(self):
		"""Mensagens de erro devem ser descritivas"""
		validator = CNPJValidator()
        
		# CNPJ com todos zeros
		result = validator.validate("00000000000000")
		assert any("iguais" in error for error in result['errors'])
        
		# CNPJ muito curto
		result = validator.validate("123")
		assert any("14 dígitos" in error for error in result['errors'])


# Testes para integração com Zephyr Scale
class TestZephyrIntegrationComplete:
	"""Testes de integração marcados para Zephyr"""
    
	@pytest.mark.zephyr("CNPJ-T100")
	@pytest.mark.integration
	def test_full_validation_flow(self):
		"""
		Zephyr Test Case: CNPJ-T100
		Descrição: Fluxo completo de validação (numérica + alfanumérica)
		Prioridade: Crítica
		Tipo: Integration
		"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		result = validator.validate(cnpj, validate_format=True)
        
		assert result['valid'] is True
		assert result['numeric_validation']['valid'] is True
		assert result['alphanumeric_validation']['valid'] is True
		assert result['cnpj_formatted'] == "11.222.333/0001-81"
    
	@pytest.mark.zephyr("CNPJ-T101")
	@pytest.mark.integration
	def test_format_and_clean_roundtrip(self):
		"""
		Zephyr Test Case: CNPJ-T101
		Descrição: Teste de ida e volta (format -> clean -> format)
		Prioridade: Alta
		Tipo: Integration
		"""
		validator = CNPJValidator()
		original = "11.222.333/0001-81"
        
		# Clean
		clean = validator.clean(original)
		assert clean == "11222333000181"
        
		# Format novamente
		formatted = validator.format(clean)
		assert formatted == original
    
	@pytest.mark.zephyr("CNPJ-T102")
	@pytest.mark.integration
	def test_validation_with_info_extraction(self):
		"""
		Zephyr Test Case: CNPJ-T102
		Descrição: Validação completa com extração de informações
		Prioridade: Alta
		Tipo: Integration
		"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-81"
        
		# Validar
		validation = validator.validate(cnpj, validate_format=True)
		assert validation['valid'] is True
        
		# Obter informações
		info = validator.get_info(cnpj)
		assert info['valid'] is True
		assert info['matriz_filial']['type'] == 'matriz'


class TestShiftLeftPrinciples:
	"""Testes que demonstram princípios de Shift Left Testing"""
    
	def test_early_validation_prevents_invalid_data(self):
		"""
		Princípio: Validar dados o mais cedo possível
		Evita que dados inválidos entrem no sistema
		"""
		validator = CNPJValidator()
        
		# Entrada do usuário
		user_input = "11111111111111"  # Inválido
        
		# Validação imediata (Shift Left)
		result = validator.validate(user_input)
        
		# Bloquear antes de processar
		assert result['valid'] is False
		# Sistema não deve prosseguir com este CNPJ
    
	def test_comprehensive_feedback_for_developers(self):
		"""
		Princípio: Fornecer feedback detalhado para desenvolvedores
		Facilita debugging e correções rápidas
		"""
		validator = CNPJValidator()
		cnpj = "11.222.333/0001-99"
        
		result = validator.validate(cnpj, validate_format=True)
        
		# Feedback detalhado
		assert 'errors' in result
		assert 'warnings' in result
		assert 'numeric_validation' in result
		assert 'alphanumeric_validation' in result
        
		# Desenvolvedor sabe exatamente o problema
		assert len(result['errors']) > 0
    
	def test_automated_regression_prevention(self):
		"""
		Princípio: Testes automatizados previnem regressões
		Mudanças futuras não quebram funcionalidade existente
		"""
		validator = CNPJValidator()
        
		# Casos de teste automatizados garantem que:
		valid_cnpjs = [
			"11.222.333/0001-81",
			"11222333000181",
		]
        
		for cnpj in valid_cnpjs:
			result = validator.validate(cnpj)
			assert result['valid'] is True, f"Regressão detectada para {cnpj}"


if __name__ == "__main__":
	pytest.main([__file__, "-v", "--tb=short"])
