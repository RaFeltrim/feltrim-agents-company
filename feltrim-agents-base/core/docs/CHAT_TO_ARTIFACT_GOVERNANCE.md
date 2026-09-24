# Chat to Artifact Governance

> Regra canonica de promocao: decisoes nascidas em conversa de chat, pre-daily,
> ritual social ou flash talk NUNCA viram fonte oficial. Toda decisao
> auditavel migra para um artefato apropriado.
>
> Politica generalizada de promocao chat -> artefato.

## Principio

```text
Chat nao e fonte final. Chat gera decisao candidata.
Decisao candidata vira artefato conforme impacto.
```

Sem promocao, decisao some quando a conversa rolar. Decisao auditavel exige
endereco fixo.

## Tabela de promocao

| Tipo de decisao candidata | Destino auditavel | Responsavel pela promocao |
|--------------------------|-------------------|---------------------------|
| Criterio de QA (passou / falhou / ressalva) | `core/docs/` (se generico) ou `packs/<pack>/docs/` (se de pack) ou `.cursor/rules/<rule>.mdc` ou `core/skills/<skill>/SKILL.md` | QA orchestrator do pack ou Rafael-QA |
| Aprendizado especifico de um agente | `core/memory/agents/<slug>/brain.md` ou `packs/<pack>/brains/<slug>/brain.md` | A propria gem ao final da tarefa |
| Ritual ou pratica cultural | `core/memory/team-rituals/` | Quem facilitou o ritual |
| Decisao tecnica irreversivel | `core/docs/adr/ADR-CORE-NNN.md` ou `packs/<pack>/adr/ADR-<PACK>-NNN.md` | Beatriz-TL ou Sofia-CIAO |
| Decisao tecnica reversivel mas com escopo | runbook em `core/docs/runbooks/` ou `packs/<pack>/runbooks/` | Camila-DevOps ou agente responsavel |
| Bug / CT / status de execucao | Sistema externo (Azure DevOps, Jira, Linear, GitHub Issues) + evidencia em `packs/<pack>/evidence/` (se aplicavel) | QA do pack + agente de status do pack |
| Backlog / story / prioridade | Sistema externo de gestao + `packs/<pack>/docs/BACKLOG.md` se houver | Marlon-PO + Claudia-PM |
| Mudanca de prompt de agente | `core/agents/gem_*.md` (versao canonica) | Sofia-CIAO + Mariana-Prompt + decisor humano |
| Mudanca de protocolo | `core/protocols/*.md` | Sofia-CIAO + decisor humano (sempre) |
| Mudanca de governanca | `governance/*.md` | Sofia-CIAO + decisor humano (sempre) |
| Mudanca de hierarquia | `governance/AGENT_HIERARCHY.md` | Decisor humano apenas |
| Mudanca de licenca | `LICENSE` | Decisor humano apenas |

## Gatilhos para promocao obrigatoria

Promova IMEDIATAMENTE quando a decisao:

- muda arquitetura, fluxo, criterio de QA, status oficial, backlog ou
  contrato entre sistemas;
- afeta custo, seguranca, dados, release, evidencias, rastreabilidade ou
  go/no-go;
- precisa ser encontrada por alguem que nao participou da conversa;
- sera cobrada no futuro por decisor humano, cliente, QA, auditoria ou
  operacao;
- afeta mais de um agente (cria handoff ou dependencia);
- contradiz um artefato ja existente (atualizar o artefato OU criar ADR de
  supersede).

## Anti-padroes (NAO fazer)

- Deixar criterio de aceite combinado apenas no pre-daily.
- Marcar bug como "resolvido" apenas com print em chat, sem evidencia
  auditavel.
- Aprovar arquitetura por "todos concordaram na flash talk".
- Mudar prompt de gem sem PR e sem aprovacao da Sofia-CIAO.
- Documentar regra de negocio apenas no brain do agente que aprendeu
  (precisa promover para artefato visivel para o time).
- Usar XP / badge / ritual como justificativa para promover capacidade do
  agente (XP e simbolico; capability review e auditavel).

## Como promover (passo a passo)

1. **Reconhecer**: durante o ritual/chat, marcar a decisao candidata em voz
   alta ("isso aqui vai virar ADR" / "isso vai pro brain do agente X").
2. **Identificar destino**: usar a tabela de promocao para escolher o
   artefato correto.
3. **Escrever**: criar/atualizar o artefato com link de origem (data do
   chat, participantes, contexto).
4. **Linkar**: no artefato antigo (se houver), apontar para o novo.
5. **Notificar**: agente cujo brain mudou, decisor humano se a promocao
   afeta governanca, time se a promocao afeta processo.
6. **Verificar**: na proxima daily, validar que a promocao foi feita e o
   artefato esta acessivel.

## Quem promove

Cada categoria de decisao tem responsavel default (ver tabela acima).
Quando nao houver responsavel claro:

- Sofia-CIAO promove decisoes de governanca / arquitetura / risco.
- A gem mais especializada promove decisoes da sua area.
- Em duvida, o agente orquestrador do chat promove e atribui revisor.

## Quando NAO promover

- Conversas puramente sociais (snack break, game night cumulative score, XP).
- Curiosidade tecnica sem implicacao em projeto real (flash talk sobre
  paper academico).
- Brainstorming sem decisao consolidada (so promove quando convergiu).
- Sentimento/tom (vive no pre-daily, nao no artefato).

## Auditoria

Sofia-CIAO faz revisao mensal de:

- Quantas promocoes foram feitas no mes.
- Quantas decisoes candidatas ficaram sem promocao (lacuna grave).
- Quantos artefatos perdidos surgiram (sintoma de promocao mal feita).

Resultado vai para `core/memory/team-rituals/monthly-hackathons.md` no proximo
hackathon, como retro.

## Veja tambem

- `core/protocols/MEMORY_AND_RAG_POLICY.md` - quando gravar / recuperar
- `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md` - promocao de agentes
- `core/memory/team-rituals/README.md` - separacao cultural vs tecnico
- `governance/RITUALS_GUARDRAILS.md` - cultura simbolica != metrica real
