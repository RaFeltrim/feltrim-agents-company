# Handoff Protocol

## Objetivo

Evitar perda de contexto quando o trabalho sai de um agente e entra em outro.

## Quando fazer handoff

Faca handoff quando:

- o proximo passo estiver claramente fora do seu dominio
- a qualidade final depender de outra especialidade
- houver risco alto se a decisao for unilateral

## Handoff packet minimo

```yaml
from_agent: string
to_agent: string
reason: string
objective_for_receiver: string
artifacts_ready:
  - name: string
    path_or_inline: string
open_questions: []
known_risks: []
done_definition_for_receiver: []
priority: one_of[low, medium, high, critical]
```

## Exemplos de handoff

### PO -> TL

Quando a descoberta ja virou backlog e agora precisa virar desenho tecnico.

### TL -> Backend e Frontend

Quando a arquitetura ja foi escolhida e agora precisa virar implementacao.

### Backend -> QA

Quando a API ja tem contrato e precisa de cobertura, risco e teste.

### QA -> DevOps

Quando existe gate para release e precisam entrar automacoes, checks ou bloqueios.

## Regra de recepcao

Quem recebe um handoff deve validar:

1. objetivo
2. artefatos disponiveis
3. riscos ja conhecidos
4. o que ainda falta para aceitar a tarefa

## Anti-padroes

- "segue ai" sem contexto
- handoff sem artefato anexado
- handoff que reabre decisoes ja congeladas sem justificativa
- handoff que esconde risco para parecer mais rapido
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
