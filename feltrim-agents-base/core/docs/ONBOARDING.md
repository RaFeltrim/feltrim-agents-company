# Onboarding - Feltrim Agents Base

> Setup inicial para usar o Feltrim Agents Framework em um novo ambiente.
> Versao generica do boilerplate. Onboarding especifico de pack vive em
> `packs/<pack>/docs/ONBOARDING.md`.

## Pre-requisitos

- Node.js >= 20 LTS
- Git
- Editor com suporte a Markdown (VS Code / Cursor / Claude Code recomendado)
- Conta em pelo menos um provedor LLM (Anthropic, OpenAI, Google) para a
  API key

Opcional (quando o pack exigir):

- Docker Desktop (para integracoes self-hosted)
- Playwright + browsers (para automacoes RPA)
- Python 3.11+ (se o pack usar scripts Python)
- PostgreSQL local ou conta Supabase
- WSL2 (Windows) para rodar scripts bash do `core/scripts/`

## Checklist de setup

### 1. Estrutura

- [ ] Clone deste repositorio para uma pasta local.
- [ ] Confirme que `core/`, `packs/`, `governance/` existem e possuem
      READMEs.
- [ ] Leia `README.md` raiz para entender o mapa.
- [ ] Leia `DECISIONS_PENDING.md` para ver o que esta em aberto.

### 2. Ambiente local

- [ ] Copiar `.env.example` para `.env`:
      ```bash
      cp .env.example .env
      ```
- [ ] Preencher pelo menos uma API key de LLM provider.
- [ ] Confirmar que `.env` esta em `.gitignore` (ja esta por default).

### 3. Dependencias (quando aplicavel)

- [ ] Se o pack ativo usar Node.js: `npm install` na raiz do pack.
- [ ] Se usar Playwright: `npx playwright install chromium` (browsers).
- [ ] Se usar Python: `pip install -r requirements.txt` (no pack).

### 4. CLI / IDE

- [ ] Configure sua CLI/IDE para reconhecer `CLAUDE.md` e `AGENTS.md` da raiz.
- [ ] Confirme que a CLI consegue listar as gens em `core/agents/*.md`.
- [ ] Confirme que a CLI consegue carregar `core/memory/MEMORY.md` no boot.

### 5. Primeira invocacao (smoke test)

- [ ] Abra a CLI/IDE na raiz do repo.
- [ ] Peça para o agente listar quais gens estao disponiveis.
- [ ] Peça para o agente listar quais packs estao ativos.
- [ ] Peça uma resposta simples sobre como invocar Sofia-CIAO.
- [ ] Verifique que o agente respeita o boot sequence (carrega
      `core/protocols/AGENT_RUNTIME_WRAPPER.md`).

### 6. Pack especifico (opcional)

- [ ] Se for trabalhar em CMS-Gherkin: leia `packs/cms-gherkin/README.md`.
- [ ] Se for trabalhar em US-Avaliator: leia `packs/us-avaliator/README.md`.
- [ ] Se for trabalhar em pack proprio: leia o `README.md` do seu pack
      e o `docs/` correspondente.
- [ ] Se for criar pack novo: veja `examples/example-pack-init.md` e use
      `packs/_template-pack/` como base.

## Integracoes opcionais

Documentadas como esqueleto em `core/integrations/`:

- **OpenClaw** (bridge WhatsApp/Telegram -> LLM): configurar variaveis em
  `.env`, subir daemon local.
- **n8n** (workflows automatizados): rodar via Docker Compose; preferir
  self-hosted para liberar `Execute Command`.
- **Obsidian** (navegacao pessoal de memoria): apenas leitura - nao usar
  como fonte de verdade transacional.
- **Pixel Agents** (extensao VS Code): opcional, acelera invocacao por
  trigger.

## Spec Kit (opcional)

Se quiser usar Spec Kit no projeto:

- [ ] Verificar se `.specify/memory/constitution.md` existe na raiz.
- [ ] Adaptar constituicao para o projeto especifico (decisao item 4 em
      `DECISIONS_PENDING.md`).
- [ ] Usar skills `speckit-*` (ver `.cursor/skills/`).

## Primeira sessao com Claude Code (ou outra CLI)

Sugestao de prompt inicial:

```
Voce esta no repositorio Feltrim Agents Base. Carregue:
1. CLAUDE.md raiz
2. core/CLAUDE.md (se existir, senao o pointer raiz)
3. core/memory/MEMORY.md
4. core/docs/SQUAD_INDEX.md
5. Liste quais packs estao ativos em packs/
6. Aguarde minha proxima instrucao.
```

A partir dai, o agente esta pronto. Para tarefas concretas, use o roster
em `core/docs/SQUAD_INDEX.md` para escolher a gem certa, ou peça para o
agente principal "spawn <gem>" passando o request packet.

## Onde pedir ajuda

- Para entender o framework: `core/docs/manifesto/FELTRIMS_FRAMEWORK_MANIFESTO.md`
- Para entender os 10 pilares: `core/docs/OPERATING_MODEL.md`
- Para entender niveis/certs/unlocks: `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md`
- Para entender governanca: `governance/COMPANY_CHARTER.md`
- Para entender pack: `packs/<pack>/README.md`

## Coexistencia com repos antigos

Se voce tem o repo antigo `feltrim-agents-base/feltrim-agents-base/` na
maquina, ele continua valido como historico. Toda nova gem, brain, ritual,
protocolo ou pack deve nascer aqui.

## Veja tambem

- `core/agents/_template/SETUP_TEMPLATE.md` - setup de novo pack/projeto a
  partir do core.
- `examples/example-pack-init.md` - passo a passo para criar pack novo.
- `examples/example-spawn-team-meeting.md` - exemplo de spawn de squad.
