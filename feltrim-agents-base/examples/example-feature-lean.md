# Exemplo: feature lean (modo PAR / MINI)

> **Default recomendado para 80% das features.** Convoca apenas os
> agentes que movem a feature, evita code review automatico e mantem
> custo de token sob controle.
>
> Baseado em feedback real (Maio/2026) de uso em ambiente de
> desenvolvimento com cobranca por token.

## Cenario

Voce vai implementar uma feature pequena/media, ou um bug fix, ou um
spike tecnico. **Nao quer** convocar a squad completa, **nao quer**
code review automatico antes de codar, **quer** apenas alinhamento
minimo PO/Dev/QA.

## Quando usar este exemplo

- Feature small ou medium (story de 1-5 dias).
- Bug fix com reteste.
- Spike tecnico de escopo definido.
- Story refinement bilateral.
- Implementacao com decisao clara e reversivel.

## Quando NAO usar

Para estes casos, ver `example-spawn-team-meeting.md` (modo FULL):

- Release / Go-Live.
- Mudanca arquitetural relevante.
- Pos-incidente critico.
- Hackathon / Kickoff.
- Proposta executiva.

## Pre-requisitos

- Cursor / Claude Code / Codex / Gemini IDE com este repo aberto.
- Leitura no contexto:
  - `core/CLAUDE.md` (boot do framework)
  - `core/docs/AGENT_ACTIVATION_POLICY.md` (modos)
  - `core/docs/TOKEN_ECONOMY.md` (economia)
  - `core/docs/SQUAD_INDEX.md` (mapa de invocacao)
  - `core/memory/team-rituals/feature-init.md` (ritual aplicado aqui)
- Issue / US descrita em `<caminho/issue.md>`.

## Prompt

```text
Quero rodar feature-init lean para a US/issue em
`<caminho/issue.md>`.

Por favor:

1. Ler `core/CLAUDE.md` minimalista (so o boot, sem carregar todas as
   gens).
2. Ler `core/docs/SQUAD_INDEX.md` secao "Mapa de invocacao".
3. Ler a US/issue em `<caminho/issue.md>`.
4. Identificar **apenas 3 agentes**:
   - GP (Claudia OU Marlon) - coordena
   - Dev (Joao OU Fabio OU Pedro OU Emerson OU Aline OU Camila OU
     Cleber) - implementa
   - QA (Rafael) - valida
5. NAO convocar: Sofia CIAO, Beatriz TL, Mariana Prompt, Laura UI,
   Ana TDAH (a menos que a tarefa exija e voce justifique).
6. Carregar APENAS as 3 gens selecionadas (`core/agents/gem_<slug>.md`).
7. Rodar o ritual em `core/memory/team-rituals/feature-init.md`:
   - GP: setup (1 min equivalente)
   - Dev: plano tecnico + risco + UPGRADE? (5-10 min)
   - QA: cenarios BDD + anti-regressao + evidencia + UPGRADE? (5 min)
   - GP: fechamento + status (1 min)
8. Output: 1 artefato unico no formato definido no ritual.

Premissas:
- Cada agente fala APENAS no seu turno e APENAS dentro do escopo.
- Se algum agente pedir UPGRADE (justificado), parar e perguntar ao
  decisor humano se aprova convocar reforco.
- Se algum agente disser que "minha participacao nao agrega", aceitar
  o downgrade e seguir.
- NAO fazer code review automatico (sera no PR, nao agora).
- NAO discutir arquitetura (sera em team-call se aparecer).

Atencao a guardrails:
- `core/docs/TOKEN_ECONOMY.md` (7 regras + anti-patterns)
- `governance/RITUALS_GUARDRAILS.md`
- `governance/SECURITY_AND_PRIVACY.md`
```

## O que esperar

Output unico, curto, acionavel:

```markdown
# Feature init: <slug>

**Data:** YYYY-MM-DD
**GP:** <Claudia | Marlon>
**Dev:** <agente backend/frontend/etc>
**QA:** Rafael
**Modo de ativacao:** PAR | MINI

## Plano tecnico (Dev)
- Onde mexer: <paths>
- API/DB/UI: <impacto>
- Pre-condicao: <estado inicial>
- Pos-condicao: <estado final>

## Risco tecnico (Dev)
- <tipo>: <mitigacao>

## Cenarios BDD (QA)
- Dado <pre> Quando <acao> Entao <pos>
- ...

## Anti-regressao a cobrir (QA)
- <funcionalidade adjacente>

## Evidencia minima no PR (QA)
- <screenshot | log | payload | curl>

## Status (GP)
- Pode comecar: <sim | bloqueado | precisa upgrade>
- Owner: <Dev>
- Reviewer no PR: <Dev par OU agente Upgrade>
- Reteste: <data/sprint>
```

**Tamanho esperado do output: 20-40 linhas. Tokens: 5k-20k.**

## Anti-padroes para nao cometer

- **NAO** convocar 5+ agentes "por garantia".
- **NAO** carregar todas as 15 gens em uma sessao de feature pequena.
- **NAO** pedir Sofia CIAO pra opinar em copy / margin / decisao tatica.
- **NAO** rodar code review automatico antes de o codigo existir.
- **NAO** rodar team-call sem trigger valido (ver
  `AGENT_ACTIVATION_POLICY.md` secao "FULL").
- **NAO** repetir convocacao identica entre features parecidas — se
  acontecer 3x, transformar em script ou gem dedicada.

## Variantes

### Variante 1: feature solo (so 1 agente)

Para typo, copy, lint, margin: pular o ritual de 3 agentes. So:

```text
Tarefa: <descricao curta>
Agente: <um dos 15, escolhido por escopo>
Output esperado: <1 linha do que esperar>
```

### Variante 2: feature MINI (4-5 agentes)

Quando a feature toca multi-area (ex: frontend + backend + DB):

Adicionar **so** os agentes adicionais necessarios:

- Frontend + Backend: Fabio + Joao + Pedro/Emerson + Rafael + Claudia.
- UI relevante: + Laura.
- Performance critica: + Beatriz.

Manter regra: nao convocar quem nao move a feature.

### Variante 3: par tecnico (so 2 agentes)

Para spike tecnico ou decisao bilateral:

- Joao + Pedro (decisao API/schema).
- Beatriz + Aline (decisao framework/cloud).
- Mariana + Rafael (decisao prompt/test).

## Veja tambem

- `core/docs/AGENT_ACTIVATION_POLICY.md` - 4 modos
- `core/docs/TOKEN_ECONOMY.md` - economia + anti-patterns
- `core/memory/team-rituals/feature-init.md` - ritual base aplicado
- `core/docs/SQUAD_INDEX.md` - mapa atualizado de invocacao
- `examples/example-spawn-team-meeting.md` - quando FULL e justificado
- `examples/example-model-benchmark.md` - comparar modelos para escolher por modo
