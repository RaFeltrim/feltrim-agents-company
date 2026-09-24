# Core Protocols

Os 8 protocolos abaixo formam a camada sistemica do Feltrim Agents Framework.
Sao genericos: aplicaveis a qualquer agente, qualquer pack, qualquer projeto.

Carregam o agente nesta ordem (ver `AGENT_RUNTIME_WRAPPER.md`):

1. Contexto do projeto
2. `AGENT_RUNTIME_WRAPPER.md` - ordem de composicao da instrucao
3. `AGENT_IO_CONTRACT.md` - request packet + response envelope minimos
4. `HANDOFF_PROTOCOL.md` - como passar trabalho entre agentes
5. `MEMORY_AND_RAG_POLICY.md` - quando gravar, quando recuperar, quando deixar morrer
6. `EVALS_AND_MONITORING.md` - scorecard, logs e gates minimos
7. Gem do agente (`core/agents/gem_*.md` ou `packs/<pack>/agents/gem_*.md`)
8. Request packet da tarefa

Quando aplicavel:

- `ORCHESTRATION_POLICY.md` - solo / paired / squad e politica de conflito
- `DELIVERY_AND_PRODUCT_SURFACES.md` - human-readable / machine-readable / execution-ready / product surface
- `MULTIMODAL_EXTENSION.md` - apenas se o problema depender de imagem, screenshot, OCR, audio ou video

## Origem

Todos extraidos do blueprint do framework FF v3 (2026). Conteudo
creditado a Rafael Feltrim.

## Regra de evolucao

Mudanca em qualquer protocolo abre commit proprio e atualiza:

- este `README.md`
- `core/docs/OPERATING_MODEL.md` (mapa para os 10 pilares classicos)
- `core/CLAUDE.md` se o boot mudar
- pack que dependa diretamente do protocolo alterado
