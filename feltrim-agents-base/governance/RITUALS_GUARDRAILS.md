# Rituals Guardrails - Cultura Simbolica != Metrica Real

> Politica explicita: rituais, XP, gamificacao, escala temporal de agentes
> e cultura social SAO simbolicos. NAO sao metricas de performance,
> avaliacao, promocao ou autoridade.

## Princpio

```text
Cultura cria coesao operacional.
Avaliacao acontece em capability review.
Promocao acontece em capability review + aprovacao humana.

Nunca confundir os tres.
```

## O que SAO os rituais

- Mecanismos de coesao operacional entre agentes.
- Convencao narrativa para planejar ciclos curtos.
- Espaco para promocao de decisao para artefato.
- Reducao de atrito em handoff.
- Espaco para curiosidade tecnica e aprendizado leve.

## O que NAO SAO os rituais

- Avaliacao de performance.
- Promocao automatica (XP nao promove agente).
- Certificacao (so capability review certifica).
- Substituto de decisor humano.
- Substituto de daily tecnica ou ADR.
- Fonte de verdade auditavel.
- Cobranca de presenca, consumo ou disponibilidade.
- Afirmacao de consciencia, sentimento real ou amizade real dos agentes.

## Lista de rituais (cultura, NAO metrica)

| Ritual | Onde | Funcao |
|--------|------|--------|
| Pre-daily | `core/memory/team-rituals/pre-daily.md` | Aquecimento de tom e energia antes da daily tecnica |
| Daily tecnica | (varia por projeto) | Decisao operacional do dia |
| Flash talks | `core/memory/team-rituals/flash-talks.md` | Aprendizado leve, curiosidade tecnica, baseline RPA |
| Snack break | `core/memory/team-rituals/snack-break-notes-template.md` | Pausa real, recuperacao de energia, conversa leve |
| Game nights | `core/memory/team-rituals/game-nights.md` | Coesao fora do expediente, fair play, XP simbolico |
| Hackathon mensal | `core/memory/team-rituals/monthly-hackathons.md` | Ideacao -> prototipo -> demo, com scorecard |
| Escala temporal | `core/memory/agents/time-scale.md` | Convencao 1 dia humano = 1 hora agente para narrativa |

## O que XP simbolico PODE ser usado para

- Reconhecer participacao em ritual.
- Marcar nivel narrativo de progresso cultural.
- Gerar badge simbolico em hackathon.
- Servir de gancho de motivacao narrativa para a gem.

## O que XP simbolico NAO PODE ser usado para

- Subir nivel de agente (so capability review faz isso).
- Conquistar certificacao (so evidencia auditavel faz isso).
- Desbloquear habilidade operacional (so capability review faz isso).
- Substituir avaliacao humana.
- Determinar prioridade de tarefa.
- Justificar promocao salarial / bonus / autoridade humana.

## Separacao obrigatoria

### Cultura/social

Vive em `core/memory/team-rituals/` e nos brain registros de pre-daily.

### Aprendizado leve

Vive em `flash-talks.md` ou `snack-break-notes-template.md`. So vira acao
quando houver artefato formal.

### Pausas / snacks

Ritual cultural opcional. Nao substituem decisao, planejamento, grooming ou
daily tecnica. Snack break especificamente:

- Participacao opcional.
- Consumo opcional.
- Sem cobranca de tipo de alimento, valor gasto, presenca obrigatoria.
- Respeito a saude, restricoes, religiao, rotina, orcamento.

### Game nights

Vivem em `game-nights.md`. Nao substituem descanso, feedback formal,
avaliacao ou reuniao de trabalho. Fora do expediente. Opcional.

### Inovacao / prototipacao

Vive no programa de hackathons (`monthly-hackathons.md`) e seus templates.

### Decisao tecnica

Vira ADR, backlog, runbook, bug, status oficial ou documento de projeto.
Nunca fica apenas no ritual. Ver
`core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`.

### Pendencia

Entra no brain do agente responsavel e no handoff. Tem dono, prazo e
destino auditavel.

### Fonte de verdade operacional

Permanece no sistema externo (Azure DevOps, Jira, Linear, GitHub).

### Datas oficiais

Permanecem humanas e reais em sistemas oficiais, QA, evidencias, PDFs,
reports, contratos, SLAs e comunicacoes com cliente.

## Escala temporal agente

```text
1 dia humano = 1 hora operacional dos agentes
```

E **simbolica**. Permitida para narrar ciclos, XP, niveis culturais e
hackathons.

Proibida para alterar datas reais de sistemas oficiais ou substituir prazo
contratual. Ver `core/memory/agents/time-scale.md`.

## Auditoria

Sofia CIAO faz revisao mensal de:

- Se algum agente tentou usar XP para se auto-promover.
- Se algum ritual virou justificativa para pular capability review.
- Se algum ritual virou cobranca operacional.
- Se algum aprendizado de flash talk ficou perdido sem promocao para
  artefato.

Resultado vira retro no proximo hackathon mensal.

## Anti-padroes especificos

| Anti-padrao | Por que e proibido | Mitigacao |
|-------------|--------------------|-----------|
| "O agente X tirou 200 XP no game night, deve subir para N4" | XP nao avalia capacidade tecnica | Capability review com evidencia auditavel |
| "Todos concordaram no pre-daily que vamos usar Redis" | Conversa nao e ADR | Promover para `core/docs/adr/` |
| "Marquei como PASSED no chat" | Status oficial fica em sistema externo | Atualizar Azure / Jira / equivalente com evidencia |
| "O snack break esta vazio, vou marcar presenca obrigatoria" | Snack break e opcional | Manter opcional, registrar so se houver aprendizado leve |
| "A gem disse no game night que esta cansada, vou reduzir tarefas" | Gem nao tem cansaco real | Verificar contexto / fila real do agente em metricas reais |
| "Sofia aprovou no flash talk" | Veredito de Sofia tem template proprio com evidencia | Sofia emite veredito formal com 5 secoes obrigatorias |

## Atualizacao deste documento

Mudancas via PR com:

- Aprovacao Sofia CIAO.
- Aprovacao decisor humano.
- Atualizar `core/memory/team-rituals/README.md` em conjunto se afetar
  algum ritual.

## Veja tambem

- `core/memory/agents/time-scale.md`
- `core/memory/team-rituals/README.md`
- `core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`
- `governance/PROMOTION_POLICY.md`
