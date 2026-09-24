# Agent Certifications - Catalogo

> Catalogo das certificacoes internas do Feltrim Agents Framework,
> generalizadas para nao-pack-especificas.

Certificacoes especificas de pack vivem em
`packs/<pack>/docs/CERTIFICATIONS.md`. Aqui no `core/` so estao as
certificacoes universais aplicaveis a qualquer pack.

## Formato canonico de certificacao

```markdown
### <CODIGO> - <Nome longo>

**Categoria:** Foundation | Tecnica | Governanca | Pack-specific
**Nivel minimo:** N<x>
**Pre-requisitos:** <outras certs ou conquistas exigidas>
**Validade:** Permanente | Re-certificar a cada <N meses> | Quando framework mudar

**O que prova:**
- Conhecimento de <area>
- Capacidade de <atividade>
- Aderencia a <padrao>

**Evidencia exigida:**
- Artefato auditavel 1
- Artefato auditavel 2

**Agentes elegiveis:** <lista ou "todos">
**Emissor:** Sofia CIAO + decisor humano
**Guardrails:** <o que ainda nao autoriza fazer>
```

## Certificacoes Foundation (toda gem deve conquistar)

### FA-FOUND - Feltrim Agents Foundation

**Categoria:** Foundation
**Nivel minimo:** N1
**Pre-requisitos:** nenhum (e a primeira)
**Validade:** Permanente, mas re-certificar se manifesto FF v3 -> FF v4

**O que prova:**

- Conhece hierarquia da empresa Feltrim Agents (CEO -> CIAO -> Squads)
- Conhece os 8 protocolos canonicos (`core/protocols/`)
- Conhece o sistema de niveis N1-N5
- Conhece a separacao entre cultura simbolica e governanca real
- Conhece o boot sequence padrao (`core/CLAUDE.md`)
- Conhece a regra de Chat -> Artefato auditavel

**Evidencia exigida:**

- Resposta a quiz de 10 perguntas sobre os 8 protocolos (>= 8/10 acertos),
  registrada em `core/memory/agents/<slug>/capability-reviews/`.
- Uma execucao real de tarefa onde a gem aplicou ao menos 3 dos 8 protocolos
  de forma explicita.

**Agentes elegiveis:** todas as 15 gens core e toda gem de pack.
**Emissor:** Sofia CIAO + decisor humano.

---

## Certificacoes Tecnicas (especialidade)

### BDD-AUDIT - BDD Writing Audit-Grade

**Categoria:** Tecnica
**Nivel minimo:** N3
**Pre-requisitos:** FA-FOUND

**O que prova:**

- Escreve cenarios Gherkin com Given/When/Then disciplinados
- Sabe separar caminho feliz, caminho de falha de regra, caminho de
  bloqueio
- Sabe quando NAO usar BDD (testes de baixo nivel, unit tests)
- Conhece anti-padroes (cenarios longos, sub-cenarios, declarativo demais)

**Evidencia exigida:**

- Conjunto de >= 10 cenarios BDD escritos pela gem em projeto real, com
  cobertura de caminho feliz + falha + bloqueio.
- Revisao positiva de Rafael-QA ou Mariana-Prompt.

**Agentes elegiveis:** Rafael-QA, Marlon-PO, gens de QA em packs.
**Emissor:** Sofia CIAO + Rafael-QA (revisor par) + decisor humano.

---

### PLAYWRIGHT-AUDIT - Playwright E2E Audit-Grade

**Categoria:** Tecnica
**Nivel minimo:** N2
**Pre-requisitos:** FA-FOUND

**O que prova:**

- Implementa testes Playwright deterministicos (sem flakiness)
- Diferencia falha de script de falha funcional
- Usa contexto de navegador isolado por execucao
- Implementa evidencia (screenshot, video, trace) de forma reproduzivel
- Trata anti-bot, stealth, CDP quando necessario

**Evidencia exigida:**

- >= 5 suites E2E em producao com taxa de flakiness < 2% por 4 semanas.
- 1 caso documentado em que diferenciou falha de script de bug funcional.

**Agentes elegiveis:** Rafael-QA, Joao-Backend, gens de pack que rodam Playwright.
**Emissor:** Sofia CIAO + Rafael-QA + decisor humano.

---

### ADR-CRAFT - ADR Architecture Decision Record

**Categoria:** Tecnica
**Nivel minimo:** N3
**Pre-requisitos:** FA-FOUND

**O que prova:**

- Escreve ADR claro, com contexto, decisao, alternativas, consequencias e
  revisao prevista.
- Sabe quando decisao requer ADR (irreversivel, multi-sprint, multi-pack).
- Identifica dependencia entre ADRs.

**Evidencia exigida:**

- Pelo menos 3 ADRs autorais em `core/docs/adr/` ou `packs/<pack>/adr/`,
  todos aceitos.
- 1 ADR superseding outro (mostra evolucao de pensamento).

**Agentes elegiveis:** Beatriz-TL, Aline-Cloud, Sofia-CIAO, qualquer N3+.
**Emissor:** Sofia CIAO + decisor humano.

---

### PROMPT-OPT - Prompt Optimization Standard

**Categoria:** Tecnica
**Nivel minimo:** N3
**Pre-requisitos:** FA-FOUND

**O que prova:**

- Mede custo de tokens antes/depois de mudancas de prompt
- Implementa semantic caching corretamente
- Sabe quando usar JSON schema enforcement
- Anti-injection: sanitiza inputs externos antes de incluir no prompt
- Compara fielmente entre providers (Claude, GPT, Gemini, open source)

**Evidencia exigida:**

- 3 benchmarks documentados (mesma tarefa, mesmo input, prompts diferentes,
  custo + qualidade medidos).
- 1 caso de prompt sob injection identificado e corrigido.

**Agentes elegiveis:** Mariana-Prompt, qualquer N3+ que mexa em prompts.
**Emissor:** Sofia CIAO + Mariana-Prompt + decisor humano.

---

## Certificacoes de Governanca

### CIAO-GO-LIVE-READY - CIAO Go-Live Audit

**Categoria:** Governanca
**Nivel minimo:** N4
**Pre-requisitos:** FA-FOUND, ADR-CRAFT

**O que prova:**

- Aplica as 6 condicoes de Go-Live do FF (ver `core/agents/gem_sofia_ciao.md`)
- Diferencia risco aceitavel de risco bloqueante
- Documenta riscos residuais com plano de monitoramento
- Classifica corretamente GO / NO-GO / CONDICIONADO
- Sabe revogar aprovacao se condicao nao for cumprida

**Evidencia exigida:**

- >= 5 vereditos Go-Live emitidos com rastreabilidade (decisao + condicoes +
  resultado real do deploy).
- 1 caso documentado de revogacao de aprovacao por nao-cumprimento de
  condicao.

**Agentes elegiveis:** Sofia-CIAO unicamente. Outros agentes podem fazer
recomendacao de Go/No-Go, mas a certificacao e exclusiva da CIAO.
**Emissor:** Decisor humano (esta e a unica cert que CIAO nao emite para si mesma).

---

### CHAT-PROMOTION - Chat to Artifact Promotion

**Categoria:** Governanca
**Nivel minimo:** N2
**Pre-requisitos:** FA-FOUND

**O que prova:**

- Reconhece quando uma conversa social/ritual contem decisao tecnica
- Promove decisao para ADR/backlog/runbook/bug/status sem mistura
- Atualiza brain do agente responsavel
- Atualiza artefato auditavel com link de origem

**Evidencia exigida:**

- >= 5 promocoes documentadas em projeto real (origem chat -> destino auditavel),
  com link auditavel.

**Agentes elegiveis:** todos.
**Emissor:** Sofia CIAO + decisor humano.

Detalhes em `core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`.

---

## Certificacoes de pack (referencia)

Certificacoes especializadas vivem em `packs/<pack>/docs/CERTIFICATIONS.md`.
Exemplos genericos de codigos possiveis:

- `<PACK>-FOUND` - Foundation do pack (conhece operating contract)
- `<PACK>-AUDIT` - capaz de auditar artefatos do pack sem retrabalho
- `EVIDENCE-PDF` - Evidence PDF Standard (gera PDF auditavel)
- `BUG-RETEST` - Bug Retest Standard (executa retest sem misturar achados)
- `CMS-BDD-V3` - CMS BDD Padrao V3 (em `packs/cms-gherkin/`)

## Catalogo vivo

Adicione nova certificacao via PR proprio. PR deve:

1. Atualizar este arquivo com o bloco novo.
2. Atualizar `governance/CERTIFICATION_POLICY.md` se a politica de emissao
   precisar mudar.
3. Notificar `core/docs/SQUAD_INDEX.md` para incluir a cert nas linhas dos
   agentes elegiveis.

## Revisao

Certificacoes podem ser revogadas se:

- O agente perdeu a capacidade (regressao grave em capability review).
- O framework FF mudou de versao e a cert foi superada.
- O artefato que serviu de evidencia foi invalidado.

Revogacao tambem requer Sofia CIAO + decisor humano. Ver
`governance/CERTIFICATION_POLICY.md`.
