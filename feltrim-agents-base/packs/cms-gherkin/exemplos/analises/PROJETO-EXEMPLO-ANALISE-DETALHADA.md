# PROJETO-EXEMPLO - Analise Detalhada

## 1. Identificacao

- Projeto: `PROJETO-EXEMPLO`
- Titulo: `Parametrizacao ficticia de cobranca e recebimento`
- Versao: `treinamento`
- Artefatos associados:
  - `USs-Avaliar/PROJETO-EXEMPLO.docx`
  - `ANALISES/PROJETO-EXEMPLO-ANALISE-DETALHADA.md`
  - `Processados_BDD/PROJETO-EXEMPLO.xlsx`
  - `xray_export/PROJETO-EXEMPLO.feature`

## 2. Leitura funcional da US

### Problema de negocio

A US descreve a necessidade de separar cobrancas e recebimentos entre um sistema legado ficticio e um sistema atual ficticio, evitando mistura operacional.

### Objetivo funcional

Criar a parametrizacao do Projeto exemplo com contas de controle distintas, produtos distintos, codigos distintos de operacao, carteiras corretas por tipo de cobranca, reflexo em todos os modulos e geracao de arquivo de retorno.

### Contexto principal extraido da US

- O sistema precisa diferenciar recebimentos do fluxo legado e do fluxo atual.
- A separacao deve ocorrer sem impacto ao usuario final.
- A parametrizacao deve refletir em todos os modulos.
- As carteiras definidas para o treinamento devem ser reaproveitadas conforme a regra.

## 3. Regras de negocio extraidas

### RN01 - Criacao de produtos

Devem existir 3 produtos distintos.

- Produto 1: Ocorrencia Tipo A.
- Produto 2: Ocorrencia Tipo B.
- Produto 3: emissoes avulsas pelos canais de atendimento.

### RN02 - Canais de emissao

Os canais listados para o treinamento sao:

- Portal Exemplo.
- Central de Atendimento.
- Canal Interno.

### RN03 - Carteiras

As carteiras devem obedecer a separacao funcional.

- Carteira 101 e exclusiva para Ocorrencia Tipo A.
- Carteira 202 atende Ocorrencia Tipo B e emissoes avulsas.

### RN04 - Operacoes

Cada produto deve ter codigo de operacao distinto.

### RN05 - Contas de controle

Cada produto deve ter conta de controle distinta.

### RN06 - Banco emissor

Os boletos devem ter o Banco Exemplo como emissor.

### RN07 - Agenda

Os produtos devem seguir agenda D+0 apos o vencimento.

### RN08 - Retorno

O arquivo de retorno deve ser gerado em diretorio configuravel.

## 4. ACs oficiais consolidados

- `AC 1`: Parametrizacao refletida em todos os modulos.
- `AC 2`: Criacao de 3 contas de controle distintas.
- `AC 3`: Criacao de 3 produtos distintos.
- `AC 4`: Criacao de codigos distintos de operacao.
- `AC 5`: Uso da carteira 101 para Ocorrencia Tipo A.
- `AC 6`: Uso da carteira 202 para Ocorrencia Tipo B e emissoes avulsas.
- `AC 7`: Banco Exemplo como emissor.
- `AC 8`: Geracao de arquivo de retorno em diretorio configuravel.

## 5. Raciocinio utilizado para criar os cenarios

### Estrategia de decomposicao

O exemplo foi quebrado por blocos funcionais para manter cenarios claros, rastreaveis e faceis de revisar durante o treinamento.

### Cenario 1 - Reflexo da parametrizacao nos modulos

Cobre o requisito transversal de propagacao da configuracao.

### Cenario 2 - Criacao das contas de controle

Cobre a existencia de tres contas distintas.

### Cenario 3 - Criacao dos produtos e das operacoes

Agrupa produtos e operacoes, pois ambos surgem no mesmo momento da parametrizacao.

### Cenario 4 - Configuracao da Ocorrencia Tipo A

Isola a regra da carteira 101.

### Cenario 5 - Configuracao da Ocorrencia Tipo B

Isola a regra da carteira 202.

### Cenario 6 - Emissao avulsa pelos canais de atendimento

Explicita os canais e mantem a mesma expectativa funcional da carteira 202.

### Cenario 7 - Definicao do banco emissor

Torna verificavel a regra do emissor.

### Cenario 8 - Geracao do arquivo de retorno

Garante a existencia do retorno em diretorio configuravel.

## 6. Decisoes de modelagem

- Os nomes foram mantidos genericos para uso em treinamento.
- Os canais foram agrupados em um unico cenario porque levam ao mesmo resultado.
- Os valores e codigos usados sao ficticios.

## 7. Cobertura final

- total de ACs oficiais: `8`
- total de cenarios finais: `8`
- cobertura declarada: `100%`

## 8. Conclusao

O Projeto exemplo foi modelado como artefato de treinamento. O objetivo e demonstrar o metodo de avaliacao, rastreabilidade e geracao de BDDs sem expor informacoes de projetos reais.
