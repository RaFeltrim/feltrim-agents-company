<!-- origem: feltrim-agents-base/feltrim-agents-base/memory/agents/_uninitialized-agents.md; sanitizada em 2026-05-16: caminhos atualizados para core/agents/ e core/memory/agents/ -->

---
name: agents_uninitialized_brains
description: Agentes existentes que ainda nao possuem cerebro operacional inicial
type: reference
---

# Agentes ainda sem cerebro inicial

Este indice evita criar pastas vazias para cada gem. Os agentes abaixo estao
disponiveis pelos prompts em `core/agents/`, mas ainda nao receberam cerebro
operacional persistente dedicado.

## Criar quando houver uso recorrente

- `core/agents/gem_aline_cloud.md` - Aline Cloud Architect.
- `core/agents/gem_ana_tdah.md` - Ana TDAH UX Ally.
- `core/agents/gem_cleber_mobile.md` - Cleber Mobile.
- `core/agents/gem_emerson_supabase.md` - Emerson Supabase / Postgres.
- `core/agents/gem_mariana_prompt.md` - Mariana Prompt Engineering.

## Criterios para inicializar

Crie uma pasta em `core/memory/agents/<slug>/brain.md` quando o agente:

- participar de 2+ calls ou handoffs no mesmo projeto;
- acumular aprendizado que nao cabe no prompt canonico;
- assumir pendencia recorrente;
- virar dono de decisao, runbook, ADR, checklist ou indicador;
- precisar registrar limites humanos especificos.

Use `_templates/agent-brain-template.md` como base.

Para packs especializados (`packs/<pack>/`), o brain do agente especifico do
pack vive em `packs/<pack>/brains/<slug>/brain.md`, nao em
`core/memory/agents/`.
