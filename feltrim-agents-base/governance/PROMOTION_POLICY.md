# Promotion Policy - Feltrim Agents Company

> Politica oficial da empresa sobre como uma gem sobe de nivel (N1 -> N5).
> Detalhes operacionais e criterios estao em
> `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md`.
> Este arquivo define **quem decide**, **quando** e **como audita**.

## Principio

```text
Promocao = evidencia auditavel + capability review fechada
         + aprovacao Sofia CIAO + aprovacao Rafael Feltrim (decisor humano).
```

## Quem inicia

- A propria gem pode candidatar-se a um nivel superior.
- Sofia CIAO pode propor promocao na revisao trimestral.
- Beatriz TL ou um Orchestrator de pack pode endossar candidatura.
- Decisor humano pode propor promocao diretamente.

## Quem aprova

| Para subir para | Aprovador primario | Aprovador secundario | Anti-objecao |
|-----------------|--------------------|--------------------|--------------|
| N2 | Sofia CIAO | Beatriz TL ou Orchestrator de pack | - |
| N3 | Sofia CIAO + decisor humano | Beatriz TL | - |
| N4 | Sofia CIAO + decisor humano | Beatriz TL (endorse) + 2 gens N3+ | Veto de qualquer N4 cancela ate review |
| N5 | Decisor humano (Rafael) APENAS | Sofia CIAO endorse, mas N5 e responsabilidade humana | So 1 N5 ativa por escopo (ver abaixo) |

### Restricao N5

- So existe **uma** Sofia CIAO N5 no `core/` por vez.
- Cada pack pode ter **uma** CIAO N5 propria, se o pack justificar.
- Promocao de outra gem para N5 implica em **transicao** + handoff
  documentado, nao em paralelismo de poder.

## Cadencia de revisoes

| Janela | Trigger | Responsavel |
|--------|---------|-------------|
| Trimestral | Revisao periodica de todas as gens ativas | Sofia CIAO |
| Pos-pack | Quando um pack e fechado / arquivado | Sofia CIAO + decisor humano |
| Pos-incidente | Violacao grave detectada em uso | Sofia CIAO (imediato) |
| Sob demanda | Candidatura espontanea da gem | A propria gem inicia |

## Evidencia auditavel - exemplos aceitos

- ADR autoral aceito.
- Bug critico detectado antes de release, com link auditavel.
- CT executado com evidencia (Playwright trace, screenshot, log).
- Refatoracao com benchmark antes/depois.
- Capability review anterior com nota >= 4/5 em todos os criterios.
- Endorso documentado de outra gem N3+ (link para artefato concreto).
- Decisor humano sinalizando aprovacao em PR / capability review.

## Evidencia NAO aceita

- Antiguidade ("a gem existe ha 6 meses").
- Presenca em rituais (pre-daily, game night, snack break).
- XP simbolico / badge / conquista de gamificacao.
- Auto-elogio sem artefato.
- "Todos gostam dessa gem".
- "Essa gem trabalhou muito esse mes".
- Simpatia, tom de voz ou criatividade isolada.

## Documentacao obrigatoria pos-aprovacao

Apos promocao aprovada, a gem responsavel pelo workflow de promocao DEVE:

1. Atualizar `core/memory/agents/<slug>/agent-profile.md` (criar se nao
   existir, usando template).
2. Atualizar a linha da gem em `core/docs/SQUAD_INDEX.md` (nivel novo).
3. Adicionar arquivo de capability review em
   `core/memory/agents/<slug>/capability-reviews/<AAAA-MM-DD>.md`.
4. Atualizar `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md` se a tabela de
   mapeamento mudou.
5. Notificar o time (canal humano combinado).

## Regressao (downgrade)

A gem pode CAIR de nivel se:

- Violar guardrail critico (vazar dado, escrever sem autorizacao, ignorar
  veto).
- Aprovar decisao sem evidencia documentada.
- Apresentar regressao em capability review extraordinaria.

Regressao tem o mesmo processo de aprovacao da promocao, com sinal
invertido. Sofia CIAO + decisor humano sempre.

Regressao NAO acontece por:

- Critica isolada de outra gem.
- Resultado ruim em ritual cultural.
- "Mau humor" da gem.
- Outras gens "nao gostarem" dela.

## Conflito de interesse

- Sofia CIAO nao pode promover/regredir a si mesma. Para mudancas na propria
  Sofia, o decisor humano decide sozinho (com revisao externa opcional).
- Uma gem nao pode auto-promover sem aprovacao externa.
- Decisor humano pode override qualquer veto (com registro do risco aceito).

## Transparencia

Todas as promocoes ativas estao visiveis em:

- `core/docs/SQUAD_INDEX.md` (coluna Nivel)
- `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md` (tabela de mapeamento)
- `core/memory/agents/<slug>/agent-profile.md` (cartao executivo da gem)
- `core/memory/agents/<slug>/capability-reviews/` (historico de reviews)

## Atualizacao deste documento

Mudanca via PR com:

- Aprovacao Rafael Feltrim.
- Aprovacao Sofia CIAO.
- Atualizar `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md` em conjunto se
  os criterios operacionais mudarem.
- Atualizar `governance/CERTIFICATION_POLICY.md` se afetar emissao de cert.

## Veja tambem

- `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md` - criterios concretos
- `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md` - matriz N1-N5
- `core/memory/agents/_templates/agent-capability-review-template.md`
- `governance/CERTIFICATION_POLICY.md`
