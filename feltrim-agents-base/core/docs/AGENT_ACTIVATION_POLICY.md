# Agent Activation Policy

> Quantos agentes invocar para uma tarefa. **Default: o menor modo que
> resolve a tarefa com qualidade.** Convocar mais que o necessario nao
> melhora resultado e queima token sem retorno.

## Por que isso existe

Feedback real (2026-05): squad atuando "constante em todo projeto" gera:

- Token cost descontrolado.
- Decisao em comite onde nao precisa.
- Ritual virando compulsao (code review automatico em cada init, team-call em mudanca de copy, Sofia CIAO opinando em margin de div).

Solucao validada por uso: **filtro por funcionalidade + acompanhamento minimo de GP + QA**. So convoca quem move a feature.

## Os 4 modos de ativacao

### Modo 1 — SOLO

**Quem:** 1 agente.

**Quando usar:**

- Mudanca de copy, microcopy, label, texto.
- Fix de typo / lint / formatacao.
- Refactor local sem impacto de API.
- Ajuste visual pequeno (margin, padding, cor, icone).
- Documentacao isolada (README, comentario, ADR pequeno).
- Atualizacao de dependencia patch (`x.y.Z`).
- Resposta a duvida factual conhecida.

**Custo tipico:** 1k-5k tokens.

**Exemplo:**

```text
Tarefa: ajustar copy do CTA "Comprar" para "Finalizar compra".
Agente: Laura (UI/UX) sozinha — ou Ana TDAH se a duvida e sobre clareza.
NAO convocar: ninguem mais. Sem code review, sem team-call.
```

### Modo 2 — PAR

**Quem:** 2 agentes (geralmente dev + QA, ou dev + PO, ou PO + UX).

**Quando usar:**

- Implementacao pequena/media de uma feature simples.
- Bug fix com reteste.
- Story refinement bilateral.
- Spike tecnico curto.
- Decisao tatica entre 2 alternativas claras.

**Custo tipico:** 5k-20k tokens.

**Exemplo:**

```text
Tarefa: implementar endpoint POST /orders com validacao basica.
Par: Joao (Backend) implementa + Rafael (QA) valida com BDD.
NAO convocar: Aline (cloud), Sofia (CIAO), Beatriz (TL), Camila (DevOps).
```

### Modo 3 — MINI-SQUAD

**Quem:** 3 a 5 agentes selecionados por contexto.

**Quando usar:**

- Feature media com impacto cross (frontend + backend + dados).
- Refactor com impacto contratual entre modulos.
- Implementacao com decisao de design relevante mas nao arquitetural.
- ADR de escopo limitado.
- Investigacao de bug com hipoteses cruzadas.

**Custo tipico:** 20k-80k tokens.

**Exemplo:**

```text
Tarefa: feature "exportar relatorio CSV" (UI -> API -> DB query -> file).
Mini-squad: Fabio (Frontend) + Joao (Backend) + Pedro (DBA) + Rafael (QA) + Claudia (PM/coordena).
NAO convocar: Aline, Sofia, Beatriz, Camila, Cleber, Laura, Mariana, Marlon, Emerson, Ana.
```

### Modo 4 — FULL TEAM MEETING

**Quem:** todos os agentes relevantes (5+ ate 15).

**Quando usar (so estes triggers):**

- **Release / Go-Live decision**.
- **Pre-deploy de mudanca de arquitetura relevante**.
- **Pos-incidente critico** (post-mortem).
- **Hackathon / Kickoff de projeto novo**.
- **Auditoria periodica de capability/promotion** (ver `PROMOTION_AND_EVOLUTION_CRITERIA.md`).
- **Revisao de proposta executiva** (ver `packs/us-avaliator/` como case).
- **Decisao estrategica multi-vertical** (ex.: trocar stack do projeto).

**Custo tipico:** 80k-500k+ tokens (use modelo barato para a maioria + modelo premium para Sofia CIAO consolidar).

**Exemplo:**

```text
Tarefa: revisar release v2.0 antes de ir pra prod.
Full team: Aline + Beatriz + Camila + Claudia + Cleber + Emerson + Fabio + Joao + Laura + Mariana + Marlon + Pedro + Rafael + Sofia + Ana.
Sofia CIAO consolida veredito final.
```

## Como decidir o modo (em 30 segundos)

```text
Pergunta 1: A tarefa toca codigo/regra de mais de UMA area (UI, API, DB, infra, processo)?
  - Nao -> SOLO ou PAR.
  - Sim -> MINI-SQUAD ou FULL.

Pergunta 2: A decisao e reversivel com baixo custo?
  - Sim -> SOLO ou PAR.
  - Nao (release, arquitetura, contrato) -> MINI-SQUAD ou FULL.

Pergunta 3: O risco de errar afeta cliente externo / SLA / billing / compliance?
  - Nao -> SOLO, PAR ou MINI.
  - Sim -> MINI ou FULL com Sofia CIAO no veredito.

Pergunta 4: Ja existe contexto suficiente em brain/memoria do agente para decidir?
  - Sim -> reduzir 1 nivel de modo.
  - Nao -> manter ou subir 1 nivel.

Default quando em duvida: COMECAR PAR. Subir se aparecer divergencia que justifique.
```

## Regra de ouro

> Nao convocar agente "por garantia". Convocar agente porque o output dele
> muda a decisao. Se Aline so vai dizer "ok ta bom" sem evidencia, ela
> nao deveria ter sido chamada.

## Anti-patterns proibidos

- **Code review automatico no init de cada feature.** Code review e ritual ativado por PR/commit/merge, nao por inicio de implementacao.
- **Sofia CIAO em mudanca de copy/UI pequena.** Sofia opera no nivel executivo, nao operacional.
- **Aline Cloud em decisao puramente front-end.** Inverso vale: Laura nao opina em C4 diagram.
- **Convocar 5+ agentes "so pra ouvir opiniao".** Opiniao nao acionavel e ruido.
- **Repetir convocacao identica entre features parecidas.** Se a mesma squad ja resolveu 3x, transforma em ritual com escopo definido.

## Permissao para "downgrade"

Qualquer agente convocado pode, no inicio do output, dizer:

```text
[ATIVACAO INADEQUADA] Minha participacao nao agrega valor a esta tarefa porque
<motivo objetivo>. Sugiro remover-me da convocacao e seguir com <agentes
necessarios>.
```

Decisor humano avalia se aceita o downgrade. Isso e **virtude**, nao falha.

## Permissao para "upgrade"

Qualquer agente convocado pode pedir reforco:

```text
[UPGRADE NECESSARIO] Identifiquei <risco / dependencia / decisao fora do meu
escopo> que exige <nome do agente>. Pauso a contribuicao ate decisor humano
decidir convocar reforco.
```

Decisor humano decide convocar ou seguir aceitando o risco.

## Medicao

Recomendado, mas opcional. Toda sessao pode registrar:

```text
modo: <SOLO|PAR|MINI|FULL>
agentes_invocados: <lista>
agentes_que_realmente_contribuiram: <lista>
tokens_estimados: <numero>
deliverable: <link/path>
data: YYYY-MM-DD HH:MM
```

Se `agentes_invocados != agentes_que_realmente_contribuiram`, ajustar a regra de selecao para a proxima vez similar.

Ver `core/docs/TOKEN_ECONOMY.md` para diretrizes complementares.

## Veja tambem

- `core/docs/TOKEN_ECONOMY.md` — economia de token e modelos sugeridos
- `core/docs/SQUAD_INDEX.md` — coluna "Quando NAO invocar" por agente
- `core/memory/team-rituals/feature-init.md` — ritual lean
- `core/memory/team-rituals/team-call.md` — ritual full
- `examples/example-feature-lean.md` — exemplo PAR/MINI
- `examples/example-spawn-team-meeting.md` — exemplo FULL (so para triggers do modo 4)
- `governance/RITUALS_GUARDRAILS.md` — ritual e simbolico, ativacao e operacional
