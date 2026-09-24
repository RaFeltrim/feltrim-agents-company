# Getting Started - Feltrim Agents Base

> Do zero ao primeiro agente respondendo em **5 minutos**.

## Pre-requisitos

- Git instalado.
- Editor com suporte a markdown (VS Code, Cursor, Obsidian, etc.).
- (Opcional) CLI de algum LLM (Claude Code, Cursor, Codex CLI, Gemini CLI).
- (Opcional) Python 3.10+ para rodar scripts de `packs/cms-gherkin/ferramentas/`.

## Passo 1 - Clone

```bash
git clone https://github.com/RaFeltrim/feltrim-agents-base.git
cd feltrim-agents-base
```

## Passo 2 - Entenda o mapa em 30 segundos

```text
core/        <- gens, protocolos, docs canonicos (generico, reutilizavel)
packs/       <- packs especializados por dominio (opt-in)
governance/  <- politicas da empresa adotante
examples/    <- exemplos prontos para copiar
```

Leia `README.md` raiz se ainda nao leu.

## Passo 3 - Inicialize sua identidade Git para o repo

Evita vazar email corporativo:

```bash
git config user.name "Seu Nome"
git config user.email "<seu-user>@users.noreply.github.com"
```

## Passo 4 - Carregue o boot sequence no seu CLI

### Para Claude Code

O arquivo `CLAUDE.md` ja eh ponto de entrada. Em sessao Claude Code:

```bash
claude
> Leia CLAUDE.md, core/CLAUDE.md, core/memory/MEMORY.md e
  core/docs/SQUAD_INDEX.md. Confirme com a lista de gens disponiveis.
```

### Para Cursor / Codex / outros

Use `AGENTS.md` (espelho do CLAUDE.md). Em sessao:

```text
Leia AGENTS.md, core/docs/SQUAD_INDEX.md e
core/docs/AGENT_ACTIVATION_POLICY.md.
Apresente as 15 gens core e quando convocar cada uma.
```

## Passo 5 - Convoque sua primeira gem (SOLO)

Exemplo para uma tarefa SOLO simples:

```text
Voce eh `core/agents/gem_rafael_qa.md` (QA SDET, N3).

Tarefa: liste 5 cenarios de teste BDD para um login com 2FA, em Gherkin
em portugues, respeitando a estrutura Dado/Quando/Entao/E.

Saida: bloco de codigo Gherkin + 1 linha de risco identificado.
```

Resultado esperado: 5 cenarios Gherkin estruturados + nota de risco.

## Passo 6 - Convoque um PAR (modo PAR)

Exemplo para uma tarefa que envolve duas areas:

```text
Voce eh `core/agents/gem_joao_backend.md` (Backend Engineer).
Co-piloto: `core/agents/gem_rafael_qa.md` (QA SDET).

Tarefa: implemente endpoint POST /api/usuarios com validacao Zod e
escreva 3 testes BDD de aceite. Sigam o handoff de
`core/protocols/HANDOFF_PROTOCOL.md`.

Saida (Joao): codigo do endpoint + payload schema.
Saida (Rafael): 3 cenarios Gherkin + 1 risco de regressao identificado.
```

## Passo 7 - Decida qual modo usar antes de gastar token

Antes de convocar, leia `core/docs/AGENT_ACTIVATION_POLICY.md` e escolha:

| Modo | Quando | Custo relativo |
|------|--------|----------------|
| SOLO | 1 gem, tarefa atomica (typo, bug local, refactor pontual) | 1x |
| PAR | 2 gens, handoff direto (backend + QA, frontend + UI) | 2x |
| MINI | 3-4 gens, feature pequena/media multi-area | 4x |
| FULL | toda squad, decisao critica/Go-Live/auditoria | 10x+ |

> 80% das tarefas resolvem em SOLO ou PAR. FULL eh excecao deliberada.

## Passo 8 - Comece a criar seu pack proprio

Quando voce tiver projetos especificos (cliente, dominio, time):

```bash
cp -r packs/_template-pack packs/<seu-pack>
```

Siga `examples/example-pack-init.md` passo a passo.

## Proximos passos

1. **Leia o manifesto:** `core/docs/manifesto/FELTRIMS_FRAMEWORK_MANIFESTO.md`
   para entender o "porque" do framework.
2. **Configure pre-commit hook:** ver `governance/SECURITY_AND_PRIVACY.md`
   para o comando de palavras-bandeira da sua instalacao.
3. **Inicialize agent profiles:** crie
   `core/memory/agents/<slug>/agent-profile.md` para cada gem em uso ativo
   (template em `core/memory/agents/_templates/agent-profile-template.md`).
4. **Veja casos de uso:** `docs/USE_CASES.md`.
5. **Compare com alternativas:** `docs/COMPARISON.md`.

## Problemas comuns

| Sintoma | Causa provavel | Solucao |
|---------|----------------|---------|
| Agente "esquece" rapidamente | Boot sequence incompleto | Confirme que carregou `core/CLAUDE.md` + `MEMORY.md` + SQUAD_INDEX |
| Custo de token muito alto | Modo errado (usando FULL pra tarefa simples) | Leia `core/docs/TOKEN_ECONOMY.md` e force modo menor |
| Agentes "discordam" sem produzir saida | Falta handoff explicito | Aplique `core/protocols/HANDOFF_PROTOCOL.md` |
| Saida sem evidencia auditavel | Falta de scorecard | Aplique `core/protocols/EVALS_AND_MONITORING.md` |
| PR rejeitado por sanitizacao | Flag word vazou | Rode `governance/SECURITY_AND_PRIVACY.md` checagem antes do push |

## Veja tambem

- `README.md` raiz - visao geral
- `docs/USE_CASES.md` - 5 casos de uso concretos
- `docs/COMPARISON.md` - vs LangChain, CrewAI, AutoGen, BMAD
- `core/docs/ONBOARDING.md` - onboarding interno mais detalhado
- `CONTRIBUTING.md` - como contribuir
