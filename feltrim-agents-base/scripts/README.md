# scripts/

Scripts auxiliares locais. Sao **espelhos** dos jobs em `.github/workflows/ci.yml`
para permitir shift-left: bloquear no commit local o que o CI bloquearia no PR.

Em divergencia entre script local e CI, **o CI eh a fonte de verdade**.

## Inventario

| Script | Espelha job CI | Quando roda | Bloqueia? |
|--------|----------------|-------------|-----------|
| `check-flag-words.sh`   | Job 2 - flag words | `pre-commit` | sim (exceto email policy = warn) |
| `check-flag-words.ps1`  | Job 2 (versao Windows) | manual | sim |
| `check-structure.sh`    | Job 4 - structure sanity | `pre-commit` | sim |
| `check-links.sh`        | Job 3 - markdown link check | `manual` (opt-in) | sim |

## Como acionar

### Via pre-commit (recomendado)

```bash
pip install pre-commit
pre-commit install
git commit -m "..."                                    # roda hooks automaticamente
pre-commit run --all-files                             # roda em tudo, nao so no diff
pre-commit run markdown-link-check --hook-stage manual --all-files   # opt-in lento
```

### Diretamente

```bash
bash scripts/check-flag-words.sh
bash scripts/check-structure.sh
bash scripts/check-links.sh
```

```powershell
pwsh scripts/check-flag-words.ps1
```

## Dependencias

| Tool | Por que | Instalar |
|------|---------|----------|
| `ripgrep` (rg) | Busca rapida em `check-flag-words.*` | Windows: `choco install ripgrep` ou `winget install BurntSushi.ripgrep.MSVC`. macOS: `brew install ripgrep`. Linux: `apt install ripgrep`. |
| `markdown-link-check` | Validar links em md | `npm install -g markdown-link-check` |
| `pre-commit` | Framework de hooks | `pip install pre-commit` |
| `bash` | Executar scripts | Windows: Git Bash (vem com Git for Windows). |

Ausencia de qualquer ferramenta gera **WARN** local (nao bloqueia) - o CI vai
pegar de qualquer forma. Isso evita travar dev novo no primeiro clone.

## Quando atualizar

Sempre que `.github/workflows/ci.yml` mudar uma checagem (novo padrao, novo
arquivo obrigatorio, novo regex de secret), atualize o script local
correspondente. Sem isso, o CI vai falhar enquanto o commit local passa - o
inverso do shift-left.
