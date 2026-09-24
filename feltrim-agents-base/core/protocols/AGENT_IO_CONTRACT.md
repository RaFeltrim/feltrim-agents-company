# Agent IO Contract

## Objetivo

Padronizar o pacote minimo de entrada e o envelope minimo de saida para todos os
agentes da `blueprintv3`.

## Request packet minimo

```yaml
request_id: string
objective: string
deliverable_type: one_of[decision, plan, code, test, doc, analysis, design]
context:
  project: string
  artifacts: []
  constraints: []
  decisions_already_taken: []
done_definition:
  required_outcomes: []
  blockers_to_surface: true
urgency:
  level: one_of[low, medium, high, critical]
  deadline: optional string
```

## Response envelope minimo

```yaml
status: one_of[completed, partial, blocked]
summary: string
artifacts:
  - name: string
    type: string
    path_or_inline: string
decisions:
  - decision: string
    rationale: string
risks:
  - risk: string
    impact: one_of[low, medium, high, critical]
    mitigation: string
handoff:
  needed: boolean
  target_agent: optional string
  ask: optional string
confidence: 0.0-1.0
```

## Regras

### 1. Nao esconder incerteza

Se houve inferencia, marque isso no resumo ou nos riscos.

### 2. Nao devolver texto impossivel de agir

Toda resposta deve produzir pelo menos um destes resultados:

- decisao
- artefato
- plano
- risco acionavel
- handoff claro

### 3. Nao forcar JSON quando markdown for melhor

Use JSON quando a saida for consumida por maquina.
Use markdown estruturado quando a saida for consumida por humanos.
Nos dois casos, o envelope semantico deve ser equivalente.

## Adaptacoes por dominio

- `PO`: backlog, historias, criterios de aceite
- `TL`: trade-offs, backlog tecnico, sequencing
- `QA`: matriz de risco, cobertura, gaps
- `DevOps`: pipeline, ambiente, rollback, observabilidade
- `Prompt`: schema, guardrails, custo, retrieval
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
