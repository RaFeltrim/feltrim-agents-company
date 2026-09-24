# Decisoes Pendentes - Feltrim Agents Base (publico)

Este arquivo concentra decisoes em aberto sobre o boilerplate publico. Cada
item tem hipoteses, recomendacao e quem decide.

> Itens internos da empresa (packs proprios, snapshots historicos,
> negociacoes de IP de terceiros) vivem em repositorio privado separado e
> nao aparecem aqui.

## Status geral

| ID | Item | Status |
|----|------|--------|
| 1 | Spec Kit no boilerplate | Implementado (`.specify/memory/constitution.md` generico) |
| 2 | Versao canonica das gens | Implementado (v2 sanitizada como base) |
| 3 | Licenca final | Pendente (proprietaria provisoria em vigor) |
| 4 | Split `integrations/` core vs pack | Implementado default (core com placeholders) - falta auditoria por integracao |
| 5 | Politica de ativacao de agentes e economia de token | Implementado em PR11 - falta medir consumo real e calibrar |
| 6 | Boot sequence `CLAUDE.md` raiz | Implementado (ponteiro para `core/CLAUDE.md`) |
| 7 | Brains com aprendizados especificos | Implementado (split core vs pack) |

---

## 1. Spec Kit `.specify/` no boilerplate

**Contexto:** Spec Kit pode acelerar novos projetos quando ja vem como
template no boilerplate.

**Hipoteses:**

- (A) Sim, com constituicao generica em `.specify/memory/constitution.md`
  (5 principios sem referencia a cliente especifico).
- (B) Nao - Spec Kit e por projeto, nao por empresa.

**Recomendacao default:** (A). **IMPLEMENTADO.**

**Decisor:** quem adotar o boilerplate.

---

## 2. Versao canonica das gens (15 papeis)

**Contexto:** Existem 3 versoes paralelas de cada papel no historico do
framework (v1, v2, v3).

**Recomendacao default:** Usar v2 como base (mais rica), aplicar sanitizacao
(remover referencias especificas), adicionar referencia explicita aos 8
protocolos do v3. Templates v1 ficam em `core/agents/_template/skeletons/`.
**IMPLEMENTADO.**

**Decisor:** pode ser revisado a qualquer momento.

---

## 3. Licenca final

**Contexto:** `LICENSE` esta como proprietaria provisoria.

**Hipoteses:**

- (A) Proprietaria fechada.
- (B) Source-available com clausula no-commercial.
- (C) MIT / Apache 2.0 (open source).
- (D) Dual license: core MIT, packs proprietarios.

**Recomendacao default:** Manter (A) ate decisao explicita.

**Decisor:** Rafael Feltrim.

---

## 4. Split `integrations/` core vs pack

**Contexto:** `core/integrations/` tem placeholders para openclaw, n8n,
obsidian, pixel-agents. Algumas sao genericas (n8n, obsidian) e outras
podem ser especificas de uma empresa.

**Hipoteses:**

- (A) Tudo em `core/integrations/` como esqueletos genericos (sem
  credenciais), e packs especificos referenciam.
- (B) Split por integracao baseado em quao especifica e.

**Recomendacao default:** (A). **IMPLEMENTADO.**

**Decisor:** quem adotar o boilerplate.

---

## 5. Politica de ativacao de agentes e economia de token

**Status PR11 (2026-05-16):** IMPLEMENTADO. Falta medir consumo real e
calibrar.

**Contexto:** Feedback real de uso indicou que squad atuando "constante
em todo projeto" gera custo de token alto e ritualizacao indesejada
(code review automatico, CIAO em decisao tatica, team-call em mudanca
de copy). Solucao validada em campo: filtro por funcionalidade + lean
activation (modos SOLO/PAR/MINI/FULL).

**Implementado em PR11:**

- `core/docs/AGENT_ACTIVATION_POLICY.md` - 4 modos
- `core/docs/TOKEN_ECONOMY.md` - 7 regras + anti-patterns + tabela
  modelo/modo
- `core/memory/team-rituals/feature-init.md` - ritual lean
- `core/memory/team-rituals/README.md` - secao "quando NAO convocar
  FULL"
- 15 gens core - secao "Trigger anti-patterns (quando NAO invocar)"
- `core/docs/SQUAD_INDEX.md` v2.2 - coluna "Quando NAO invocar" + modo
  default em mapa de invocacao
- `examples/example-feature-lean.md` - novo (default para 80% das
  features)
- `examples/example-spawn-team-meeting.md` - editado com aviso de custo
- `examples/example-model-benchmark.md` - novo (para benchmark de novos
  modelos quando lancarem)
- `governance/SECURITY_AND_PRIVACY.md` - secao "Consumo de token como
  risco operacional" + severidades T1/T2/T3

**Pendente decisao (proxima rodada):**

- [ ] Medir custo real em USD/mes por modo (PAR/MINI/FULL).
- [ ] Calibrar tabela de modelos sugeridos quando modelos novos
  publicarem (proximas geracoes Codex / Claude / GPT, etc.).
- [ ] Decidir se cria scoreboard operacional de "agentes convocados x
  contribuiram" por sessao.
- [ ] Avaliar adicao de hard cap de tokens por modo apos 1 mes de
  observacao.

**Decisor:** quem adotar o boilerplate.

---

## 6. Boot sequence (CLAUDE.md raiz)

**Contexto:** O CLAUDE.md original tem boot sequence elaborada com
leitura obrigatoria de MEMORY.md, glob de agents, etc.

**Recomendacao default:** `CLAUDE.md` raiz e ponteiro para
`core/CLAUDE.md`, que mantem o boot. Boot sequence sanitizada (sem
referencia a cliente especifico). **IMPLEMENTADO.**

---

## 7. Brains com aprendizados especificos de projeto

**Contexto:** Brains de agente podem conter aprendizados de projeto
cliente, marketplaces internos ou genericos.

**Recomendacao default:** SPLIT:

- Brains de papeis genericos (beatriz-tl, camila-devops, joao-backend,
  etc.) vao para `core/memory/agents/<slug>/brain.md` apos sanitizacao.
- Brains especificos de cliente vao para `packs/<cliente>/brains/<slug>/brain.md`
  (em repositorio privado).

**IMPLEMENTADO.**

---

## Como contribuir com decisoes

Para resolver qualquer item:

1. Anotar a decisao tomada neste arquivo (riscar a sessao e marcar
   `RESOLVIDO em YYYY-MM-DD: <opcao escolhida> - <quem decidiu>`).
2. Implementar a mudanca em PR proprio.
3. Atualizar `README.md` raiz se o mapa do repo mudar.

---

## Repositorio relacionado

- **Repositorio privado da empresa:** mantem packs especificos de
  cliente, snapshots historicos de versoes anteriores do framework e
  itens com IP pendente de auditoria. Nao publicado.
- **Este repositorio:** boilerplate publico, generico, reutilizavel.
