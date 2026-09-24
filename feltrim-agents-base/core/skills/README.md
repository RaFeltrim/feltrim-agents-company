# Core Skills (esqueleto)

Pasta reservada para Cursor Agent Skills, MCP server skills, ou workflow
skills compartilhadas entre packs.

## Estrutura recomendada

```
core/skills/
|-- README.md                              (este arquivo)
|-- <skill-slug>/
|   |-- SKILL.md                           (instrucoes da skill)
|   |-- scripts/                           (scripts opcionais)
|   `-- references/                        (referencias opcionais)
```

## Skill comum

Nao ha skills core consolidadas ainda. Sugestoes de partida:

- `agent-promote-skill` - automatiza criacao de capability review + atualizacao
  de agent-profile.
- `pack-init-skill` - guia para instanciar `packs/_template-pack/` em um novo
  pack (referenciado em `examples/example-pack-init.md`).
- `evidence-pdf-skill` - converte sessao de execucao em PDF auditavel
  (skill generica reutilizavel por qualquer pack QA).

Skills especificas de pack vivem em `packs/<pack>/skills/` ou em
`<pack>/SKILL.md`.
