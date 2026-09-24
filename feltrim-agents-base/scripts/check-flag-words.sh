#!/usr/bin/env bash
# check-flag-words.sh
#
# Espelho LOCAL do job `flag-words-check` em .github/workflows/ci.yml.
# Roda no pre-commit hook para falhar ANTES do push.
#
# Em divergencia entre este script e o CI, o CI eh a fonte de verdade.
# Atualize este arquivo para acompanhar mudancas no workflow, nao o contrario.
#
# Requer:
#   - bash 4+ (Git Bash no Windows funciona)
#   - ripgrep (`rg`) instalado
#       Windows: choco install ripgrep   ou   winget install BurntSushi.ripgrep.MSVC
#       macOS:   brew install ripgrep
#       Linux:   apt install ripgrep     ou   dnf install ripgrep
#
# Saida: exit 0 = OK, exit 1 = falha (com mensagem do que falhou).

set -euo pipefail

# ANSI minimo - se nao for tty, sem cor.
if [ -t 1 ]; then
  RED=$'\033[0;31m'
  GREEN=$'\033[0;32m'
  YELLOW=$'\033[0;33m'
  NC=$'\033[0m'
else
  RED=""
  GREEN=""
  YELLOW=""
  NC=""
fi

fail=0

# Verifica que rg esta instalado. Se nao, instrui e segue (warning, nao bloqueia
# tudo no primeiro setup; o CI ainda vai pegar).
if ! command -v rg >/dev/null 2>&1; then
  echo "${YELLOW}WARN: ripgrep (rg) nao instalado - skipping flag-words-check local.${NC}"
  echo "      Instale para checagem local:"
  echo "        Windows: choco install ripgrep   ou   winget install BurntSushi.ripgrep.MSVC"
  echo "        macOS:   brew install ripgrep"
  echo "        Linux:   apt install ripgrep"
  echo "      O CI vai rodar essa checagem mesmo assim no push."
  exit 0
fi

# ---------------------------------------------------------------------------
# Check 1 - Caminhos absolutos (Windows/Unix) em arquivos publicos
# ---------------------------------------------------------------------------
echo "[1/4] Checking absolute paths..."

# Lista de paths a varrer (igual ao CI). Skip silencioso se algum dir nao existe.
search_paths=()
for p in core governance examples docs packs README.md CONTRIBUTING.md \
         CODE_OF_CONDUCT.md SECURITY.md CHANGELOG.md CLAUDE.md AGENTS.md LICENSE; do
  if [ -e "$p" ]; then
    search_paths+=("$p")
  fi
done

if [ ${#search_paths[@]} -gt 0 ]; then
  if rg -i "(C:\\\\Users\\\\[A-Za-z]+|/Users/[A-Za-z]+/|~/Desktop)" \
        "${search_paths[@]}" \
        --glob '!**/CHANGELOG.md' \
        --glob '!**/README.md' \
        --glob '!*.lock' \
        --glob '!scripts/check-flag-words.sh' \
        --glob '!scripts/check-flag-words.ps1' \
        > /tmp/.flag-words-paths.$$ 2>/dev/null; then
    echo "${RED}FAIL: absolute paths found:${NC}"
    cat /tmp/.flag-words-paths.$$
    fail=1
  fi
  rm -f /tmp/.flag-words-paths.$$
fi

# ---------------------------------------------------------------------------
# Check 2 - .env real commitado (excluindo .env.example)
# ---------------------------------------------------------------------------
echo "[2/4] Checking committed .env files..."
bad_env=$(git ls-files | grep -E "^\.env$|^\.env\.[a-z]+$" | grep -vE "^\.env\.example$" || true)
if [ -n "$bad_env" ]; then
  echo "${RED}FAIL: real .env file(s) commitado:${NC}"
  echo "$bad_env"
  fail=1
fi

# ---------------------------------------------------------------------------
# Check 3 - API keys / tokens / secrets
# ---------------------------------------------------------------------------
echo "[3/4] Checking for likely secrets..."
if rg -i "(api[_-]?key|token|password|secret)\s*[:=]\s*['\"][A-Za-z0-9_-]{20,}" \
      --type-not lock \
      --glob '!**/CHANGELOG.md' \
      --glob '!**/SECURITY.md' \
      --glob '!**/SECURITY_AND_PRIVACY.md' \
      --glob '!**/.github/**' \
      --glob '!**/.env.example' \
      --glob '!scripts/check-flag-words.sh' \
      --glob '!scripts/check-flag-words.ps1' \
      > /tmp/.flag-words-secrets.$$ 2>/dev/null; then
  echo "${RED}FAIL: likely secret commitado:${NC}"
  cat /tmp/.flag-words-secrets.$$
  fail=1
fi
rm -f /tmp/.flag-words-secrets.$$

# ---------------------------------------------------------------------------
# Check 4 - Committer email policy (allowlist *@users.noreply.github.com)
# ---------------------------------------------------------------------------
echo "[4/4] Checking committer email policy..."
bad_emails=$(git log -10 --format="%ae" 2>/dev/null \
  | grep -vE "^[^@]+@users\.noreply\.github\.com$" \
  | grep -vE "^[^@]+@noreply\.github\.com$" \
  | grep -v "^$" || true)
if [ -n "$bad_emails" ]; then
  echo "${YELLOW}WARN: commits encontrados com email fora da allowlist:${NC}"
  echo "$bad_emails" | sort -u
  echo ""
  echo "Configure git local com:"
  echo "  git config user.email '<seu-user>@users.noreply.github.com'"
  echo ""
  echo "(NAO bloqueando o commit local - mas o CI vai bloquear o push.)"
  # local = warning. CI = fail. Evita travar dev novo no setup.
fi

# ---------------------------------------------------------------------------
if [ "$fail" -eq 0 ]; then
  echo "${GREEN}OK: flag-words-check passou.${NC}"
  exit 0
else
  echo "${RED}FAIL: flag-words-check encontrou problemas. Corrija e tente de novo.${NC}"
  exit 1
fi
