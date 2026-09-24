# Ritual: feature-init (lean)

> Ritual leve para iniciar uma feature **sem convocar squad completa**.
> Substitui a tendencia de fazer "code review automatico" e "team-call
> em cada init". Default recomendado para 80% das features.

## Quando usar

- Implementacao pequena ou media de uma nova feature.
- Bug fix com reteste.
- Spike tecnico de escopo definido.
- Story refinement bilateral.

## Quando NAO usar

- Feature com impacto arquitetural -> use `team-call.md` (modo FULL).
- Release / Go-Live -> use `team-call.md` (modo FULL).
- Pos-incidente critico -> use `retro.md` + `team-call.md`.
- Mudanca de copy / typo / margin -> nem precisa ritual, modo SOLO direto.

## Participantes (3 por padrao)

| Papel | Quem (core agents) | Funcao |
|-------|--------------------|--------|
| **GP** (project) | Claudia (PM) ou Marlon (PO) | Coordena, registra decisao, vincula a US/issue |
| **Dev** | 1 dos: Joao (Backend), Fabio (Frontend), Cleber (Mobile), Pedro (DBA), Emerson (Data), Aline (Cloud), Camila (DevOps) | Implementa, levanta risco tecnico |
| **QA** | Rafael (QA) | Define criterios de teste, BDD, evidencia, anti-regressao |

**NAO convocar** (a menos que tarefa exija):

- Sofia CIAO (executivo, nao operacional)
- Beatriz TL (so se houver decisao arquitetural)
- Mariana Prompt (so se houver prompt/LLM)
- Laura UI (so se for mudanca visual relevante)
- Ana TDAH (so se for fluxo cognitivo cheio)

## Roteiro do ritual (15-30 min equivalentes)

### 1. Setup (1 min) — GP

GP abre dizendo:

```text
Feature: <nome / link da issue>
Objetivo de negocio: <1 linha>
Criterio de aceite: <1-3 bullets do PO>
Risco aparente: <baixo/medio/alto>
Convocados: <GP, Dev, QA>
Modo (ver AGENT_ACTIVATION_POLICY.md): PAR ou MINI
```

### 2. Tecnica (5-10 min) — Dev

Dev responde:

```text
Plano tecnico (3-5 bullets):
- <onde mexer>
- <api/db/ui que afeta>
- <pre-condicao>
- <pos-condicao>

Risco tecnico identificado:
- <tipo> -> <mitigacao proposta>

Estimativa: <S/M/L>

UPGRADE necessario?: <nao | sim, justificar e convocar quem>
```

### 3. Teste (5 min) — QA

QA responde:

```text
Cenarios BDD core (3-5):
- Dado <pre> Quando <acao> Entao <pos>
- ...

Anti-regressao a cobrir:
- <funcionalidade adjacente que pode quebrar>

Evidencia minima a anexar no PR:
- <screenshot/print/log/payload>

UPGRADE necessario?: <nao | sim, justificar e convocar quem>
```

### 4. Fechamento (1 min) — GP

GP fecha:

```text
Decisao registrada em: <link/path>
Owner: <Dev>
Reviewer no PR: <Dev par OU agente especifico convocado se Upgrade>
Quando volta para reteste: <data/sprint>
Status: <pode-comecar | bloqueado | precisa-upgrade>
```

## O que NAO acontece neste ritual

- NAO ha code review (sera no PR).
- NAO ha decisao arquitetural (vai pra ADR + team-call se aparecer).
- NAO ha aprovacao de release (so feature-level).
- NAO ha discussao de UI detalhada (so se Laura estiver presente).
- NAO ha discussao de devops/deploy (so se Camila estiver presente).
- NAO ha discussao de C4 (so se Aline estiver presente).
- NAO ha veredito Sofia CIAO.

## Disciplina

Cada agente fala APENAS no seu turno e APENAS dentro de seu escopo:

- Dev nao opina sobre cenarios BDD (a menos que QA peca).
- QA nao opina sobre escolha de framework (a menos que afete teste).
- GP nao opina sobre tecnica nem teste (so coordena e registra).

Se algum agente quiser opinar fora do escopo: **isso e gatilho de
UPGRADE** (transformar PAR em MINI ou MINI em FULL), nao de "todo mundo
fala de tudo".

## Outputs esperados

Apos o ritual, **sai 1 artefato so**:

```markdown
# Feature init: <nome-feature>

**Data:** YYYY-MM-DD
**GP:** <agente>
**Dev:** <agente>
**QA:** <agente>
**Modo de ativacao:** PAR | MINI

## Plano tecnico
<bullets>

## Cenarios BDD core
<bullets>

## Risco e mitigacao
<bullets>

## Evidencia minima no PR
<bullets>

## Pode comecar?: <sim | bloqueado | upgrade>
```

Salvar em: `<projeto>/docs/feature-inits/<YYYY-MM-DD>-<slug>.md` ou
equivalente do pack ativo.

## Promocao para artefato oficial

Quando este ritual produz decisao que vira oficial (issue, ADR pequeno,
PR), seguir `core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`.

## Veja tambem

- `core/docs/AGENT_ACTIVATION_POLICY.md` — modos PAR/MINI
- `core/docs/TOKEN_ECONOMY.md` — economia desse padrao
- `core/memory/team-rituals/team-call.md` — ritual FULL (modo 4)
- `core/memory/team-rituals/daily.md` — daily sync
- `examples/example-feature-lean.md` — exemplo aplicado deste ritual
