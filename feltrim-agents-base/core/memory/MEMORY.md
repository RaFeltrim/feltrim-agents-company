---
name: core_memory_index
description: Indice raiz da memoria operacional do Feltrim Agents Framework (core, generico)
type: reference
---

# Core Memory - Indice

Este e o indice raiz da memoria operacional generica do Feltrim Agents
Framework. Toda memoria que nao for de pack especifico vive em `core/memory/`.

Memorias de projeto especifico vivem em `packs/<pack>/brains/` ou
`packs/<pack>/docs/`. Memorias historicas vivem em repositorio privado
separado (snapshots arquivados).

## Convencao de frontmatter

Todo arquivo de memoria comeca com:

```yaml
---
name: <slug_unico_em_snake_case>
description: <descricao curta de 1 linha>
type: user | project | feedback | reference | agent | team-ritual
---
```

`type` ajuda o orquestrador a decidir o que carregar no boot e o que carregar
sob demanda. O default e carregar tudo de `type: reference` no boot do core.

## Arvore

```
core/memory/
|-- MEMORY.md                              (este arquivo)
|-- agents/
|   |-- README.md                          (indice dos brains operacionais)
|   |-- time-scale.md                      (convencao 1 dia humano = 1 hora agente)
|   |-- _uninitialized-agents.md           (agentes ainda sem brain)
|   |-- _templates/
|   |   |-- agent-brain-template.md
|   |   |-- pre-daily-template.md
|   |   |-- team-call-template.md
|   |   |-- agent-profile-template.md      (cartao executivo do agente)
|   |   `-- agent-capability-review-template.md (unidade auditavel de evolucao)
|   |-- beatriz-tl/brain.md
|   |-- camila-devops/brain.md
|   |-- claudia-pm/brain.md
|   |-- fabio-frontend/brain.md
|   |-- joao-backend/brain.md
|   |-- laura-ui/brain.md
|   |-- marlon-po/brain.md
|   |-- pedro-dba/brain.md
|   |-- rafael-qa/brain.md
|   `-- sofia-ciao/brain.md
`-- team-rituals/
    |-- README.md
    |-- pre-daily.md
    |-- flash-talks.md
    |-- game-nights.md
    |-- monthly-hackathons.md
    |-- prototype-to-product-checklist.md
    |-- team-call-notes-template.md
    |-- snack-break-notes-template.md
    |-- game-night-notes-template.md
    |-- hackathon-idea-template.md
    `-- hackathon-scorecard-template.md
```

## Que carregar no boot

- Sempre: `MEMORY.md`, `agents/README.md`, `agents/time-scale.md`,
  `agents/_uninitialized-agents.md`, `team-rituals/README.md`.
- Quando uma gem for invocada: carregar o `brain.md` correspondente.
- Sob demanda: templates so quando criar artefato novo.

## Que NAO entra em `core/memory/`

- Massas de dados de cliente (vai para fora do repo).
- Credenciais (vivem em `.env` local, nunca commitar).
- Evidencias com PII (ficam fora do repo ou em pack com ACL).
- Brains de agentes de pack (vao para `packs/<pack>/brains/`).
- Aprendizados especificos de cliente (vao para `packs/<cliente>/brains/`).
- Conversas sociais ou rituais antigos sem promocao para ADR (descartar).

## Veja tambem

- `core/protocols/MEMORY_AND_RAG_POLICY.md` - quando gravar, quando recuperar
- `core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md` - quando promover conversa para artefato
- `core/docs/OPERATING_MODEL.md` - 10 pilares do sistema de agentes
