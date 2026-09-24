# CLAUDE.md - Feltrim Agents Base (pointer)

Este e o ponto de entrada minimo para Claude Code neste repositorio.

O boot sequence real, hierarquia de agentes, sistema de memoria e regras
operacionais estao em:

- `core/CLAUDE.md` - boot sequence canonico
- `core/docs/SQUAD_INDEX.md` - roster completo, triggers e niveis
- `core/memory/MEMORY.md` - indice de memoria persistente
- `governance/COMPANY_CHARTER.md` - identidade da empresa

## Boot rapido

1. Ler `core/CLAUDE.md`.
2. Ler `core/memory/MEMORY.md` e carregar arquivos indexados.
3. Glob `core/agents/*.md` e contar gens disponiveis.
4. Ler `core/docs/SQUAD_INDEX.md` para entender quem invocar quando.
5. Verificar se algum pack esta ativo (existe pasta em `packs/<nome>/` com
   `agents/` populado) e, se sim, ler `packs/<nome>/README.md`.

## Packs disponiveis

- `packs/cms-gherkin/` - BDD/Gherkin com prompts por modelo LLM
- `packs/us-avaliator/` - Studio QA, substituicao Copilot Pro (exemplo)
- `packs/_template-pack/` - esqueleto para novos packs

Packs proprios da empresa (com IP de cliente) vivem em repositorio privado
separado.

## Aviso

Carregue apenas `core/` e packs ativos do diretorio `packs/`. Snapshots
historicos vivem em repositorio privado.
