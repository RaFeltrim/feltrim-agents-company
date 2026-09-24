# Contribuindo com Feltrim Agents Base

Obrigado pelo interesse em contribuir. Este boilerplate cresce com PRs
cuidadosos que preservam a separacao entre `core/` generico, `packs/`
especificos e `governance/` da empresa adotante.

## TL;DR

1. Abra uma issue antes de PR grande (`feature_request` ou `agent_proposal`).
2. Fork + branch a partir de `master`.
3. Rode a checagem de palavras-bandeira local (ver `governance/SECURITY_AND_PRIVACY.md`).
4. PR com checklist preenchido (`.github/PULL_REQUEST_TEMPLATE.md`).
5. Aguardar revisao - Sofia CIAO (auditoria) + Mariana (prompts) + Beatriz TL (arquitetura) sao os revisores naturais.

## Onde sua contribuicao se encaixa

| Tipo de mudanca | Vai para | Quem revisa |
|-----------------|----------|-------------|
| Nova gem generica (papel reutilizavel) | `core/agents/gem_<slug>.md` | Mariana + Beatriz TL |
| Nova versao de gem existente | `core/agents/gem_<slug>.md` (commit incremental) | Mariana + dona do papel |
| Novo protocolo sistemico | `core/protocols/<NOME>.md` + atualizar README | Beatriz TL + Sofia CIAO |
| Novo ritual de equipe | `core/memory/team-rituals/<nome>.md` + atualizar README | Marlon-PO ou Claudia-PM |
| Nova certificacao | `core/docs/AGENT_CERTIFICATIONS.md` + `governance/CERTIFICATION_POLICY.md` | Sofia CIAO + Beatriz TL |
| Novo unlock | `core/docs/AGENT_UNLOCKS.md` | Sofia CIAO |
| Novo pack publico | `packs/<nome>/` com `README.md` + `docs/` + atualizar `core/docs/SQUAD_INDEX.md` | Beatriz TL + Sofia CIAO |
| Novo exemplo | `examples/example-<nome>.md` + atualizar `examples/README.md` | qualquer reviewer |
| Mudanca em governance | `governance/<arquivo>.md` | Sofia CIAO + decisor humano |
| Doc auxiliar publica | `docs/<NOME>.md` | qualquer reviewer |
| Correcao de typo / link / formatacao | onde for | qualquer reviewer |

## O que NAO entra neste repo

- Nome de cliente real, sistema interno de cliente, prefixo SKU, codigo de regra interno - ver `governance/SECURITY_AND_PRIVACY.md`.
- Email corporativo nos commits (use `<seu-user>@users.noreply.github.com`).
- Credenciais, API keys, tokens, secrets - usar `.env` local.
- IP de terceiros sem auditoria de origem e licenca.
- Conteudo somente em PDF / video / binario (nao indexavel).

## Padroes de commit

Padrao tipo Conventional Commits, simples:

```
<tipo>(<area>): <descricao curta em portugues>

[opcional: corpo explicando POR QUE, nao O QUE]
```

Tipos comuns:

- `feat` - nova capacidade (gem, protocolo, ritual, pack, doc, etc.)
- `fix` - bug em script, comportamento errado, link quebrado
- `docs` - mudanca apenas em documentacao
- `refactor` - reorganizacao sem mudar comportamento
- `chore` - manutencao (ci, deps, configs)
- `sec` - sanitizacao, remocao de leak, atualizacao de politica de seguranca

Areas comuns: `core`, `governance`, `packs`, `examples`, `gh` (.github/), `docs`, `ci`.

Exemplo:

```
feat(core): add gem_cleber_mobile com unlock host-flash-talk
```

## Padroes de PR

- 1 PR = 1 escopo. Nao misturar refator com nova feature.
- Titulo segue o mesmo padrao do commit.
- Descricao preenche o template em `.github/PULL_REQUEST_TEMPLATE.md`.
- Marque a checklist de sanitizacao - se o item nao se aplica, deixe explicito.
- Resposta a review: corrigir e re-pedir review, nao discutir.

## Checagem local antes do push (shift-left)

O repositorio tem pre-commit hooks que espelham 1:1 os jobs do CI. Instalar
uma vez evita o ciclo "push - CI vermelho - fix - push de novo" para erros
triviais (lint, link quebrado, placeholder vazado, email corporativo).

### Setup (uma vez por clone)

```bash
pip install pre-commit
pre-commit install
```

### Uso diario

```bash
git commit -m "feat(core): add gem_nova"   # hooks rodam automaticamente

# Forcar rodar em todos arquivos (nao so o diff):
pre-commit run --all-files

# Rodar so 1 hook:
pre-commit run markdownlint --all-files

# Rodar o link-check (opt-in, mais lento, bate em rede):
pre-commit run markdown-link-check --hook-stage manual --all-files

# Emergencia (NAO recomendado, prefira corrigir):
git commit --no-verify
```

### Scripts invocaveis direto (sem pre-commit)

```bash
bash scripts/check-flag-words.sh    # sanitizacao (job CI 2)
bash scripts/check-structure.sh     # arquivos obrigatorios (job CI 4)
bash scripts/check-links.sh         # links markdown (job CI 3, opt-in)
```

Equivalente PowerShell (Windows, sem Git Bash):

```powershell
pwsh scripts/check-flag-words.ps1
```

### Dependencias

| Tool | Para que | Instalar |
|------|----------|----------|
| `pre-commit` | Framework de hooks | `pip install pre-commit` |
| `ripgrep` (rg) | Flag-words check | `choco install ripgrep` / `brew install ripgrep` / `apt install ripgrep` |
| `markdown-link-check` | Link check | `npm install -g markdown-link-check` |
| `markdownlint-cli2` | Markdown lint | gerenciado automaticamente pelo `pre-commit` |

Veja `scripts/README.md` para detalhe de cada script.

O workflow em `.github/workflows/ci.yml` continua sendo a fonte de verdade -
em divergencia entre local e CI, o CI bloqueia o merge. Os scripts locais so
antecipam a falha.

## Boot rapido para revisores

Antes de aprovar um PR, leia:

1. `governance/SECURITY_AND_PRIVACY.md` - politica de seguranca / privacidade.
2. `governance/PROMOTION_POLICY.md` - quem aprova o que.
3. `governance/AGENT_HIERARCHY.md` - cadeia de escalada.
4. `core/docs/AGENT_ACTIVATION_POLICY.md` - quando convocar quais agentes.
5. O PR especifico + arquivos tocados.

## Codigo de conduta

Este projeto adota o [Contributor Covenant](CODE_OF_CONDUCT.md). Comportamento
abusivo, assedio ou desrespeito sera tratado conforme a politica.

## Licenca

Ao contribuir, voce aceita que sua contribuicao sera licenciada nos mesmos
termos de `LICENSE` (proprietaria provisoria, decisao final em andamento -
ver `DECISIONS_PENDING.md`).

## Duvidas

- Tecnicas: abrir issue do tipo `feature_request`.
- Sobre o framework: abrir issue do tipo `question` (ou Discussion se ativo).
- Sobre seguranca / leak: ver `SECURITY.md`.

Obrigado por ajudar a manter o boilerplate util, generico e auditavel.
