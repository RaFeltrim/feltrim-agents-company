# Core Integrations (esqueletos genericos)

Contratos genericos para integracoes que o framework pode consumir. Cada
subpasta tem um README descrevendo o contrato (variaveis de ambiente,
endpoints esperados, formato de payload).

Integracoes especificas da empresa (ex.: instancias self-hosted, contas
proprias) ficam em `packs/<pack>/integrations/` em repositorio privado.

## Integracoes disponiveis (skeleton)

- `openclaw/` - bridge de chat (WhatsApp/Telegram) para LLM via daemon
  self-hosted, model-agnostic.
- `n8n/` - automation runner; preferir self-hosted via Docker Compose +
  reverse proxy para liberar `Execute Command`.
- `obsidian/` - navegacao pessoal de memoria/cerebros do agente. Nao e
  fonte de verdade transacional; e leitor de markdown.
- `pixel-agents/` - extensao de IDE/CLI para invocacao rapida de agentes.

## Contrato comum

Toda integracao traz um README com:

1. **Proposito** - o que essa integracao resolve.
2. **Pre-requisitos** - servico externo necessario, versao minima, conta.
3. **Variaveis de ambiente** - secrets vao para `.env` (nunca aqui).
4. **Como o agente invoca** - exemplo de payload de request/response.
5. **Limites** - rate limits, timeouts, falhas conhecidas.
6. **Falhar graciosamente** - o que fazer quando a integracao esta offline.

## Como adicionar uma nova integracao

1. Criar `core/integrations/<nome>/README.md` com o contrato acima.
2. Adicionar variaveis de ambiente em `.env.example` da raiz.
3. Documentar no `core/docs/ARQUITETURA.md` quem usa essa integracao.
4. Se a integracao precisar de instancia interna da empresa adotante,
   criar tambem `packs/<empresa>-internal/integrations/<nome>/` em
   repositorio privado.
