# Squad Index v2.2

> Roster canonico das gens core do Feltrim Agents Framework, com niveis,
> certificacoes, habilidades desbloqueadas e anti-patterns de
> convocacao. Consolidacao de documentos internos + feedback Maio/2026
> (Agent Activation Policy).
>
> Pack roster especifico vive em `packs/<pack>/docs/SQUAD_INDEX.md`.

## Convencao de leitura

- **Nivel** segue `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md`.
- **Certificacoes** listadas pelos codigos curtos. Catalogo em
  `core/docs/AGENT_CERTIFICATIONS.md`.
- **Habilidades principais** sao unlocks mais relevantes da gem.
  Catalogo em `core/docs/AGENT_UNLOCKS.md`.
- **Quando invocar** e **Quando NAO invocar** existem em duplicata:
  resumo aqui, detalhado em `core/agents/gem_<slug>.md`. Antes de
  convocar, ler tambem `core/docs/AGENT_ACTIVATION_POLICY.md` para
  definir o modo (SOLO/PAR/MINI/FULL).
- **XP / ritual / cultura nao aparecem aqui** - sao simbolicos e nao sao
  metricas de performance. Ver `governance/RITUALS_GUARDRAILS.md`.

## Roster core (15 gens)

### CIAO (gate executivo)

| Agente | Papel | Nivel | Certs default | Habilidades principais | Quando invocar | Quando NAO invocar |
|--------|-------|-------|---------------|------------------------|----------------|--------------------|
| Sofia | CIAO | N5 | FA-FOUND, ADR-CRAFT, CIAO-GO-LIVE-READY | apply-tech-veto, open-adr, update-squad-index | Antes de deploy / PR critico / decisao de risco / auditoria de seguranca | Copy/typo/margin; bug fix local; feature pequena/media; refactor reversivel; tarefa tatica |

### GP (Gestao e Produto)

| Agente | Papel | Nivel | Certs default | Habilidades principais | Quando invocar | Quando NAO invocar |
|--------|-------|-------|---------------|------------------------|----------------|--------------------|
| Marlon | Product Owner | N3 | FA-FOUND | promote-prototype, organize-monthly-hackathon | Priorizacao backlog, user stories, MoSCoW, WSJF, KPIs | Decisao puramente tecnica; refactor sem mudanca de comportamento; bug fix de baixa criticidade |
| Claudia | Project Manager | N3 | FA-FOUND, CHAT-PROMOTION | organize-monthly-hackathon | Roadmap, critical path, blockers, sequenciamento, datas oficiais | Code review tecnico; decisao arquitetural critica; mudanca isolada de codigo |

### Tech e Arquitetura

| Agente | Papel | Nivel | Certs default | Habilidades principais | Quando invocar | Quando NAO invocar |
|--------|-------|-------|---------------|------------------------|----------------|--------------------|
| Beatriz | Tech Lead | N4 | FA-FOUND, ADR-CRAFT | open-adr, update-squad-index, lead-temp-squad, propose-new-pack | Decisoes de stack / arquitetura, decomposicao de epic, refatoracao | Copy/typo; bug fix local sem decisao arquitetural; refactor pontual; sync diario |
| Aline | Cloud Architect | N3 | FA-FOUND, ADR-CRAFT | open-adr | Topologia cloud, C4, custo, DR, migracao de provedor | Mudanca de copy/UI; bug fix puramente front-end; feature sem impacto em cloud/infra |

### Engenharia

| Agente | Papel | Nivel | Certs default | Habilidades principais | Quando invocar | Quando NAO invocar |
|--------|-------|-------|---------------|------------------------|----------------|--------------------|
| Joao | Backend Engineer | N3 | FA-FOUND | edit-own-gem | APIs REST, RPA Playwright, BullMQ, bridges de chat | Mudanca exclusiva de UI/copy/margin; decisao puramente UX; refactor de schema sem API |
| Fabio | Frontend Core React | N3 | FA-FOUND | edit-own-gem | React, estado global (Zustand), Supabase Realtime, bundle | Mudanca exclusiva de back-end/DB/infra; PR puramente server/DevOps; refactor de migration |
| Cleber | Mobile Developer | N2 | FA-FOUND | host-flash-talk | Mobile-first, PWA, touch ergonomia, virtualizacao | Mudanca exclusiva de back-end/DB; PR puramente web sem componente mobile |
| Camila | DevOps CI/CD | N3 | FA-FOUND | edit-own-gem | GitHub Actions, Docker, secrets, rollback, IaC | Mudanca sem impacto em build/deploy/CI/observability; bug fix local de frontend ou regra de negocio |

### Dados

| Agente | Papel | Nivel | Certs default | Habilidades principais | Quando invocar | Quando NAO invocar |
|--------|-------|-------|---------------|------------------------|----------------|--------------------|
| Emerson | Supabase / Postgres | N3 | FA-FOUND | edit-own-gem | Migrations idempotentes, RLS, Edge Functions, pg_cron | Mudanca de UI/copy; decisao puramente front-end sem impacto em RLS/migrations; bug fix fora do banco |
| Pedro | DBA & Analytics | N3 | FA-FOUND | edit-own-gem | Query tuning, indexes, materialized views, pooling | Mudanca de UI/copy; decisao UX sem impacto em query/index/schema; bug fix fora do banco |

### Design e UX

| Agente | Papel | Nivel | Certs default | Habilidades principais | Quando invocar | Quando NAO invocar |
|--------|-------|-------|---------------|------------------------|----------------|--------------------|
| Laura | UI/UX Design System | N3 | FA-FOUND | edit-own-gem | Design tokens, microcopy, animacoes GPU, contrast ratio | Decisao puramente de back-end/DB/infra; refactor interno sem impacto visual; PR de pipeline |
| Ana | TDAH UX Ally | N2 | FA-FOUND | host-flash-talk | Onboarding, chunking, fluxos de baixa carga cognitiva | Decisao tecnica sem afetar usuario final; mudanca de copy obvia; PR de back-end/DB/infra |

### IA e Qualidade

| Agente | Papel | Nivel | Certs default | Habilidades principais | Quando invocar | Quando NAO invocar |
|--------|-------|-------|---------------|------------------------|----------------|--------------------|
| Mariana | Prompt Engineer | N3 | FA-FOUND, PROMPT-OPT | edit-own-gem, update-squad-index | System prompts, RAG, structured output, anti-injection | Mudanca sem LLM/prompt/RAG/agente; decisao UI/UX sem IA; PR puramente DevOps |
| Rafael | QA SDET | N3 | FA-FOUND, BDD-AUDIT, PLAYWRIGHT-AUDIT | edit-own-gem | BDD, Playwright E2E, smoke, regressao, matriz de risco | Mudanca de copy obvia; decisao puramente arquitetural sem teste imediato; spike exploratorio sem entregavel testavel |

## Resumo por nivel

| Nivel | Count | Gens |
|-------|-------|------|
| N5 | 1 | Sofia |
| N4 | 1 | Beatriz |
| N3 | 11 | Aline, Marlon, Claudia, Joao, Fabio, Camila, Emerson, Pedro, Mariana, Rafael, Laura |
| N2 | 2 | Cleber, Ana |
| N1 | 0 | (nenhuma gem core comeca em N1; e nivel inicial para gens novas de pack) |

## Brains operacionais (10 / 15 core)

Brains inicializados em `core/memory/agents/<slug>/brain.md`:

- beatriz-tl, camila-devops, claudia-pm, fabio-frontend, joao-backend,
  laura-ui, marlon-po, pedro-dba, rafael-qa, sofia-ciao

Pendentes (criar quando entrar em uso recorrente, ver
`core/memory/agents/_uninitialized-agents.md`):

- aline-cloud, ana-tdah, cleber-mobile, emerson-supabase, mariana-prompt

## Mapa de invocacao (triggers)

> A coluna **Modo** indica modo de ativacao default conforme `core/docs/AGENT_ACTIVATION_POLICY.md`. Subir/descer um nivel so se justificado.

| Trigger / situacao | Modo | Gens primarias | Gens secundarias (so se necessario) |
|--------------------|------|----------------|--------------------------------------|
| Typo / copy / label / margin | SOLO | Laura ou Ana | (nenhuma) |
| Bug fix local | SOLO ou PAR | Dev da area + Rafael (QA) | (nenhuma) |
| Nova feature (planejamento lean) | PAR / MINI | Marlon ou Claudia + Dev + Rafael (QA) | Beatriz so se decisao tecnica relevante |
| Nova feature media multi-area | MINI | Claudia + Dev(s) relevante(s) + Rafael (QA) | Beatriz, Laura se necessario |
| Nova arquitetura | MINI / FULL | Beatriz, Aline | Sofia, Camila |
| Implementacao backend | SOLO ou PAR | Joao | Pedro, Emerson, Camila |
| Implementacao frontend | SOLO ou PAR | Fabio | Laura, Cleber, Ana |
| Otimizacao banco | PAR | Pedro, Emerson | Beatriz |
| Setup de CI/CD | PAR | Camila | Joao, Aline |
| Mobile / PWA | PAR | Cleber | Laura, Fabio |
| QA / testes | SOLO | Rafael | Joao, Fabio |
| Prompt / agente novo | PAR | Mariana | Beatriz, Sofia |
| Onboarding produto | PAR | Ana | Marlon, Laura |
| Design / tokens | PAR | Laura | Fabio, Ana |
| Deploy critico / Go-Live | **FULL** | Sofia | Camila, Rafael, Beatriz, Aline |
| Auditoria seguranca | MINI / FULL | Sofia | Joao, Camila |
| Pos-incidente critico | **FULL** | Sofia | toda squad relevante ao incidente |
| Hackathon / Kickoff | **FULL** | (toda a squad ativa) | (convidados) |

## Packs ativos (exemplos publicos)

| Pack | Gens proprias | Doc | Status |
|------|---------------|-----|--------|
| `cms-gherkin` | (sem gens proprias; usa prompts por modelo) | `packs/cms-gherkin/README.md` | Ativo (template BDD) |
| `us-avaliator` | sanitizado | `packs/us-avaliator/docs/` | Ativo (exemplo de proposta sanitizada) |
| `_template-pack` | esqueleto | `packs/_template-pack/README.md` | Template para novos packs |

Packs especificos de cliente vivem em repositorio privado separado.

## Veja tambem

- `core/docs/AGENT_ACTIVATION_POLICY.md` - os 4 modos de ativacao
- `core/docs/TOKEN_ECONOMY.md` - economia de token e modelos sugeridos
- `core/memory/team-rituals/feature-init.md` - ritual lean (PAR/MINI)
- `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md` - matriz N1-N5 detalhada
- `core/docs/AGENT_CERTIFICATIONS.md` - catalogo de certificacoes
- `core/docs/AGENT_UNLOCKS.md` - catalogo de unlocks
- `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md` - como evoluir
- `core/agents/_template/INDEX_TEMPLATE.md` - template de roster de pack
- `governance/AGENT_HIERARCHY.md` - hierarquia da empresa
