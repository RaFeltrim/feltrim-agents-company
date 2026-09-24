#!/usr/bin/env bash
# check-links.sh
#
# Espelho LOCAL do job `markdown-links` em .github/workflows/ci.yml.
# Opt-in (manual stage no pre-commit) porque eh lento (~30-60s) e bate em
# rede. Rode antes de PR grande:
#
#   pre-commit run markdown-link-check --hook-stage manual --all-files
#
# Ou diretamente:
#
#   bash scripts/check-links.sh
#
# Requer: markdown-link-check (npm)
#   npm install -g markdown-link-check

set -euo pipefail

if [ -t 1 ]; then
  RED=$'\033[0;31m'; GREEN=$'\033[0;32m'; YELLOW=$'\033[0;33m'; NC=$'\033[0m'
else
  RED=""; GREEN=""; YELLOW=""; NC=""
fi

if ! command -v markdown-link-check >/dev/null 2>&1; then
  echo "${YELLOW}WARN:${NC} markdown-link-check nao instalado."
  echo "       Instale: npm install -g markdown-link-check"
  echo "       O CI vai rodar essa checagem mesmo assim no PR."
  exit 0
fi

CONFIG=".github/markdown-link-check.json"
fail=0

# Lista de arquivos = igual ao CI.
files=(
  README.md
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  SECURITY.md
  CHANGELOG.md
)
# globs (apenas se dir existe)
for d in docs core/docs governance examples; do
  if [ -d "$d" ]; then
    for f in "$d"/*.md; do
      [ -f "$f" ] && files+=("$f")
    done
  fi
done

for f in "${files[@]}"; do
  if [ -f "$f" ]; then
    echo "Checking $f..."
    if ! markdown-link-check "$f" --quiet --config "$CONFIG"; then
      fail=1
    fi
  fi
done

if [ "$fail" -eq 0 ]; then
  echo "${GREEN}OK:${NC} markdown-link-check passou."
  exit 0
else
  echo "${RED}FAIL:${NC} markdown-link-check encontrou links quebrados."
  exit 1
fi
