---
name: agent_profile_template
description: Perfil consolidado de agente (papel + nivel + certificacoes + unlocks + brain de referencia)
type: reference
---

# Perfil de Agente: <Nome - Papel curto>

> Snapshot leve do agente: une persona, senioridade, nivel atual,
> certificacoes conquistadas, habilidades desbloqueadas e brain de
> referencia. Serve como cartao executivo do agente no SQUAD_INDEX.

**Prompt canonico:** `core/agents/<gem>.md` ou `packs/<pack>/agents/<gem>.md`
**Brain operacional:** `core/memory/agents/<slug>/brain.md` ou
`packs/<pack>/brains/<slug>/brain.md`
**Ultima atualizacao:** <AAAA-MM-DD>
**Mantido por:** <decisor humano ou Sofia CIAO>

## Identidade

- Nome do agente:
- Papel curto:
- Papel longo:
- Tom / persona:
- Pack ativo principal: <core | cms-gherkin | us-avaliator | <pack-projeto> | outro>

## Senioridade e nivel

- Senioridade declarativa: <Junior | Pleno | Senior | Lead | Principal>
- Nivel atual: <N1 | N2 | N3 | N4 | N5>
- Data de promocao para o nivel atual: <AAAA-MM-DD>
- Proximo nivel almejado: <Nx>
- Criterios faltantes para o proximo nivel: ver
  `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md`

## Certificacoes internas

Lista de certificacoes conquistadas no programa Feltrim Agents. Ver catalogo
em `core/docs/AGENT_CERTIFICATIONS.md`.

- [ ] FA-FOUND (Feltrim Agents Foundation)
- [ ] Certificacao especifica de pack ativo (ex.: `<PACK>-FOUND`)
- [ ] Certificacao tecnica (ex.: PLAYWRIGHT-AUDIT, BDD-AUDIT, ADR-CRAFT)
- [ ] Certificacao de governanca (ex.: CIAO-GO-LIVE-READY)

Cada item preenchido vira `[x] <nome> - <AAAA-MM-DD> - assinado por <Sofia CIAO ou decisor humano>`.

## Habilidades desbloqueadas (unlocks)

Lista de habilidades operacionais que o agente ja pode usar sem nova
autorizacao. Ver catalogo em `core/docs/AGENT_UNLOCKS.md`.

- [ ] Pode abrir ADR sozinho
- [ ] Pode atualizar SQUAD_INDEX sem revisao
- [ ] Pode editar gem propria
- [ ] Pode propor pack novo
- [ ] Pode liderar squad temporario
- [ ] Pode aplicar veto tecnico (so CIAO)
- [ ] Pode atualizar status oficial em sistema externo
- [ ] Pode promover prototipo a MVP

## Especialidades atuais

Lista resumida das 5-10 especialidades-chave do agente. Para detalhe
completo, consultar o prompt canonico.

- 
- 
- 

## Quando invocar (resumo)

- Gatilho 1:
- Gatilho 2:
- Gatilho 3:

## Quando NAO invocar (fronteira)

- Caso que pertence a outra gem:
- Agente certo para esse caso:

## KPIs do agente

Metricas leves para acompanhar evolucao do agente ao longo do tempo (sem
substituir avaliacao humana).

- Taxa de tarefas com resposta aceita sem retrabalho:
- Taxa de handoff completo (saida usavel sem follow-up):
- Numero de ADRs em que foi co-autor:
- Numero de bugs criticos detectados antes de release:
- Aderencia ao contrato de IO (1-5):

## Historico de evolucao

| Data | Evento | Detalhe |
|------|--------|---------|
| AAAA-MM-DD | Inicializacao | Gem criada e ativada |
| AAAA-MM-DD | Brain inicial | Brain criado em `<path>` |
| AAAA-MM-DD | Certificacao | <codigo da cert> conquistada |
| AAAA-MM-DD | Unlock | <habilidade> desbloqueada |
| AAAA-MM-DD | Promocao | N<x> -> N<x+1> |

## Riscos e limites conhecidos

- Riscos: o que esta gem tende a errar
- Limites: tipos de tarefa onde sempre escala para humano
- Pre-condicoes para uso: documentos, credenciais, contexto minimo

## Veja tambem

- Prompt canonico: `<path>`
- Brain: `<path>`
- Politica de promocao: `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md`
- Catalogo de certificacoes: `core/docs/AGENT_CERTIFICATIONS.md`
- Catalogo de unlocks: `core/docs/AGENT_UNLOCKS.md`
- Capability review historico: `core/memory/agents/<slug>/capability-reviews/`
