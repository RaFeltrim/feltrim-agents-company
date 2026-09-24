# Changelog

Todas as mudancas notaveis neste projeto serao documentadas aqui.

O formato segue [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) e
este projeto adere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Adicionado

- **Shift-left pre-commit hooks** que espelham 1:1 os 4 jobs do CI:
  - `.pre-commit-config.yaml` - config principal (markdownlint, higiene de
    arquivos, flag-words, structure, link-check opt-in).
  - `scripts/check-flag-words.sh` + `.ps1` - sanitizacao local (paths
    absolutos, .env real, secrets, email policy).
  - `scripts/check-structure.sh` - arquivos e diretorios obrigatorios + count
    minimo de gens (>=15) e protocolos (>=8).
  - `scripts/check-links.sh` - markdown link check (manual stage, opt-in).
  - `scripts/README.md` - inventario e instrucoes.
- Secao "Checagem local antes do push (shift-left)" reescrita no
  `CONTRIBUTING.md` com setup e uso diario.

### Em desenvolvimento

- Calibracao da `AGENT_ACTIVATION_POLICY.md` apos 1 mes de uso real.
- Decisao de licenca final (proprietaria / open-source / dual).
- Auditoria de `core/integrations/` para split core vs pack.

## [0.1.0] - 2026-05-16

Primeira release publica do boilerplate. MVP completo.

### Adicionado

#### `core/` - generico, reutilizavel

- 15 gens canonicas sanitizadas (`core/agents/gem_*.md`): Sofia CIAO,
  Beatriz TL, Marlon PO, Claudia PM, Aline Cloud, Camila DevOps, Joao
  Backend, Fabio Frontend, Cleber Mobile, Laura UI, Ana TDAH UX, Mariana
  Prompt, Emerson Supabase, Pedro DBA, Rafael QA.
- 3 templates (`core/agents/_template/`): gem-skeleton, INDEX_TEMPLATE,
  SETUP_TEMPLATE.
- 8 protocolos sistemicos (`core/protocols/`): AGENT_RUNTIME_WRAPPER,
  AGENT_IO_CONTRACT, HANDOFF_PROTOCOL, MEMORY_AND_RAG_POLICY,
  EVALS_AND_MONITORING, ORCHESTRATION_POLICY, DELIVERY_AND_PRODUCT_SURFACES,
  MULTIMODAL_EXTENSION.
- 13 docs canonicos (`core/docs/`): ARQUITETURA, ONBOARDING, SQUAD_INDEX
  v2.2, AGENT_LEVELS_AND_CERTIFICATIONS, AGENT_CERTIFICATIONS,
  AGENT_UNLOCKS, PROMOTION_AND_EVOLUTION_CRITERIA,
  CHAT_TO_ARTIFACT_GOVERNANCE, OPERATING_MODEL, AGENT_ACTIVATION_POLICY,
  TOKEN_ECONOMY, plus subpastas adr/, manifesto/, strategy/, templates/.
- Memoria operacional (`core/memory/`): MEMORY.md index, 10 brains
  inicializados, 5 templates, time-scale.md, 12 rituais (pre-daily,
  flash-talks, game-nights, monthly-hackathons, feature-init,
  team-call-notes-template, snack-break-notes-template,
  game-night-notes-template, hackathon-idea-template,
  hackathon-scorecard-template, prototype-to-product-checklist).
- Esqueletos de skills, integrations, scripts.

#### `governance/` - politicas da empresa

- COMPANY_CHARTER, AGENT_HIERARCHY, RITUALS_GUARDRAILS, PROMOTION_POLICY,
  CERTIFICATION_POLICY, SECURITY_AND_PRIVACY + README.

#### `packs/` - exemplos publicos

- `cms-gherkin/` (BDD/Gherkin completo com 4 prompts por modelo LLM, 2
  ferramentas Python, 6 docs operacionais, exemplos PROJETO-EXEMPLO).
- `us-avaliator/` (proposta sanitizada + 14 relatorios de revisao
  multi-perspectiva).
- `_template-pack/` (esqueleto para criar novos packs).

#### `examples/` - exemplos de uso

- example-feature-lean (modo PAR/MINI, default 80% das features).
- example-spawn-team-meeting (modo FULL com aviso de custo).
- example-pack-init (passo a passo de criar pack novo).
- example-model-benchmark (benchmark de modelos novos).

#### `.specify/` - Spec Kit

- Constitution generica com 5 principios.

#### Documentacao publica de projeto

- README.md hero com badges, Mermaid de hierarquia, quick start e
  comparacao vs alternativas.
- CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, CHANGELOG.md.
- docs/GETTING_STARTED.md (5 minutos), docs/USE_CASES.md (5 casos),
  docs/COMPARISON.md (vs LangChain/CrewAI/AutoGen/BMAD).
- `.github/ISSUE_TEMPLATE/` (bug, feature, agent proposal, question).
- `.github/PULL_REQUEST_TEMPLATE.md`.
- `.github/workflows/ci.yml` (markdown lint + flag word grep + link check).

### Politica de ativacao (Maio/2026 feedback)

Resposta a feedback de uso real que apontou consumo excessivo de token
quando squad atua "constante em todo projeto":

- 4 modos definidos: SOLO / PAR / MINI / FULL.
- Cada uma das 15 gens com secao "Trigger anti-patterns (quando NAO
  invocar)".
- SQUAD_INDEX v2.2 com coluna "Quando NAO invocar" + modo default por
  trigger.
- Ritual lean `feature-init.md` para defaults PAR/MINI.
- Severidades T1/T2/T3 para incidente de token em
  `governance/SECURITY_AND_PRIVACY.md`.

### Sanitizacao

- Zero referencias a clientes (CVP, marketplaces, etc.) em arquivos
  publicos.
- Zero paths absolutos de maquina local.
- Headers HTML de auditoria reescritos em estilo publico.
- Lista de palavras-bandeira em `governance/SECURITY_AND_PRIVACY.md`
  convertida em template generico (instalacoes mantem lista propria fora
  do repo).
- Identidade do commit usa `RaFeltrim@users.noreply.github.com` para nao
  vazar email corporativo.

### Decisoes pendentes registradas

7 itens em `DECISIONS_PENDING.md` para revisao humana futura.

---

## Convencao de versionamento

- `MAJOR` - mudanca incompativel em protocolo, hierarquia, ou contrato de
  gem.
- `MINOR` - nova gem, novo protocolo, novo pack, novo ritual.
- `PATCH` - correcao de typo, doc, link, formatacao.

## Convencao de secoes

- `Adicionado` - novo conteudo.
- `Alterado` - mudanca em conteudo existente.
- `Depreciado` - sera removido em release futura.
- `Removido` - removido nesta release.
- `Corrigido` - bug fix.
- `Sec` - sanitizacao, leak fix, politica de seguranca.

[Unreleased]: https://github.com/RaFeltrim/feltrim-agents-base/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/RaFeltrim/feltrim-agents-base/releases/tag/v0.1.0
