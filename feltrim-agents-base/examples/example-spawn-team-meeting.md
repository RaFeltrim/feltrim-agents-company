# Exemplo: spawn team meeting (modo FULL)

> Como convocar um time multi-perspectiva para revisar um artefato
> (proposta, arquitetura, plano, codigo, decisao).
>
> **AVISO de custo:** este e o modo **FULL** (modo 4 de
> `core/docs/AGENT_ACTIVATION_POLICY.md`), o mais caro em token.
> **Use apenas** para release/Go-Live, pos-incidente critico, mudanca
> arquitetural relevante, hackathon/kickoff, auditoria periodica ou
> proposta executiva.
>
> Para **80% das features** (small/medium development), use
> `example-feature-lean.md` (modo PAR/MINI). Convocar full team em
> mudanca simples queima 5-10x mais token sem agregar valor.

## Cenario

Voce tem um artefato em `<caminho/do/artefato>` (proposta, ADR,
arquitetura, schema, prompt, plano de teste, etc) e quer **opiniao
multi-perspectiva** antes de aprovar, e a tarefa se encaixa nos triggers
de modo FULL abaixo.

## Triggers que justificam modo FULL

Antes de seguir, confirme que esta em **pelo menos um** destes casos:

- [ ] Release / Go-Live decision (versao production-ready)
- [ ] Pre-deploy de mudanca arquitetural relevante
- [ ] Pos-incidente critico (post-mortem)
- [ ] Hackathon / Kickoff de projeto novo
- [ ] Auditoria periodica de capability/promotion
- [ ] Revisao de proposta executiva
- [ ] Decisao estrategica multi-vertical (trocar stack do projeto)

Se nao marcou nenhum: pare. Use `example-feature-lean.md`.

## Pre-requisitos

- Cursor / Claude Code / Codex / Gemini IDE com este repo aberto.
- Leitura de `core/CLAUDE.md` e `core/docs/SQUAD_INDEX.md` no contexto.
- Artefato a ser revisado salvo em algum lugar acessivel.

## Prompt

```text
Quero convocar um team meeting para revisar o artefato em
`<caminho/do/artefato>`.

Por favor:

1. Ler `core/CLAUDE.md` para boot do framework.
2. Ler `core/docs/SQUAD_INDEX.md` para conhecer a squad.
3. Ler `core/memory/team-rituals/team-call.md` para o ritual.
4. Ler o artefato em `<caminho/do/artefato>`.
5. Identificar quais agentes core sao relevantes para a revisao deste
   artefato especifico (ex: ADR de arquitetura -> Aline + Beatriz +
   Sofia + Camila; proposta executiva -> Sofia + Marlon + Claudia +
   Pedro; UI -> Laura + Cleber + Ana TDAH + Fabio).
6. Para cada agente selecionado:
   - Carregar a gem completa em `core/agents/gem_<slug>.md`.
   - Produzir revisao em formato:
     - Quem (papel + nivel atual ver `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md`)
     - Veredito (APROVA / APROVA COM RESSALVA / REPROVA / BLOQUEIA)
     - Pontos fortes
     - Pontos a corrigir (acionavel)
     - Bloqueios (se houver)
     - Promocao de chat para artefato? (ver `core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`)
7. Consolidar como um team-call report em formato markdown.
8. Identificar quais pontos viram artefato oficial (issue, ADR, bug,
   PR) e quais ficam como nota informativa.
9. Sofia CIAO faz veredito final consolidando.

Premissas:
- Cada agente fala APENAS dentro do seu escopo (Aline NAO opina de UI;
  Laura NAO opina de C4 diagram).
- Conflitos entre agentes sao explicitados, nao mascarados.
- Decisao final fica com o decisor humano (eu); agentes recomendam.

Atencao a guardrails:
- `governance/RITUALS_GUARDRAILS.md` (XP/ritual e simbolico)
- `governance/SECURITY_AND_PRIVACY.md` (sem flag words em outputs)
```

## O que esperar

O resultado vai ter:

1. Lista de agentes convocados com justificativa.
2. Revisao individual de cada agente (3-6 paragrafos cada).
3. Pontos consolidados em 4 colunas (Forte / Corrigir / Bloqueio /
   Ressalva).
4. Veredito Sofia CIAO (`APROVADO` / `APROVADO COM RESSALVA` /
   `REPROVADO` / `BLOQUEADO`).
5. Lista do que vira artefato oficial vs nota.
6. Recomendacao acionavel para o decisor humano.

## Exemplo real (sanitizado)

O pack `packs/us-avaliator/` traz um caso real onde 14 agentes
revisaram a `Proposta_Substituicao_Copilot.md` simultaneamente.

Cada `agent-reports/relatorio_<slug>.md` mostra como cada agente
estruturou sua propria revisao seguindo este padrao.

## Veja tambem

- `core/docs/AGENT_ACTIVATION_POLICY.md` - quando usar FULL vs outros modos
- `core/docs/TOKEN_ECONOMY.md` - quanto custa cada modo
- `core/memory/team-rituals/feature-init.md` - alternativa lean (PAR/MINI)
- `core/memory/team-rituals/team-call-notes-template.md` - ata para registrar
- `core/memory/team-rituals/monthly-hackathons.md` - hackathon trigger de FULL
- `packs/us-avaliator/` - case de team meeting completo (proposta executiva)
- `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md` - criterio de promocao
  baseado em outputs como este
- `examples/example-feature-lean.md` - exemplo PAR/MINI para o resto
