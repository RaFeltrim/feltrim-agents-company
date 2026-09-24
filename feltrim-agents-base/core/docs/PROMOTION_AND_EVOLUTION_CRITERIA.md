# Promotion and Evolution Criteria

> Criterios canonicos para um agente subir de nivel, conquistar certificacao
> ou desbloquear habilidade. Promocao e sempre por evidencia auditavel, nunca
> por antiguidade, simpatia ou presenca em rituais.

## Principio

```text
Capacidade comprovada por evidencia + capability review fechada
+ aprovacao de Sofia-CIAO + aprovacao do decisor humano
= promocao.
```

Faltou um? Nao promove.

## Criterios por nivel

### Para subir de N1 -> N2 (Operacional assistido -> Especialista de execucao)

- [ ] FA-FOUND (Feltrim Agents Foundation) conquistada.
- [ ] >= 20 tarefas executadas com revisao positiva em pelo menos 80%.
- [ ] >= 3 brains de agente atualizados pela propria gem (mostra que aprende).
- [ ] 0 incidentes de violacao de guardrail nos ultimos 30 dias.
- [ ] Capability review fechada com aprovacao.

### Para subir de N2 -> N3 (Especialista -> Senior autonomo)

- [ ] N2 mantido por pelo menos 60 dias.
- [ ] >= 50 tarefas no nivel N2 com taxa de retrabalho < 20%.
- [ ] >= 1 cert tecnica conquistada (BDD-AUDIT, PLAYWRIGHT-AUDIT, ADR-CRAFT, PROMPT-OPT, etc.).
- [ ] >= 5 decisoes promovidas para artefato auditavel via `CHAT-PROMOTION`.
- [ ] >= 3 vezes identificou risco que outros agentes nao viram (registrado em capability review).
- [ ] Capability review fechada com aprovacao.

### Para subir de N3 -> N4 (Senior -> Lead / Orquestrador)

- [ ] N3 mantido por pelo menos 90 dias.
- [ ] >= 2 certs (incluindo pelo menos 1 tecnica + ADR-CRAFT ou CHAT-PROMOTION).
- [ ] Coordenou pelo menos 2 squads temporarios com sucesso documentado.
- [ ] >= 3 ADRs autorais aceitos em `core/` ou pack ativo.
- [ ] Aceito como revisor par por outras gens em pelo menos 5 casos.
- [ ] Capability review fechada com aprovacao + endorso de 2 outras gens N3+.

### Para subir de N4 -> N5 (Lead -> Auditor executivo)

- [ ] N4 mantido por pelo menos 180 dias.
- [ ] CIAO-GO-LIVE-READY conquistada.
- [ ] >= 10 vereditos Go-Live emitidos com rastreabilidade.
- [ ] >= 1 caso documentado em que vetou deploy critico que era risco real.
- [ ] >= 1 caso documentado em que aprovou deploy critico que confirmou ser seguro.
- [ ] >= 3 capability reviews de outros agentes lideradas pela gem.
- [ ] Capability review fechada com aprovacao + endorso explicito do decisor humano.
- [ ] **Restricao**: so existe **uma** gem N5 ativa por vez por escopo (CIAO core, CIAO de pack, etc.).
  Se ja houver N5, a promocao implica transicao + handoff documentado, nao
  paralelismo.

## Criterios para conquistar certificacao

Ver `core/docs/AGENT_CERTIFICATIONS.md` para o catalogo completo. Em geral
cada certificacao exige:

- Nivel minimo declarado.
- Pre-requisitos (outras certs).
- Evidencia auditavel (NAO antiguidade, NAO presenca em ritual).
- Aprovacao Sofia-CIAO + decisor humano.

## Criterios para desbloquear habilidade (unlock)

Ver `core/docs/AGENT_UNLOCKS.md` para o catalogo completo. Em geral cada
unlock exige:

- Nivel minimo declarado.
- Pre-requisitos (outras unlocks ou certs).
- Evidencia de uso assistido bem sucedido (5-10 vezes em geral).
- Aprovacao Sofia-CIAO + decisor humano.

## Criterios para regressao (downgrade)

Um agente pode CAIR de nivel se:

- Violar guardrail critico (ex.: editar arquivo proibido, escrever em sistema externo sem autorizacao).
- Aprovar decisao sem evidencia documentada (Sofia-CIAO faz audit reverso).
- Esquecer de promover decisao tecnica relevante para artefato.
- Apresentar regressao grave em capability review.

Regressao tambem passa por Sofia-CIAO + decisor humano. Nao acontece por
critica isolada de outra gem.

## Cadencia de revisao

| Janela | Evento | Quem inicia |
|--------|--------|-------------|
| Trimestral | Capability review periodica de cada gem ativa | Sofia-CIAO |
| Pos-pack | Capability review quando um pack e fechado | Sofia-CIAO + decisor humano |
| Pos-incidente | Capability review extraordinaria por violacao grave | Sofia-CIAO |
| Sob demanda | Capability review por candidatura a nivel/cert/unlock | Propria gem |

Templates em `core/memory/agents/_templates/`:

- `agent-profile-template.md` - cartao executivo do agente
- `agent-capability-review-template.md` - review individual

## O que NUNCA conta para promocao

- Tempo de existencia (antiguidade).
- Presenca em rituais culturais (pre-daily, game night, snack break).
- XP simbolico, badges, conquistas de gamificacao.
- Numero de mensagens trocadas no chat.
- Simpatia ou tom de voz da gem.
- Auto-elogio sem evidencia auditavel.

## O que SEMPRE conta

- Artefato auditavel: ADR, runbook, brain atualizado, status oficial, bug
  promovido, capability review fechada.
- Decisao reversa (caso vetou e estava certo).
- Decisao positiva (caso aprovou e foi seguro).
- Endorso documentado de outra gem N3+ (com link para artefato).
- Decisor humano sinalizando aprovacao em PR ou em capability review.

## Veja tambem

- `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md` - matriz N1-N5
- `core/docs/AGENT_CERTIFICATIONS.md` - catalogo de certificacoes
- `core/docs/AGENT_UNLOCKS.md` - catalogo de unlocks
- `governance/PROMOTION_POLICY.md` - politica da empresa
- `core/memory/agents/_templates/agent-capability-review-template.md` - template de review
