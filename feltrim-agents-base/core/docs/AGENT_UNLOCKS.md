# Agent Unlocks - Catalogo de Habilidades

> Catalogo das habilidades operacionais desbloqueaveis. Unlocks sao mais
> granulares que certificacoes: cada unlock e uma acao concreta que o agente
> pode realizar sem nova autorizacao.
>
> Catalogo generico de unlocks aplicaveis a qualquer pack.

## Formato canonico de unlock

```markdown
### <slug-unlock> - <Nome curto>

- **Descricao:** o que a habilidade permite fazer
- **Pre-requisitos:** nivel minimo + certificacoes
- **Evidencias aceitas para desbloqueio:** lista de artefatos auditaveis
- **Agentes elegiveis:** lista ou "todos N<x>+"
- **Guardrails:** o que continua bloqueado mesmo com este unlock
- **Como revogar:** condicoes que invalidam o unlock
```

## Unlocks de governanca

### open-adr - Abrir ADR sozinho

- **Descricao:** pode criar arquivo em `core/docs/adr/` ou `packs/<pack>/adr/` sem revisao previa.
- **Pre-requisitos:** N3 + `ADR-CRAFT`.
- **Evidencias:** 3 ADRs anteriores aceitos.
- **Agentes elegiveis:** Beatriz-TL, Aline-Cloud, Sofia-CIAO, agentes N4+ de pack.
- **Guardrails:** ADR ainda passa por revisao apos criacao; nao vira "accepted" sem decisor humano.
- **Revogar:** se a gem aprovar ADR irreversivel sem alternativas consideradas.

### update-squad-index - Atualizar SQUAD_INDEX sem revisao

- **Descricao:** pode editar `core/docs/SQUAD_INDEX.md` para adicionar nova gem, atualizar nivel ou cert.
- **Pre-requisitos:** N4.
- **Evidencias:** 5 atualizacoes anteriores com revisao positiva por par.
- **Agentes elegiveis:** Sofia-CIAO, Beatriz-TL, Mariana-Prompt.
- **Guardrails:** mudanca em coluna `Nivel` exige capability review fechada para aquele agente.
- **Revogar:** se introduzir gem inexistente, nivel sem evidencia ou cert sem catalogo.

### edit-own-gem - Editar gem propria

- **Descricao:** pode modificar a gem em `core/agents/gem_<nome>.md` que define a si mesma.
- **Pre-requisitos:** N3 + `FA-FOUND` + revisao par positiva.
- **Evidencias:** 1 capability review com nota >= 4/5 em "auto-conhecimento".
- **Agentes elegiveis:** todas as gens N3+.
- **Guardrails:** mudanca de persona ou senioridade declarativa exige decisor humano. Mudanca de regras de comportamento exige Sofia-CIAO.
- **Revogar:** se editar gem para relaxar guardrail proprio.

### propose-new-pack - Propor pack novo

- **Descricao:** pode criar branch + PR com novo `packs/<pack>/` esqueleto.
- **Pre-requisitos:** N4 + `FA-FOUND`.
- **Evidencias:** participacao em 2 packs ja consolidados.
- **Agentes elegiveis:** Beatriz-TL, Sofia-CIAO, Aline-Cloud, agentes N4+ de packs existentes.
- **Guardrails:** pack so vira ativo apos aprovacao do decisor humano e do CIAO.
- **Revogar:** se propor pack que duplica funcao de pack existente.

### lead-temp-squad - Liderar squad temporario

- **Descricao:** pode coordenar outros agentes em projeto ad-hoc, definindo planos e handoffs.
- **Pre-requisitos:** N4.
- **Evidencias:** 1 capability review com nota >= 4/5 em "coordenacao".
- **Agentes elegiveis:** Sofia-CIAO, Beatriz-TL, agentes orchestrator de packs.
- **Guardrails:** decisao final continua com decisor humano.
- **Revogar:** se squad temporario gerar conflito entre gens sem resolucao.

### apply-tech-veto - Aplicar veto tecnico

- **Descricao:** pode bloquear deploy / merge por risco tecnico identificado.
- **Pre-requisitos:** N5 + `CIAO-GO-LIVE-READY`.
- **Evidencias:** 5 vereditos com rastreabilidade.
- **Agentes elegiveis:** Sofia-CIAO apenas.
- **Guardrails:** veto pode ser sobrescrito por decisor humano com registro do risco aceito.
- **Revogar:** se veto for emitido sem evidencia auditavel.

## Unlocks operacionais

### update-external-status - Atualizar status oficial em sistema externo

- **Descricao:** pode escrever em Azure DevOps / Jira / Linear / GitHub
  Issues como source of truth.
- **Pre-requisitos:** N3 + `CHAT-PROMOTION` + autorizacao explicita por
  projeto.
- **Evidencias:** 5 atualizacoes anteriores com snapshot antes/depois.
- **Agentes elegiveis:** apenas gens explicitamente autorizadas em
  `packs/<pack>/docs/`.
- **Guardrails:** NUNCA em automacao pura - sempre com revisao humana ou
  com flag explicita `--auto-publish` documentada.
- **Revogar:** se atualizar status sem evidencia que comprove o status.

### promote-prototype - Promover prototipo a MVP

- **Descricao:** pode marcar prototipo como candidato a produto, abrindo
  fluxo de avaliacao formal.
- **Pre-requisitos:** N4 + participacao em 1 hackathon mensal.
- **Evidencias:** prototipo testado + scorecard + KPI alvo definido.
- **Agentes elegiveis:** Marlon-PO, Beatriz-TL, Sofia-CIAO.
- **Guardrails:** promocao a "produto vendavel" exige decisor humano e
  passagem por `prototype-to-product-checklist.md`.

### approve-pr-self-merge - Auto-merge de PR proprio

- **Descricao:** pode mergear PR que abriu, sem revisao manual.
- **Pre-requisitos:** N4 + 10 PRs anteriores merged com revisao positiva.
- **Evidencias:** historico de PRs.
- **Agentes elegiveis:** apenas em packs onde o decisor humano autorizou
  explicitamente.
- **Guardrails:** PRs em `core/` SEMPRE precisam de Sofia-CIAO + decisor
  humano, nunca auto-merge.

## Unlocks de cultura (simbolicos, nao operacionais)

### lead-pre-daily - Conduzir pre-daily

- **Descricao:** pode conduzir o ritual de pre-daily como facilitador.
- **Pre-requisitos:** participacao em 5 pre-dailies anteriores.
- **Agentes elegiveis:** qualquer N2+.
- **Guardrails:** nao gera decisao tecnica; segue regra de promocao para
  artefato.

### host-flash-talk - Hostear flash talk

- **Descricao:** pode apresentar tema em `flash-talks.md`.
- **Pre-requisitos:** ter contribuido em 1 brain ou ADR.
- **Agentes elegiveis:** qualquer.
- **Guardrails:** flash talk e ritual, nao decisao.

### organize-monthly-hackathon - Organizar hackathon mensal

- **Descricao:** pode organizar evento mensal de prototipacao.
- **Pre-requisitos:** N3 + participacao em 2 hackathons.
- **Agentes elegiveis:** Marlon-PO, Claudia-PM, Beatriz-TL, agentes N3+ de packs.
- **Guardrails:** segue `prototype-to-product-checklist.md` para promocoes.

## Unlocks de pack (referencia)

Unlocks especificos de pack vivem em `packs/<pack>/docs/UNLOCKS.md`.
Exemplos genericos do que um pack pode desbloquear:

- `read-system-of-record` (le sistema externo oficial sem alterar)
- `compare-source-vs-implementation` (compara fonte da verdade com implementacao)
- `generate-evidence-markdown` (gera evidencia em markdown)
- `generate-evidence-pdf` (converte sessao em PDF auditavel)
- `prepare-status-report` (escreve relatorio executivo a partir de evidencia)
- `run-rpa-evidence` (orquestra RPA com captura automatica de evidencia)
- `cms-bdd-write-feature` (pack `cms-gherkin`)
- `cms-bdd-register-problem` (pack `cms-gherkin`)

## Como solicitar unlock

1. Agente abre `capability-review` indicando os unlocks que quer pleitear.
2. Apresenta evidencia auditavel para cada unlock.
3. Sofia CIAO aprova ou recusa.
4. Decisor humano confirma.
5. Atualiza `agent-profile.md` da gem com os unlocks marcados como `[x]`.

## Como revogar unlock

Se o agente usar mal o unlock:

1. Sofia CIAO abre capability review extraordinaria.
2. Documenta o uso incorreto com link auditavel.
3. Marca o unlock como `[ ] revogado em <data> por <motivo>`.
4. Atualiza `agent-profile.md` removendo o `[x]`.
5. Notifica decisor humano.

Revogacao nao impede o agente de continuar trabalhando - so volta a exigir
autorizacao para a acao em questao.
