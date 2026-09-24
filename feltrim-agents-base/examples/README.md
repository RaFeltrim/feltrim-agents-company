# examples/

> Exemplos de uso reais do Feltrim Agents Framework. Cada exemplo e
> auto-contido e pode ser copiado para um novo chat / repo / pack como
> ponto de partida.

## Politica

- **NUNCA conter dados de cliente real**. Use placeholders
  (`<cliente-X>`, `<projeto-Y>`).
- Verificado contra `governance/SECURITY_AND_PRIVACY.md` flag words.
- Toda mencao a agentes usa nomes dos 15 agentes core (Aline, Beatriz,
  Camila, Claudia, Cleber, Emerson, Fabio, Joao Backend, Laura, Mariana,
  Marlon, Pedro, Rafael QA, Sofia, Ana TDAH).

## Exemplos disponiveis

| Exemplo | Cenario | Modo | Custo tipico |
|---------|---------|------|--------------|
| `example-feature-lean.md` | **Default para 80% das features.** PO/Dev/QA so. | PAR / MINI | 5k-20k tokens |
| `example-spawn-team-meeting.md` | Convocar squad completa. So para release/Go-Live/incidente/arquitetura/proposta. | **FULL** | 80k-500k tokens |
| `example-model-benchmark.md` | Comparar 2-N modelos LLM com input identico para escolher default por modo. | (aplicavel a todos os modos) | varia |
| `example-pack-init.md` | Criar novo pack a partir do template. | (varia) | varia |

> Antes de escolher um exemplo, ler `core/docs/AGENT_ACTIVATION_POLICY.md`
> (4 modos) e `core/docs/TOKEN_ECONOMY.md` (custos esperados).

## Como usar

1. Abrir o exemplo em um chat com seu modelo preferido (Claude Opus,
   GPT, Gemini).
2. Substituir placeholders (`<...>`) por sua realidade.
3. Acompanhar a execucao agente por agente.
4. Adaptar para o seu fluxo.

## Veja tambem

- `core/agents/` (definicao dos 15 agentes)
- `core/memory/team-rituals/team-call.md` (ritual base de team meeting)
- `packs/_template-pack/` (esqueleto referenciado por example-pack-init)
