"""
Testes para o CLI do CNPJ Validator
Garante cobertura de código do módulo cli.py
"""

import pytest
import sys
import json
from io import StringIO
from unittest.mock import patch, mock_open
from cnpj_validator.cli import CNPJValidatorCLI, create_parser, main


class TestCNPJValidatorCLI:
	"""Testes para a classe CNPJValidatorCLI."""
    
	def setup_method(self):
		"""Setup executado antes de cada teste."""
		self.cli = CNPJValidatorCLI()
    
	def test_init(self):
		"""Testa inicialização do CLI."""
		assert self.cli is not None
		assert self.cli.validator is not None
		assert self.cli.alphanumeric_validator is not None
    
	def test_validate_valid_cnpj(self):
		"""Testa validação de CNPJ válido."""
		result = self.cli.validate("11.222.333/0001-81")
        
		assert result['valid'] is True
		assert result['cnpj'] == "11.222.333/0001-81"
		assert 'errors' in result
    
	def test_validate_invalid_cnpj(self):
		"""Testa validação de CNPJ inválido."""
		result = self.cli.validate("11111111111111")
        
		assert result['valid'] is False
		assert 'errors' in result
		assert len(result['errors']) > 0
    
	def test_validate_with_verbose(self):
		"""Testa validação com modo verbose."""
		result = self.cli.validate("11.222.333/0001-81", verbose=True)
        
		assert result['valid'] is True
		assert 'numeric_validation' in result
		assert 'alphanumeric_validation' in result
    
	def test_validate_empty_cnpj(self):
		"""Testa validação de CNPJ vazio."""
		result = self.cli.validate("")
        
		assert result['valid'] is False
		assert len(result['errors']) > 0
    
	def test_generate_numeric_cnpj(self):
		"""Testa geração de CNPJ numérico."""
		cnpjs = self.cli.generate(count=1, alphanumeric=False)
        
		assert cnpjs is not None
		assert len(cnpjs) == 1
		cnpj = cnpjs[0]
		assert len(cnpj.replace(".", "").replace("/", "").replace("-", "")) == 14
        
		# Valida o CNPJ gerado
		result = self.cli.validate(cnpj)
		assert result['valid'] is True
    
	def test_generate_alphanumeric_cnpj(self):
		"""Testa geração de CNPJ alfanumérico."""
		cnpjs = self.cli.generate(count=1, alphanumeric=True)
        
		assert cnpjs is not None
		assert len(cnpjs) == 1
		cnpj = cnpjs[0]
		assert len(cnpj.replace(".", "").replace("/", "").replace("-", "")) == 14
    
	def test_generate_with_root(self):
		"""Testa geração de CNPJ com raiz específica."""
		cnpjs = self.cli.generate(count=1, alphanumeric=False, root="11222333")
        
		assert cnpjs is not None
		assert len(cnpjs) == 1
		cnpj = cnpjs[0]
		assert cnpj.startswith("11.222.333")
    
	def test_generate_multiple_cnpjs(self):
		"""Testa geração de múltiplos CNPJs."""
		cnpjs = self.cli.generate(count=5, alphanumeric=False)
        
		assert len(cnpjs) == 5
		for cnpj in cnpjs:
			result = self.cli.validate(cnpj)
			assert result['valid'] is True
    
	def test_generate_multiple_alphanumeric(self):
		"""Testa geração de múltiplos CNPJs alfanuméricos."""
		cnpjs = self.cli.generate(count=3, alphanumeric=True)
        
		assert len(cnpjs) == 3
		assert all(cnpj is not None for cnpj in cnpjs)
    
	def test_format_valid_cnpj(self):
		"""Testa formatação de CNPJ válido."""
		formatted = self.cli.format("11222333000181")
        
		assert formatted == "11.222.333/0001-81"
    
	def test_format_already_formatted(self):
		"""Testa formatação de CNPJ já formatado."""
		formatted = self.cli.format("11.222.333/0001-81")
        
		assert formatted == "11.222.333/0001-81"
    
	def test_format_invalid_cnpj(self):
		"""Testa formatação de CNPJ inválido."""
		formatted = self.cli.format("11111111111111")
		# format apenas formata, não valida
		assert formatted == "11.111.111/1111-11"
    
	def test_info_valid_cnpj(self):
		"""Testa obtenção de informações de CNPJ válido."""
		info = self.cli.info("11.222.333/0001-81")
        
		assert info is not None
		assert 'valid' in info
		assert info['valid'] is True
    
	def test_info_invalid_cnpj(self):
		"""Testa obtenção de informações de CNPJ inválido."""
		info = self.cli.info("11111111111111")
        
		assert info is not None
		assert 'valid' in info
		assert info['valid'] is False
    
	def test_batch_validate_file(self):
		"""Testa validação em lote de arquivo."""
		mock_file_content = "11.222.333/0001-81\n34.028.316/0001-03\n11111111111111\n"
        
		with patch('builtins.open', mock_open(read_data=mock_file_content)):
			results = self.cli.batch_validate("test.txt")
        
		assert len(results) == 3
		assert results[0]['valid'] is True
		assert results[1]['valid'] is True
		assert results[2]['valid'] is False
    
	def test_batch_validate_empty_file(self):
		"""Testa validação em lote de arquivo vazio."""
		mock_file_content = "\n\n\n"
        
		with patch('builtins.open', mock_open(read_data=mock_file_content)):
			results = self.cli.batch_validate("test.txt")
        
		assert len(results) == 0


class TestCLIParser:
	"""Testes para o parser de argumentos do CLI."""
    
	def test_create_parser(self):
		"""Testa criação do parser."""
		parser = create_parser()
        
		assert parser is not None
		assert parser.prog == 'cnpj-validator'
    
	def test_parser_validate_command(self):
		"""Testa parsing do comando validate."""
		parser = create_parser()
		args = parser.parse_args(['validate', '11.222.333/0001-81'])
        
		assert args.command == 'validate'
		assert args.cnpj == '11.222.333/0001-81'
    
	def test_parser_validate_with_verbose(self):
		"""Testa parsing do comando validate com --verbose."""
		parser = create_parser()
		args = parser.parse_args(['validate', '11.222.333/0001-81', '--verbose'])
        
		assert args.command == 'validate'
		assert args.verbose is True
    
	def test_parser_validate_with_json(self):
		"""Testa parsing do comando validate com --json."""
		parser = create_parser()
		args = parser.parse_args(['validate', '11.222.333/0001-81', '--json'])
        
		assert args.command == 'validate'
		assert args.json is True
    
	def test_parser_generate_command(self):
		"""Testa parsing do comando generate."""
		parser = create_parser()
		args = parser.parse_args(['generate'])
        
		assert args.command == 'generate'
    
	def test_parser_generate_with_count(self):
		"""Testa parsing do comando generate com --count."""
		parser = create_parser()
		args = parser.parse_args(['generate', '--count', '5'])
        
		assert args.command == 'generate'
		assert args.count == 5
    
	def test_parser_generate_alphanumeric(self):
		"""Testa parsing do comando generate com --alphanumeric."""
		parser = create_parser()
		args = parser.parse_args(['generate', '--alphanumeric'])
        
		assert args.command == 'generate'
		assert args.alphanumeric is True
    
	def test_parser_generate_with_root(self):
		"""Testa parsing do comando generate com --root."""
		parser = create_parser()
		args = parser.parse_args(['generate', '--root', '11222333'])
        
		assert args.command == 'generate'
		assert args.root == '11222333'
    
	def test_parser_format_command(self):
		"""Testa parsing do comando format."""
		parser = create_parser()
		args = parser.parse_args(['format', '11222333000181'])
        
		assert args.command == 'format'
		assert args.cnpj == '11222333000181'
    
	def test_parser_info_command(self):
		"""Testa parsing do comando info."""
		parser = create_parser()
		args = parser.parse_args(['info', '11.222.333/0001-81'])
        
		assert args.command == 'info'
		assert args.cnpj == '11.222.333/0001-81'
    
	def test_parser_batch_command(self):
		"""Testa parsing do comando batch."""
		parser = create_parser()
		args = parser.parse_args(['batch', 'cnpjs.txt'])
        
		assert args.command == 'batch'
		assert args.file == 'cnpjs.txt'
    
	def test_parser_batch_with_json(self):
		"""Testa parsing do comando batch com --json."""
		parser = create_parser()
		args = parser.parse_args(['batch', 'cnpjs.txt', '--json'])
        
		assert args.command == 'batch'
		assert args.json is True
    
	def test_parser_batch_with_summary(self):
		"""Testa parsing do comando batch com --summary."""
		parser = create_parser()
		args = parser.parse_args(['batch', 'cnpjs.txt', '--summary'])
        
		assert args.command == 'batch'
		assert args.summary is True


class TestCLIMainFunction:
	"""Testes para a função main do CLI."""
    
	@patch('sys.argv', ['cnpj-validator', 'validate', '11.222.333/0001-81'])
	@patch('sys.stdout', new_callable=StringIO)
	def test_main_validate_valid(self, mock_stdout):
		"""Testa execução da função main com validate válido."""
		try:
			main()
		except SystemExit:
			pass
        
		output = mock_stdout.getvalue()
		assert "válido" in output.lower() or "✅" in output
    
	@patch('sys.argv', ['cnpj-validator', 'validate', '11111111111111'])
	@patch('sys.stdout', new_callable=StringIO)
	def test_main_validate_invalid(self, mock_stdout):
		"""Testa execução da função main com validate inválido."""
		try:
			main()
		except SystemExit:
			pass
        
		output = mock_stdout.getvalue()
		assert "inválido" in output.lower() or "❌" in output
    
	@patch('sys.argv', ['cnpj-validator', 'generate'])
	@patch('sys.stdout', new_callable=StringIO)
	def test_main_generate(self, mock_stdout):
		"""Testa execução da função main com generate."""
		try:
			main()
		except SystemExit:
			pass
        
		output = mock_stdout.getvalue()
		assert len(output.strip()) > 0
    
	@patch('sys.argv', ['cnpj-validator', 'format', '11222333000181'])
	@patch('sys.stdout', new_callable=StringIO)
	def test_main_format(self, mock_stdout):
		"""Testa execução da função main com format."""
		try:
			main()
		except SystemExit:
			pass
        
		output = mock_stdout.getvalue()
		assert "11.222.333/0001-81" in output
    
	@patch('sys.argv', ['cnpj-validator'])
	@patch('sys.stdout', new_callable=StringIO)
	def test_main_no_command(self, mock_stdout):
		"""Testa execução da função main sem comando."""
		with pytest.raises(SystemExit) as excinfo:
			main()
        
		assert excinfo.value.code == 0


class TestCLIIntegration:
	"""Testes de integração do CLI."""
    
	def test_validate_and_format_workflow(self):
		"""Testa workflow completo: validar e formatar."""
		cli = CNPJValidatorCLI()
        
		# Validar
		result = cli.validate("11222333000181")
		assert result['valid'] is True
        
		# Formatar
		formatted = cli.format("11222333000181")
		assert formatted == "11.222.333/0001-81"
    
	def test_generate_and_validate_workflow(self):
		"""Testa workflow completo: gerar e validar."""
		cli = CNPJValidatorCLI()
        
		# Gerar
		cnpjs = cli.generate(count=1, alphanumeric=False)
		cnpj = cnpjs[0]
        
		# Validar
		result = cli.validate(cnpj)
		assert result['valid'] is True
    
	def test_batch_validate_workflow(self):
		"""Testa workflow de validação em lote."""
		cli = CNPJValidatorCLI()
        
		mock_file_content = "11.222.333/0001-81\n34.028.316/0001-03\n"
        
		with patch('builtins.open', mock_open(read_data=mock_file_content)):
			results = cli.batch_validate("test.txt")
        
		assert len(results) == 2
		assert all(r['valid'] for r in results)


class TestCLIErrorHandling:
	"""Testes de tratamento de erros do CLI."""
    
	def test_validate_none_cnpj(self):
		"""Testa validação com None."""
		cli = CNPJValidatorCLI()
		result = cli.validate(None)
        
		assert result['valid'] is False
		assert 'errors' in result
    
	def test_format_none_cnpj(self):
		"""Testa formatação com None."""
		cli = CNPJValidatorCLI()
        
		with pytest.raises(AttributeError):
			cli.format(None)
    
	def test_info_none_cnpj(self):
		"""Testa info com None."""
		cli = CNPJValidatorCLI()
		info = cli.info(None)
        
		assert info is not None
		assert info.get('valid') is False
    
	def test_batch_validate_nonexistent_file(self):
		"""Testa validação em lote com arquivo inexistente."""
		cli = CNPJValidatorCLI()
        
		with pytest.raises(FileNotFoundError):
			cli.batch_validate("arquivo_inexistente.txt")
    
	def test_generate_with_invalid_root(self):
		"""Testa geração com raiz inválida."""
		cli = CNPJValidatorCLI()
        
		# Raiz muito curta
		cnpjs = cli.generate(count=1, alphanumeric=False, root="123")
		assert cnpjs is not None  # Deve gerar mesmo com raiz curta
		assert len(cnpjs) == 1
