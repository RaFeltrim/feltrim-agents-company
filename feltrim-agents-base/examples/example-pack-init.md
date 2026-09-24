# Exemplo: criar novo pack

> Como criar um novo pack do Feltrim Agents Framework a partir do
> template, sem misturar com `core/` nem com packs existentes.

## Cenario

Voce tem um novo projeto / cliente / dominio e quer encapsular as
particularidades dele em um pack proprio, mantendo `core/` generico.

## Quando criar pack vs quando trabalhar em core

| Situacao | Pack ou Core? |
|----------|---------------|
| Regra valida para qualquer projeto | **Core** |
| Regra valida apenas para este cliente / dominio | **Pack** |
| Gem nova com persona generica reutilizavel | **Core** |
| Gem com habilidades de RPA especificas de um sistema | **Pack** |
| Skill operacional generica | **Core** |
| Skill que precisa do diretorio do projeto cliente | **Pack** |
| Brain de agente core acumulando aprendizado generico | **Core** |
| Brain de agente especifico de um pack (ex: `<pack>-orchestrator`) | **Pack** |

## Passo a passo

### 1. Identificar nome do pack

Convencao: `<dominio>-<funcao>` (ex: `cms-gherkin`, `us-avaliator`,
`<seu-pack>`).

Verificar que nao colide com pack existente.

### 2. Criar estrutura

```bash
PACK=<seu-pack>
mkdir -p packs/$PACK/{agents,brains,docs,skills}
```

Ou copiar do template (quando `packs/_template-pack/` estiver disponivel):

```bash
cp -r packs/_template-pack packs/$PACK
```

### 3. Criar `README.md` do pack

Usar como base o `README.md` de um pack existente (ex:
`packs/cms-gherkin/README.md` ou `packs/us-avaliator/README.md`):

- Visao geral do pack (1-2 paragrafos)
- Atencao / flag words
- Estrutura
- Como ativar (quais arquivos carregar no chat)
- Fonte da verdade
- Decisor humano
- Roster do pack
- Certificacoes especificas
- Skills locais
- Veja tambem

### 4. Criar gens especificas (se aplicavel)

Em `packs/$PACK/agents/gem_<slug>.md`:

- Header: `<!-- origem: ... criada em YYYY-MM-DD para pack $PACK -->`
- Usar `core/agents/_template/gem-skeleton.md` como skeleton.
- Especificar nivel atual (N1-N5 ver `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md`).
- Especificar certificacoes default.
- Especificar unlocks default.

### 5. Criar brains (se gens especificas precisam de memoria)

Em `packs/$PACK/brains/<slug>/brain.md`:

- Header com origem e nivel
- `Aprendizados`
- `Decisoes recentes`
- `Padroes que funcionaram`
- `Padroes que falharam`

### 6. Criar docs operacionais

Em `packs/$PACK/docs/`:

- Regras nao-negociaveis do pack
- Operating contract com o cliente / dominio
- Capability matrix do pack
- `CHANGELOG.md` (versionar mudancas)

### 7. Criar skills (se aplicavel)

Se o pack precisa de skills operacionais ativas, elas geralmente vivem
no **repo do projeto cliente** (`.cursor/skills/...`), nao no pack
boilerplate. Apenas referenciar em `packs/$PACK/skills/README.md`.

### 8. Verificar contra `governance/SECURITY_AND_PRIVACY.md`

Rodar a checagem antes de commitar:

```bash
rg -i "(api_key|password|secret|token|<lista-flag-words-do-cliente>)" packs/$PACK/
```

Resultado esperado: zero matches de segredo ativo.

### 9. Atualizar `core/docs/SQUAD_INDEX.md` (se gens especificas foram criadas)

Adicionar linha apontando para o pack.

### 10. Commit

```bash
git add packs/$PACK core/docs/SQUAD_INDEX.md
git commit -m "feat(pack): adiciona pack $PACK com X gens + Y brains + Z docs"
```

## Decisor humano

Toda criacao de pack passa pelo decisor humano (Rafael Feltrim) para
validacao da estrutura e dos guardrails.

## Veja tambem

- `packs/cms-gherkin/` (exemplo pack rico - prompts + ferramentas + exemplos)
- `packs/us-avaliator/` (exemplo pack didatico - proposta sanitizada)
- `packs/_template-pack/` (esqueleto vazio para novos packs)
- `core/agents/_template/gem-skeleton.md`
- `core/memory/agents/_templates/`
- `governance/SECURITY_AND_PRIVACY.md`
