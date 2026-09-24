---
name: agent_capability_review_template
description: Review periodica das capacidades, certificacoes, unlocks e desempenho de um agente
type: reference
---

# Capability Review: <Nome - Papel> - <AAAA-MM-DD>

> Esta review e a unidade auditavel que
> autoriza uma promocao, uma certificacao nova ou um unlock. Sem review
> preenchida, nada e movido em `agent-profile-<slug>.md`.

**Agente:** `<Nome - Papel>` (`core/agents/<gem>.md` ou `packs/<pack>/agents/<gem>.md`)
**Revisor humano:** <Rafael Feltrim ou delegado autorizado>
**Revisor agente:** `Sofia CIAO` (gate executivo)
**Periodo coberto:** <AAAA-MM-DD> a <AAAA-MM-DD>
**Janela:** <trimestral | pos-projeto | pos-pack | sob demanda>

## Contexto da review

- Motivo da review (sprint fechada, projeto encerrado, candidatura a nivel,
  pedido de unlock, incidente, etc.):
- Pack(s) em que o agente atuou no periodo:
- Numero de tarefas atendidas:
- Numero de handoffs liderados / recebidos:

## Evidencias acumuladas

Lista resumida das principais entregas do periodo, com link para artefato
auditavel. Sem evidencia auditavel, nao conta.

| Tipo | Descricao | Link auditavel | Resultado |
|------|-----------|----------------|-----------|
| ADR | | | |
| Bug critico detectado | | | |
| CT executado | | | |
| Refatoracao | | | |
| Pack novo | | | |

## Desempenho contra criterios de nivel

Comparar contra `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md`.

- Nivel atual: <Nx>
- Nivel almejado nesta review: <Ny>
- Criterios para o nivel almejado:
  - [ ] Criterio 1 (descricao) - evidencia: <link>
  - [ ] Criterio 2 - evidencia: <link>
  - [ ] Criterio 3 - evidencia: <link>
- Criterios atendidos: <N de M>

## Certificacoes candidatas

Lista de certificacoes que o agente quer conquistar nesta janela. Ver
`core/docs/AGENT_CERTIFICATIONS.md`.

- [ ] <CODIGO_CERT> - <nome longo> - prova exigida: <link>
- [ ] <CODIGO_CERT> - <nome longo> - prova exigida: <link>

## Habilidades pleiteadas (unlocks)

Lista de habilidades que o agente quer desbloquear. Ver
`core/docs/AGENT_UNLOCKS.md`.

- [ ] <slug-unlock> - justificativa: <texto> - prova: <link>
- [ ] <slug-unlock> - justificativa: <texto> - prova: <link>

## Riscos e regressoes observados

- Comportamentos a corrigir:
- Anti-padroes que apareceram:
- Tarefas onde o agente nao deveria ter aceitado e aceitou:
- Tarefas onde o agente deveria ter escalado e nao escalou:

## Decisao da review

Marque uma:

- [ ] Aprovado para promocao: N<x> -> N<y>
- [ ] Aprovado parcialmente: novas certs / unlocks conquistados, sem subir de nivel
- [ ] Recusado: nivel mantido, recomendacoes abaixo
- [ ] Backstep: nivel cai (caso de regressao grave); requer justificativa explicita

### Recomendacoes para a proxima janela

- Acao 1:
- Acao 2:
- Acao 3:

## Acao consequente (a ser executada apos approval)

- [ ] Atualizar `core/memory/agents/<slug>/agent-profile.md`
- [ ] Atualizar `core/docs/SQUAD_INDEX.md` (colunas Nivel / Certificacoes / Unlocks)
- [ ] Adicionar entrada em `core/memory/agents/<slug>/capability-reviews/` (arquivo desta review)
- [ ] Notificar `<canal humano>` sobre mudanca de nivel ou unlock relevante
- [ ] Atualizar `governance/PROMOTION_POLICY.md` se a review descobriu lacuna na politica

## Assinaturas

- Sofia CIAO (agente): <APROVADO | RECUSADO | CONDICIONADO> - <AAAA-MM-DD>
- Decisor humano: <APROVADO | RECUSADO> - <AAAA-MM-DD>

## Notas

<Espaco livre para observacoes que nao couberam acima>
