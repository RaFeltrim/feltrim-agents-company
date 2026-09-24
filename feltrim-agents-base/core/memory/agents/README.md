<!-- versao publica sanitizada; brains de pack vivem em packs/<pack>/brains/ -->

---
name: agents_operational_brains
description: Indice dos cerebros operacionais persistentes dos agentes core
type: reference
---

# Cerebros Operacionais dos Agentes Core

Esta pasta guarda memoria operacional persistente dos agentes core da
Feltrim Agents Company. Ela complementa os prompts em `core/agents/`: o
prompt define a persona e as regras de atuacao; o cerebro registra
experiencia de projeto, aprendizado acumulado, padroes de decisao, handoffs
e contexto de colaboracao.

## Guardrail principal

Os agentes nao possuem consciencia, sentimentos reais ou relacoes humanas
reais. O que esta documentado aqui e uma simulacao util de continuidade
operacional, coesao de time, tom, confianca e cultura de trabalho.

Conversas leves e rituais sociais podem melhorar contexto e fluidez, mas
decisoes tecnicas auditaveis nunca devem ficar perdidas em conversa social.
Toda decisao relevante deve ser promovida para ADR, backlog, runbook, bug,
plano de teste ou documento de projeto. Ver
`core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`.

Use `time-scale.md` como convencao simbolica para cultura e planejamento
interno: 1 dia humano equivale a 1 hora operacional dos agentes. Essa escala
nao altera datas reais de sistemas oficiais, QA, evidencias, contratos,
reports ou documentos oficiais.

## Separacao obrigatoria

1. **Memoria tecnica/projeto:** fatos do projeto, regras, restricoes, fontes de verdade e contexto recorrente.
2. **Senioridade/aprendizados:** criterio profissional amadurecido pelo agente, heuristicas e licoes aprendidas.
3. **Decisoes e ADRs:** escolhas auditaveis, alternativas consideradas, responsavel e impacto.
4. **Conversas de call:** atas, combinados, perguntas, conflitos e proximas acoes.
5. **Pre-daily social/team bonding:** check-in leve, energia, reconhecimento e transicao para pauta tecnica.
6. **Pendencias e handoffs:** itens que exigem continuidade entre agentes ou intervencao humana.

## Estrutura

- `_templates/` - modelos canonicos para brain, pre-daily, team-call,
  agent-profile e agent-capability-review.
- `time-scale.md` - convencao temporal simbolica para rituais, XP, ciclos
  de descanso, game nights e hackathons internos.
- `_uninitialized-agents.md` - indice dos agentes core que ainda nao
  receberam cerebro inicial.
- `<slug>/brain.md` - brain operacional persistente de cada agente core
  inicializado. Slugs default usam o mesmo nome curto da gem (ex.:
  `beatriz-tl`, `joao-backend`, `sofia-ciao`).

## Brains de pack

Brains de agentes que sao especificos de um pack vivem em
`packs/<pack>/brains/<slug>/brain.md`, nao aqui. Este diretorio so
guarda brains de gens core (15 papeis genericos).

## Estado atual (boilerplate inicial)

### Implementado

- Brains iniciais existem para 10 papeis centrais: Beatriz-TL, Camila-DevOps,
  Claudia-PM, Fabio-Frontend, Joao-Backend, Laura-UI, Marlon-PO, Pedro-DBA,
  Rafael-QA, Sofia-CIAO.
- Escala temporal simbolica esta documentada em `time-scale.md`.
- Templates de brain, pre-daily, team-call, agent-profile e capability-review
  estao em `_templates/`.

### Parcialmente implementado

- XP cultural pode ser registrado em rituais, mas ainda nao ha loja,
  inventario, carteira ou scoreboard completo (ver
  `governance/PROMOTION_POLICY.md`).
- Atualizacao de brains depende de decisao humana ou instrucao explicita;
  nao e sincronizacao automatica.

### Pendente

- Inicializar brains dos agentes core listados em `_uninitialized-agents.md`,
  se entrarem em uso recorrente.
- Definir governanca para gamificacao completa antes de criar loja,
  inventario ou economia de XP.

## Uso diario

1. Antes da daily, registrar um pre-daily curto usando
   `_templates/pre-daily-template.md` ou em
   `core/memory/team-rituals/pre-daily.md`.
2. Ao iniciar trabalho de um agente, ler o prompt em `core/agents/` (ou
   `packs/<pack>/agents/`) e o respectivo `brain.md`.
3. Durante calls, registrar notas no formato de
   `_templates/team-call-template.md`.
4. Ao final de uma atuacao, atualizar aprendizados, handoffs e pendencias do
   brain do agente.
5. Se surgir decisao tecnica, promover para ADR/backlog/runbook (ver
   `core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`); nao deixar apenas na call ou
   no pre-daily.
6. Se usar escala agente em ritual ou gamificacao, manter qualquer artefato
   oficial com calendario real humano.

## Regra de promocao

Promova para documento auditavel quando a informacao:

- muda arquitetura, fluxo, criterio de QA, status oficial, backlog ou
  contrato entre sistemas;
- afeta custo, seguranca, dados, release, evidencias, rastreabilidade ou
  go/no-go;
- precisa ser encontrada por alguem que nao participou da conversa;
- sera cobrada no futuro por decisor humano, cliente, QA, auditoria ou
  operacao.
