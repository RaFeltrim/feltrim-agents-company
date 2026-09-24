# Cliente da API da Receita Federal para consulta de CNPJ

class CNPJData:
	"""Stub para dados de CNPJ (ajuste conforme implementação real)."""
	def __init__(self, cnpj="", razao_social="", nome_fantasia="", situacao_cadastral="", data_situacao_cadastral="", motivo_situacao_cadastral="", data_abertura="", porte="", natureza_juridica="", cnae_principal=None, cnaes_secundarios=None, endereco=None, telefone="", email="", capital_social=0.0, quadro_societario=None, simples_nacional=None, mei=False, raw_data=None):
		self.cnpj = cnpj
		self.razao_social = razao_social
		self.nome_fantasia = nome_fantasia
		self.situacao_cadastral = situacao_cadastral
		self.data_situacao_cadastral = data_situacao_cadastral
		self.motivo_situacao_cadastral = motivo_situacao_cadastral
		self.data_abertura = data_abertura
		self.porte = porte
		self.natureza_juridica = natureza_juridica
		self.cnae_principal = cnae_principal or {}
		self.cnaes_secundarios = cnaes_secundarios or []
		self.endereco = endereco or {}
		self.telefone = telefone
		self.email = email
		self.capital_social = capital_social
		self.quadro_societario = quadro_societario or []
		self.simples_nacional = simples_nacional or {}
		self.mei = mei
		self.raw_data = raw_data or {}

class ReceitaFederalAPI:
	pass  # Implementação real deve ser migrada

class ReceitaFederalAPIError(Exception):
	pass
