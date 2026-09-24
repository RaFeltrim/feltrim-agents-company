# Operating Model - Blueprint v3

## Objetivo

Explicar como a `blueprintv3` cobre os pilares classicos de um sistema de agentes.

## Mapeamento dos 10 pilares

### 1. Role and goal

Coberto por:

- gems especializadas por dominio
- `docs/SQUAD_INDEX.md`

### 2. Structured input and output

Coberto por:

- `protocols/AGENT_IO_CONTRACT.md`
- `protocols/AGENT_RUNTIME_WRAPPER.md`

### 3. Behavior and protocol

Coberto por:

- `protocols/ORCHESTRATION_POLICY.md`
- `protocols/HANDOFF_PROTOCOL.md`

### 4. Reasoning and tool use

Coberto por:

- gems por especialidade
- envelopes de decisao e riscos nos outputs

### 5. Multi-agent logic

Coberto por:

- `docs/SQUAD_INDEX.md`
- `protocols/ORCHESTRATION_POLICY.md`

### 6. Memory and long-term context

Coberto por:

- `memory/MEMORY.md`
- `protocols/MEMORY_AND_RAG_POLICY.md`

### 7. Voice and vision

Coberto opcionalmente por:

- `protocols/MULTIMODAL_EXTENSION.md`

### 8. Deliver the output

Coberto por:

- `protocols/DELIVERY_AND_PRODUCT_SURFACES.md`
- `protocols/AGENT_IO_CONTRACT.md`

### 9. Wrap in a UI

Coberto por:

- `protocols/DELIVERY_AND_PRODUCT_SURFACES.md`
- agentes de frontend, UX e devops

### 10. Evaluate and monitor

Coberto por:

- `protocols/EVALS_AND_MONITORING.md`

## Diferenca principal da v3

A versao anterior ja era forte em especializacao e colaboracao.
A v3 adiciona a cola sistemica que faltava:

- padrao de runtime
- padrao de contrato
- padrao de memoria
- padrao de eval
- padrao de delivery

## Regra operacional

Se um agente nao sabe:

- o que recebe
- o que devolve
- para quem faz handoff
- como sera avaliado

entao ele ainda nao esta pronto para producao dentro da v3.
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
