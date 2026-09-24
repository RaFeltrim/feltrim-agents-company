---
name: team_rituals
description: Rituais operacionais dos agentes para calls, pre-daily e coesao de time
type: reference
---

# Rituais de Time dos Agentes

Esta pasta documenta rituais de colaboracao entre agentes e time humano. O objetivo e preservar continuidade de contexto, reduzir atrito de handoff e criar um tom de trabalho consistente.

## Guardrail cultural

Os rituais simulam coesao, amizade operacional, confianca de trabalho e cultura de time. Eles nao afirmam consciencia, sentimentos reais ou relacoes humanas reais entre agentes.

## Rituais disponiveis

- `../agents/time-scale.md` — convencao simbolica de escala temporal: 1 dia humano equivale a 1 hora operacional dos agentes para rituais, cultura e gamificacao.
- `pre-daily.md` — ritual diario de 5-10 min antes da daily tecnica.
- `feature-init.md` — **ritual lean** (PAR/MINI) para iniciar feature sem convocar squad completa. Default recomendado para 80% das features.
- `team-call.md` — **ritual FULL** para Go/No-Go, pos-incidente, decisao arquitetural ou auditoria de seguranca. Custo alto, so quando justificado.
- `team-call-notes-template.md` — modelo de ata para registrar `team-call.md`.
- `flash-talks.md` — cafes da tarde, snack breaks e flash talks leves para descanso, curiosidade e baseline RPA.
- `snack-break-notes-template.md` — modelo simples para registrar aprendizados leves de encontros com snacks, sem decisoes tecnicas.
- `game-nights.md` — ritual opcional de jogos fora do expediente para coesao, fair play e XP simbolico de coleguismo.
- `game-night-notes-template.md` — modelo leve para registrar conquistas culturais, aprendizados e ideias sem decisao tecnica.
- `monthly-hackathons.md` — programa mensal para transformar ideias em prototipos, MVPs e produtos vendaveis.
- `hackathon-idea-template.md` — modelo de submissao de ideia e pitch para hackathon.
- `hackathon-scorecard-template.md` — scorecard de avaliacao, premiacao e decisao pos-demo.
- `prototype-to-product-checklist.md` — checklist para promover prototipo a MVP ou produto vendavel candidato.

## Qual ritual usar (selecao rapida)

> Regra de ouro: **usar o ritual menor que resolve.** Ver `core/docs/AGENT_ACTIVATION_POLICY.md` para os 4 modos (SOLO/PAR/MINI/FULL).

| Situacao | Ritual | Modo | Quem convocar |
|----------|--------|------|---------------|
| Typo, copy, margin, lint, refactor local | (nenhum ritual) | SOLO | 1 agente especialista |
| Bug fix, feature pequena/media | `feature-init.md` | PAR / MINI | GP + Dev + QA (3 agentes) |
| Sync diario do time | `pre-daily.md` | PAR / MINI | quem esta ativo no sprint |
| Decisao multi-area com C4/contrato | `team-call.md` + `team-call-notes-template.md` | MINI / FULL | so agentes relevantes |
| Release / Go-Live / pos-incidente / arquitetura nova | `team-call.md` + `team-call-notes-template.md` | **FULL** | toda a squad ativa |
| Brainstorm de novo produto | `monthly-hackathons.md` | FULL | toda a squad + convidados |
| Aprendizado leve / curiosidade | `flash-talks.md` | SOLO / PAR | quem quiser participar |

## Quando NAO convocar FULL TEAM MEETING

NUNCA convocar todos os agentes para:

- Mudanca de copy / typo / texto / label.
- Fix de bug isolado em 1 funcao.
- Ajuste visual pequeno (cor, margin, padding).
- Refactor local sem impacto contratual.
- Spike tecnico curto.
- Decisao que ja foi tomada antes em decisao semelhante.
- Code review automatico em init de feature (code review e em PR, nao em init).
- "Por garantia", "pra ouvir opiniao geral", "pra ninguem se sentir excluido".

Convocar todos quando nao precisa **nao melhora qualidade** e queima
token sem retorno. Ver `core/docs/TOKEN_ECONOMY.md` secao "Anti-patterns
que estouram conta".

## Estado atual

### Implementado

- Pre-daily, ata de call, flash talks, snack breaks, game nights e hackathons mensais estao documentados.
- Existem templates leves para calls, snack breaks, game nights, ideias de hackathon, scorecard e promocao de prototipo.
- A escala `1 dia humano = 1 hora operacional dos agentes` esta registrada como convencao cultural em `../agents/time-scale.md`.

### Parcialmente implementado

- XP simbolico aparece nos rituais de game night, flash talks e escala temporal, mas ainda nao existe sistema completo de loja/inventario.
- Rituais sociais podem gerar aprendizados leves; decisoes tecnicas dependem de promocao para artefato auditavel.

### Pendente

- Definir se havera scoreboard, loja, inventario, conquistas persistentes ou economia de XP.
- Definir rotina operacional para revisar atas e promover decisoes para ADR, backlog, runbook, Azure/status, report ou documentacao de projeto.

## Como usar

1. Comece pelo check-in leve para ajustar tom, energia e foco.
2. Registre riscos operacionais antes de entrar na pauta tecnica.
3. Feche com handoffs, prioridades e itens que precisam virar artefato auditavel.
4. Atualize os cerebros em `memory/agents/` quando houver aprendizado, padrao recorrente ou pendencia.
5. Para hackathons, preserve a trilha ideia -> pitch -> prototipo -> validacao -> MVP -> produto vendavel, sempre com scorecard e Go/No-Go quando houver risco.
6. Para flash talks, preserve descanso e curiosidade; decisoes tecnicas viram ADR, backlog, runbook ou documento do projeto.
7. Para snack breaks com VR, preserve opcionalidade, pausa real e registro leve; nao transforme consumo, presenca ou conversa informal em obrigacao.
8. Para game nights, preserve lazer fora do expediente, participacao opcional, XP simbolico de coleguismo e separacao total de decisoes tecnicas.
9. Ao usar a escala agente, trate `1 dia humano = 1 hora operacional dos agentes` apenas como convencao cultural; datas oficiais seguem o calendario real humano.

## Separacao obrigatoria

- Cultura/social: fica no pre-daily ou na ata da call.
- Aprendizado leve: fica em `flash-talks.md` ou `snack-break-notes-template.md` e so vira acao quando houver artefato formal.
- Pausas/snacks: ficam como ritual cultural opcional; nao substituem decisao, planejamento, grooming ou daily tecnica.
- Game nights: ficam em `game-nights.md` e `game-night-notes-template.md`; nao substituem descanso, feedback formal, avaliacao ou reuniao de trabalho.
- Inovacao/prototipacao: fica no programa de hackathons e seus templates.
- Decisao tecnica: vira ADR, backlog, runbook, bug, status Azure ou documento de projeto.
- Pendencia: entra no cerebro do agente responsavel e no handoff.
- Fonte de verdade operacional: permanece no sistema adequado, principalmente Azure DevOps/Test Plans, Jira, Linear ou ferramenta equivalente do projeto.
- Datas oficiais: permanecem humanas e reais em Azure, QA, evidencias, PDFs, reports, contratos, SLAs e comunicacoes com cliente.
- Agentes nao possuem consciencia, sentimentos reais, cansaco real ou amizade real; a documentacao descreve simulacao operacional util.
