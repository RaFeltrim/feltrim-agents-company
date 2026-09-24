---
name: Bug report
about: Reportar comportamento errado em script, doc, link ou prompt
title: "[BUG] "
labels: ["bug", "triage"]
assignees: ''
---

## Descricao

<!-- O que esta acontecendo de errado? -->

## Como reproduzir

1. Va para `<arquivo / pasta>`
2. Faca `<acao>`
3. Observe `<comportamento errado>`

## Comportamento esperado

<!-- O que voce esperava acontecer -->

## Comportamento atual

<!-- O que aconteceu de fato -->

## Severidade (auto-avaliacao)

- [ ] **Critica** - bloqueia uso do repo / vazamento de IP / quebra de sanitizacao
- [ ] **Alta** - quebra fluxo principal (boot sequence, ritual core)
- [ ] **Media** - quebra fluxo secundario (link quebrado, doc desatualizada)
- [ ] **Baixa** - typo, formatacao, melhoria editorial

## Contexto

- Versao do repo (commit SHA): 
- CLI / IDE usado: 
- Sistema operacional: 
- Modelo LLM usado (se aplicavel): 

## NAO inclua

- Flag words da sua empresa.
- Email corporativo.
- Credenciais ou segredos.
- Dados de cliente real.

Se houver leak deste tipo no repo, **NAO abra issue publica**: siga
`SECURITY.md` e use Security Advisory privado.
