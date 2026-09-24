# language: pt
# encoding: utf-8
# PROJETO-EXEMPLO - Parametrizacao ficticia de cobranca e recebimento
# Versao: treinamento
# Total de Cenarios: 8
# Gerado em: 2026-03-20

@PROJETO-EXEMPLO @Treinamento @BDD @CMS
Funcionalidade: PROJETO-EXEMPLO - Parametrizacao ficticia de cobranca e recebimento
  Parametrizar o Projeto exemplo para separar cobrancas e
  recebimentos entre um sistema legado ficticio e um sistema atual
  ficticio, com produtos, contas de controle e carteiras vinculadas
  ao novo fluxo.

  @CT-1 @AC-1
  Cenário: Reflexo da parametrizacao nos modulos
    Dado a necessidade de separar cobrancas e recebimentos entre dois fluxos ficticios
    Quando a parametrizacao do Projeto exemplo for concluida
    Então a configuracao deve refletir em todos os modulos sem misturar os fluxos

  @CT-2 @AC-2
  Cenário: Criacao das contas de controle
    Dado os tres tipos de cobranca definidos para o treinamento
    Quando as contas de controle forem cadastradas
    Então devem ser criadas 3 contas distintas para o Projeto exemplo

  @CT-3 @AC-3 @AC-4
  Cenário: Criacao dos produtos e das operacoes
    Dado os novos produtos ficticios definidos para o treinamento
    Quando a parametrizacao dos produtos for realizada
    Então devem ser criados 3 produtos com codigos distintos de operacao

  @CT-4 @AC-5
  Cenário: Configuracao da Ocorrencia Tipo A
    Dado um registro classificado como Ocorrencia Tipo A
    Quando a cobranca correspondente for gerada
    Então o produto deve utilizar exclusivamente a carteira 101

  @CT-5 @AC-6
  Cenário: Configuracao da Ocorrencia Tipo B
    Dado um registro classificado como Ocorrencia Tipo B
    Quando a cobranca correspondente for gerada
    Então o produto deve utilizar a carteira 202

  @CT-6 @AC-6
  Cenário: Emissao avulsa pelos canais de atendimento
    Dado uma emissao avulsa pelos canais Portal Exemplo, Central de Atendimento ou Canal Interno
    Quando o boleto avulso for gerado
    Então a emissao deve utilizar o produto 3 com a carteira 202

  @CT-7 @AC-7
  Cenário: Definicao do banco emissor
    Dado um boleto gerado para qualquer um dos produtos do Projeto exemplo
    Quando a cobranca for disponibilizada
    Então o Banco Exemplo deve ser o emissor do boleto

  @CT-8 @AC-8
  Cenário: Geracao do arquivo de retorno
    Dado um retorno gerado para os produtos do Projeto exemplo
    Quando o arquivo de retorno for disponibilizado
    Então o arquivo deve ser gerado em diretorio configuravel
