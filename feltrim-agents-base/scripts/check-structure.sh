#!/usr/bin/env bash
# check-structure.sh
#
# Espelho LOCAL do job `structure-check` em .github/workflows/ci.yml.
#
# Garante que arquivos e diretorios obrigatorios continuam presentes apos
# qualquer commit, e que o pack core mantem o numero minimo de gens (>=15) e
# protocolos (>=8).
#
# Em divergencia entre este script e o CI, o CI eh a fonte de verdade.

set -euo pipefail

if [ -t 1 ]; then
  RED=$'\033[0;31m'; GREEN=$'\033[0;32m'; NC=$'\033[0m'
else
  RED=""; GREEN=""; NC=""
fi

fail=0

# ---------------------------------------------------------------------------
required_files=(
  "README.md"
  "CONTRIBUTING.md"
  "CODE_OF_CONDUCT.md"
  "SECURITY.md"
  "CHANGELOG.md"
  "LICENSE"
  "CLAUDE.md"
  "AGENTS.md"
  "core/CLAUDE.md"
  ".env.example"
  ".gitignore"
  "DECISIONS_PENDING.md"
  "core/memory/MEMORY.md"
  "core/docs/SQUAD_INDEX.md"
  "core/docs/AGENT_ACTIVATION_POLICY.md"
  "core/docs/TOKEN_ECONOMY.md"
  "governance/COMPANY_CHARTER.md"
  "governance/SECURITY_AND_PRIVACY.md"
)

echo "[1/4] Required files..."
for f in "${required_files[@]}"; do
  if [ ! -f "$f" ]; then
    echo "${RED}MISSING:${NC} $f"
    fail=1
  fi
done

# ---------------------------------------------------------------------------
required_dirs=(
  "core/agents"
  "core/protocols"
  "core/docs"
  "core/memory/agents"
  "core/memory/team-rituals"
  "governance"
  "packs"
  "examples"
  ".specify/memory"
)

echo "[2/4] Required directories..."
for d in "${required_dirs[@]}"; do
  if [ ! -d "$d" ]; then
    echo "${RED}MISSING DIR:${NC} $d"
    fail=1
  fi
done

# ---------------------------------------------------------------------------
echo "[3/4] Core gens count..."
gens=$(ls -1 core/agents/gem_*.md 2>/dev/null | wc -l | tr -d ' ')
echo "  found: $gens"
if [ "$gens" -lt 15 ]; then
  echo "${RED}FAIL:${NC} esperado >=15 core gens, encontrado $gens"
  fail=1
fi

# ---------------------------------------------------------------------------
echo "[4/4] Core protocols count..."
protocols=$(ls -1 core/protocols/*.md 2>/dev/null | grep -v README | wc -l | tr -d ' ')
echo "  found: $protocols"
if [ "$protocols" -lt 8 ]; then
  echo "${RED}FAIL:${NC} esperado >=8 protocolos, encontrado $protocols"
  fail=1
fi

# ---------------------------------------------------------------------------
if [ "$fail" -eq 0 ]; then
  echo "${GREEN}OK:${NC} structure-check passou."
  exit 0
else
  echo "${RED}FAIL:${NC} structure-check encontrou ausencias."
  exit 1
fi
