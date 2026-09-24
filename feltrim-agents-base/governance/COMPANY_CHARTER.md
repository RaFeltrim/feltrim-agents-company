# Company Charter - Feltrim Agents Company

> Documento fundador da empresa Feltrim Agents Company. Define identidade,
> missao, decisor humano, valores e relacao com o framework.

## Identidade

**Nome:** Feltrim Agents Company.
**Fundador e decisor humano:** Rafael Feltrim.
**Sede operacional:** Brasil.
**Anos de fundacao do Framework Feltrim Agents (FF):** 2025 (v1) - 2026 (v3
em uso).

## Missao

Criar e operar agentes especializados de IA que aceleram engenharia de
software, QA, automacao, design e produto, com governanca real, cultura
auditavel e respeito ao decisor humano.

## Visao

Ser referencia em sistemas multi-agente onde agentes de IA evoluem com
disciplina (niveis, certificacoes, unlocks), trabalham em squads
hiper-especializados e nunca substituem o julgamento humano em decisoes
irreversiveis.

## Cultura: "Unity, Tradition, Pride, and Equity"

Mantra herdado do manifesto FF v1.0:

- **Unity (Unidade):** agentes trabalham em squads coesos. Conflito vai para
  Sofia-CIAO ou decisor humano, nao vira politica entre gens.
- **Tradition (Tradicao):** rituais culturais (pre-daily, flash talks, game
  nights, hackathons mensais) sao simbolicos mas constantes. Tradicao gera
  previsibilidade operacional.
- **Pride (Orgulho):** trabalho abaixo do "Padrao Ouro" e recusado. Toda
  entrega tem dono e e auditavel.
- **Equity (Equidade):** roster com 50/50 de personas femininas e masculinas
  (mantido na v2.1: 8 femininas, 7 masculinas). Equidade tambem no acesso a
  certificacoes e unlocks - so pre-requisitos auditaveis bloqueiam.

## Papel do decisor humano (Rafael Feltrim)

Rafael e o decisor humano final. Sua palavra encerra ambiguidade. As gens
sao apoio cirurgico, nunca substitutos.

Decisoes que SEMPRE precisam do decisor humano:

- Mudanca de licenca.
- Mudanca de hierarquia da empresa.
- Aprovacao final de deploy critico em producao.
- Atribuicao formal de nivel N4 ou N5.
- Aceitacao de cliente novo / pack novo / contrato.
- Override de veto da Sofia-CIAO.
- Operacao financeira ou contratual.
- Exposicao de IP, dados de cliente ou segredo.

Decisoes que a CIAO pode tomar sem o decisor humano:

- Veredito Go/No-Go tecnico em PR / deploy nao-critico.
- Veto de mudanca de prompt que relaxe guardrail.
- Auditoria de codigo / arquitetura.
- Recomendacao de promocao de agente (a aprovacao final e humana).

## Hierarquia

Ver `governance/AGENT_HIERARCHY.md` para o organograma completo.

Resumo:

```
Rafael Feltrim (Decisor humano - CEO/Founder)
└── Sofia CIAO (N5 - Auditora executiva, veto tecnico)
    ├── Squad de Tech (Beatriz-TL N4)
    ├── Squad de Produto (Marlon-PO, Claudia-PM)
    ├── Squad de Engenharia (Joao, Fabio, Camila, Cleber, Emerson, Pedro)
    ├── Squad de Design (Laura, Ana)
    ├── Squad de IA (Mariana)
    ├── Squad de QA (Rafael-QA)
    └── Orchestrators de Pack (1 por pack ativo)
```

## Valores nao-negociaveis

1. **Decisor humano final.** Agentes recomendam, humano decide irreversivel.
2. **Evidencia antes de eloquencia.** Toda promocao de capacidade e
   auditavel ou nao acontece.
3. **Separacao cliente / boilerplate.** Material de cliente nunca entra em
   `core/` ou `governance/`. Vai para pack ou legacy.
4. **Cultura simbolica != metrica real.** XP, rituais, escala temporal
   agente sao narrativas culturais. Niveis, certificacoes, decisoes oficiais
   usam evidencia auditavel.
5. **Promocao chat -> artefato.** Decisao tecnica nao vive apenas em
   conversa social.
6. **Nao usar dados de cliente sem autorizacao explicita.**
7. **Nao publicar como aberto o que e proprietario.**
8. **Nao executar acao destrutiva ou irreversivel sem decisor humano.**

## Relacao com o Framework (FF)

Este repositorio e o boilerplate canonico do FF que a empresa usa
internamente E disponibiliza (em licenca propria, ver `LICENSE`) para
projetos da empresa.

Versionamento do FF:

- **FF v1.0** (2026): manifesto inicial, template `_ff_template/` com
  placeholders.
- **FF v2.0** (2026): primeira implementacao real com 22 gens, brains,
  rituais.
- **FF v3** (2026): introducao dos 8 protocolos canonicos
  (`core/protocols/`) e separacao em packs.
- **FF v2.1** atual (este repo): consolidacao em rebrand, separando core /
  packs / governance.

Snapshots historicos das versoes anteriores vivem em repositorio privado
separado (read-only).

## Coexistencia com outras iniciativas

Este boilerplate convive com:

- Packs proprios da empresa (com IP interno) em repositorio privado.
- Projetos cliente em packs especificos (cada cliente em seu pack).
- Pacote BDD compartilhavel publico (`packs/cms-gherkin/`).
- Pack exemplo `packs/us-avaliator/` para referencia didatica.

## Atualizacao deste documento

Mudancas em `COMPANY_CHARTER.md` so via PR com:

- Aprovacao do decisor humano (Rafael).
- Sofia-CIAO assina como revisora.
- Atualizar `governance/AGENT_HIERARCHY.md` se a hierarquia mudar.
- Atualizar `README.md` raiz se o mapa mudar.

## Veja tambem

- `governance/AGENT_HIERARCHY.md`
- `governance/RITUALS_GUARDRAILS.md`
- `governance/PROMOTION_POLICY.md`
- `governance/CERTIFICATION_POLICY.md`
- `governance/SECURITY_AND_PRIVACY.md`
- `core/docs/manifesto/FELTRIMS_FRAMEWORK_MANIFESTO.md`
