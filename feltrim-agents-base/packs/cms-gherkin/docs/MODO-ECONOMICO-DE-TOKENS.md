# Modo Economico de Tokens

Este modo existe para reduzir custo, retrabalho e variacao entre execucoes.

## Principio central

O modelo deve produzir apenas a inteligencia necessaria uma vez.

Depois disso:
- a fonte estruturada vira a verdade operacional
- os artefatos finais saem por script local
- problemas e solucoes ficam registrados para reutilizacao futura

## Estrutura nova do pacote

- `FONTES-ESTRUTURADAS/` -> fonte unica em JSON por PI/US
- `FERRAMENTAS/gerar_artefatos.py` -> gera analise, planilha e feature
- `FERRAMENTAS/registrar_problema.py` -> registra problemas e solucoes
- `MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md` -> historico do projeto

## Leitura minima antes de agir

1. `MODO-ECONOMICO-DE-TOKENS.md`
2. `Padrao-a-Seguir/EXEMPLO-PADRAO-APROVADO.md`
3. `MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md`
4. `USs-Avaliar/` na US alvo
5. `FONTES-ESTRUTURADAS/` na fonte da US alvo, se ja existir

## Fluxo recomendado

1. Ler apenas a US alvo e o contexto minimo acima.
2. Criar ou atualizar `FONTES-ESTRUTURADAS/<SLUG>.json`.
3. Rodar o gerador local:
   `python CMS-Gherkin/FERRAMENTAS/gerar_artefatos.py --fonte CMS-Gherkin/FONTES-ESTRUTURADAS/<SLUG>.json`
4. Validar cobertura dos ACs.
5. Se houver problema, registrar:
   `python CMS-Gherkin/FERRAMENTAS/registrar_problema.py --titulo "..." --contexto "..." --causa "..." --solucao "..."`

## O que economiza tokens de verdade

- evitar pedir para o modelo escrever tres artefatos completos do zero
- reutilizar a fonte estruturada existente em vez de reprocessar tudo
- ler o guia compacto antes dos guias longos
- deixar formatacao repetitiva para script local

## O que continua gastando token

- leitura inicial da US
- extracao dos ACs e regras de negocio
- analise de inconsistencias reais do documento funcional

## Regra operacional

Se a informacao ja estiver na fonte estruturada ou na memoria operacional, reutilize.
Nao refaca raciocinio ou texto sem necessidade.
