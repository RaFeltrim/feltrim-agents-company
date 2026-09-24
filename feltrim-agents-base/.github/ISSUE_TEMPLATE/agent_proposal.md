---
name: Agent proposal
about: Propor nova gem (papel novo) ou nova certificacao/unlock
title: "[AGENT] "
labels: ["agent-proposal", "triage"]
assignees: ''
---

## Tipo de proposta

- [ ] Nova gem (papel novo nao coberto pelas 15 atuais)
- [ ] Nova versao de gem existente (refator de prompt)
- [ ] Nova certificacao interna
- [ ] Novo unlock (habilidade desbloqueavel)

---

## Se for NOVA GEM

### Identidade proposta

- **Nome:** 
- **Papel curto:** 
- **Papel longo:** 
- **Slug do arquivo:** `gem_<slug>.md`
- **Pack:** `core/` ou `packs/<pack>/`

### Justificativa

<!-- Por que as 15 gens atuais NAO cobrem essa necessidade? -->

### Boundary com outras gens

| Gem similar atual | Como esta gem nova se diferencia |
|-------------------|----------------------------------|
| `gem_X.md` | |

### Nivel inicial sugerido

- [ ] N1 - operacional assistido (revisao em cada saida)
- [ ] N2 - especialista de execucao (revisao por amostragem)
- [ ] N3 - senior autonomo (revisao em decisao critica)
- [ ] N4 - lead (decisao estrategica humana)
- [ ] N5 - so via decisor humano

### Certificacoes default

<!-- Quais certs essa gem ja tem ao ser criada? (FA-FOUND e default) -->

### Unlocks default

<!-- Quais habilidades ja desbloqueadas? Listar slugs do AGENT_UNLOCKS.md -->

### Quando invocar

<!-- 3-5 gatilhos especificos -->

### Quando NAO invocar (anti-patterns)

<!-- 3-5 cenarios onde outro agente seria melhor -->

---

## Se for NOVA CERTIFICACAO

### Codigo proposto

`<CODIGO>` (formato: `<AREA>-<NOME-CURTO>`)

### Categoria

- [ ] Foundation (toda gem deve ter)
- [ ] Tecnica
- [ ] Governanca
- [ ] Pack-specific (especificar pack)

### O que prova

<!-- 3-5 competencias verificaveis -->

### Evidencia exigida

<!-- Artefatos auditaveis para emitir a cert -->

### Agentes elegiveis

<!-- Lista ou "todos" -->

### Emissor

<!-- Quem aprova? Sofia CIAO + decisor humano? -->

---

## Se for NOVO UNLOCK

### Slug

`<verbo>-<objeto>` (ex.: `apply-tech-veto`, `host-flash-talk`)

### Descricao

<!-- 1 frase -->

### Pre-requisitos

<!-- Certs / nivel / endorso necessario -->

### Agentes elegiveis

<!-- Lista de gens -->

### Guardrails

<!-- O que essa habilidade NAO autoriza fazer -->

---

## Checklist universal

- [ ] Li `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md`.
- [ ] Li `core/docs/AGENT_CERTIFICATIONS.md` ou `core/docs/AGENT_UNLOCKS.md`.
- [ ] Li `governance/PROMOTION_POLICY.md` ou `governance/CERTIFICATION_POLICY.md`.
- [ ] A proposta NAO conflita com hierarquia atual em
      `governance/AGENT_HIERARCHY.md`.
- [ ] A proposta NAO assume cliente real ou marketplace especifico.
