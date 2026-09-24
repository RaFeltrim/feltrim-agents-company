<!-- versao publica sanitizada; indice generico de pack ou projeto -->

# INDEX - Esquadrao do Projeto

> **Ultima atualizacao:** {DATA}
> **Projeto:** {NOME_DO_PROJETO}
> **Dominio:** {DOMINIO}
> **Decisor humano:** {DECISOR_HUMANO}

Este documento mapeia o esquadrao de agentes deste pack/projeto. Cada persona
referencia a gem canonica em `core/agents/` (ou versao especializada em
`packs/<pack>/agents/`).

> **Como usar:**
> 1. Copie esta pasta para o pack/projeto.
> 2. Substitua todos os `{PLACEHOLDERS}` pelos dados do projeto.
> 3. Apague linhas de gens que nao se aplicam (ex.: sem mobile -> apague Cleber).
> 4. Adicione gens proprias do pack abaixo da secao "Gens proprias do pack".

---

## CIAO (Chief Intelligence & Auditing Officer)

### Sofia - CIAO - mente estrategica e gate de Go-Live
- `core/agents/gem_sofia_ciao.md`

---

## GP (Gestao e Produto)

### Marlon - Product Owner - business value, stories, criterios
- `core/agents/gem_marlon_po.md`

### Claudia - Project Manager - sprints, blockers, critical path
- `core/agents/gem_claudia_pm.md`

---

## DEVs (Desenvolvimento e Arquitetura)

### Beatriz - Tech Lead - arquitetura de solucao, ADRs, trade-offs
- `core/agents/gem_beatriz_tl.md`

### Aline - Cloud Architect - C4, topologia, custo, DR
- `core/agents/gem_aline_cloud.md`

### Camila - DevOps - CI/CD, IaC, secrets
- `core/agents/gem_camila_devops.md`

### Joao - Backend - APIs, RPA, BullMQ, integracoes
- `core/agents/gem_joao_backend.md`

### Fabio - Frontend React - componentes, estado, bundle
- `core/agents/gem_fabio_frontend.md`

### Cleber - Mobile - mobile-first, PWA, touch ergonomia
- `core/agents/gem_cleber_mobile.md`

### Laura - UI/UX - design system, tokens, microinteracoes
- `core/agents/gem_laura_ui.md`

### Ana - TDAH UX Ally - acessibilidade neurodivergente
- `core/agents/gem_ana_tdah.md`

### Mariana - Prompt Engineer - prompts, RAG, structured output
- `core/agents/gem_mariana_prompt.md`

---

## DB (Database e Data Engineering)

### Emerson - Supabase / Postgres Engineer - migrations, RLS, Edge Functions
- `core/agents/gem_emerson_supabase.md`

### Pedro - DBA & Analytics - query tuning, indexes, materialized views
- `core/agents/gem_pedro_dba.md`

---

## QA (Qualidade)

### Rafael - QA SDET - BDD, Playwright E2E, smoke, regressao
- `core/agents/gem_rafael_qa.md`

---

## Gens proprias do pack

Adicione aqui as gens especializadas do pack, no formato:

- `<Nome> - <Funcao>` - `packs/<pack>/agents/gem_<pack>_<funcao>.md`

Exemplos genericos:

- `packs/<pack>/agents/gem_<pack>_orchestrator.md`
- `packs/<pack>/agents/gem_<pack>_runner.md`
- `packs/<pack>/agents/gem_<pack>_evidence.md`

## Protocolos universais

Toda gem deste pack carrega tambem:

- `core/protocols/AGENT_RUNTIME_WRAPPER.md` - ordem de composicao da instrucao
- `core/protocols/AGENT_IO_CONTRACT.md` - request packet + response envelope
- `core/protocols/HANDOFF_PROTOCOL.md` - passagem de bastao
- `core/protocols/MEMORY_AND_RAG_POLICY.md` - quando gravar / recuperar
- `core/protocols/EVALS_AND_MONITORING.md` - scorecard e gates
- `core/protocols/ORCHESTRATION_POLICY.md` - solo / paired / squad
- `core/protocols/DELIVERY_AND_PRODUCT_SURFACES.md` - human-readable / machine-readable / execution-ready
- `core/protocols/MULTIMODAL_EXTENSION.md` - apenas se houver imagem/audio/video
