# core/CLAUDE.md - Boot sequence (Claude Code / CLIs / IDEs)

> Pointer para o boot sequence canonico. Este arquivo existe para que
> CLIs e ferramentas que esperam encontrar `core/CLAUDE.md` funcionem
> sem ajuste. O boot sequence completo esta em `CLAUDE.md` raiz e em
> `AGENTS.md` raiz (espelho para outras CLIs/IDEs).

## Ordem de leitura recomendada (boot)

1. **`CLAUDE.md`** (raiz) - entry-point oficial
2. **`AGENTS.md`** (raiz) - espelho para outras CLIs
3. **`core/memory/MEMORY.md`** - indice de memoria operacional
4. **`core/docs/SQUAD_INDEX.md`** - roster de gens + triggers + anti-patterns
5. **`core/docs/AGENT_ACTIVATION_POLICY.md`** - quando convocar SOLO/PAR/MINI/FULL
6. **`core/docs/TOKEN_ECONOMY.md`** - politica de custo de token
7. **`governance/COMPANY_CHARTER.md`** - identidade da empresa adotante
8. **`governance/SECURITY_AND_PRIVACY.md`** - politica de seguranca

Para detalhes de arquitetura, ver `core/docs/ARQUITETURA.md` e
`core/docs/manifesto/FELTRIMS_FRAMEWORK_MANIFESTO.md`.

## Por que este arquivo existe

Algumas ferramentas multi-agente esperam encontrar `<repo>/CLAUDE.md`
**ou** `<repo>/core/CLAUDE.md` (convencao). Manter ambos garante
compatibilidade sem duplicar conteudo. O conteudo canonico vive na
raiz.
