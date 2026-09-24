<!-- versao publica sanitizada; template generico para criar pack/projeto a partir de core/ -->

# Setup Template - Novo Pack ou Projeto

> **Versao:** 2.1 (Feltrim Agents Base 2026)
> **Proposito:** instanciar um novo pack ou um novo projeto a partir das gens
> e protocolos do `core/`.

## Quick start (5 minutos)

### Passo 1 - Copie o esqueleto de pack

```bash
cp -r packs/_template-pack/ packs/<nome-do-novo-pack>/
```

ou, para um projeto isolado fora deste repo:

```bash
mkdir <nome-do-projeto>/_ai_docs
cp core/agents/_template/INDEX_TEMPLATE.md <nome-do-projeto>/_ai_docs/INDEX.md
cp core/agents/_template/SETUP_TEMPLATE.md <nome-do-projeto>/_ai_docs/SETUP.md
```

### Passo 2 - Configure o INDEX

Substitua todos os placeholders em `INDEX.md`:

| Placeholder | Exemplo | Descricao |
|-------------|---------|-----------|
| `{NOME_DO_PROJETO}` | `Pack CMS Consignado` | Nome do projeto/pack |
| `{DATA}` | `2026-05-16` | Data de criacao |
| `{STACK_BACKEND}` | `Java Spring` | Stack principal do backend |
| `{STACK_FRONTEND}` | `React` | Stack principal do frontend |
| `{DOMINIO}` | `BDD QA banking` | Dominio funcional do projeto |
| `{DECISOR_HUMANO}` | `Rafael Feltrim` | Quem aprova decisoes finais |

### Passo 3 - Escolha as gens

Decida quais gens do `core/agents/` vao para o pack/projeto:

- Sempre incluir: `gem_sofia_ciao.md` (gate Go-Live)
- Default backend: `joao`, `pedro`, `emerson`, `aline`, `camila`
- Default frontend: `fabio`, `laura`, `cleber`, `ana`
- Default produto: `marlon`, `claudia`
- Default qualidade: `rafael`, `beatriz`, `mariana`

Pack pode adicionar gens proprias em `packs/<pack>/agents/gem_*.md` (ex.:
gens com prefixo do pack: `gem_<pack>_<funcao>.md`).

### Passo 4 - Customize as gens novas (se houver)

Use `gem-skeleton.md` como base. Edite:

- **Persona e estilo** com o tom do pack
- **Especialidades** com tecnologias reais do projeto
- **Quando invocar** com gatilhos reais
- **Regras de comportamento** com guardrails especificos
- **Origem** com path absoluto do template usado

### Passo 5 - Crie o KNOWLEDGE_BASE

```bash
cp core/docs/templates/KNOWLEDGE_BASE_TEMPLATE.md \
   packs/<pack>/docs/KNOWLEDGE_BASE.md
```

Comece vazio. Vai preenchendo conforme bugs sao resolvidos e padroes ouro
emergem.

### Passo 6 - Ative o pack no boot

Se o pack for default para o projeto, mencione em `CLAUDE.md`/`AGENTS.md` ou
em `<projeto>/_ai_docs/INDEX.md` que ele esta ativo. Se for opcional, deixe
apenas referenciado no `README.md`.

## Regras de ouro do framework (aplicaveis ao pack)

1. **Hiper-especializacao** - cada gem tem escopo isolado. QA nao escreve stories. PO nao decide arquitetura.
2. **Hierarquia** - todo pack tem ao menos uma gem CIAO (gate executivo) ou referencia `core/agents/gem_sofia_ciao.md`.
3. **Cultura** - guardrails operam como tradicao, mas decisoes auditaveis vivem em ADR/runbook/backlog (nao em conversa social).
4. **Shift-left** - QA, seguranca e performance presentes desde o instante 0 do pack.
5. **Aprovacao CIAO** - nada vai para producao sem o selo executivo.
6. **Knowledge Base viva** - todo bug catalogado vira anti-padrao no KB do pack.
7. **Portabilidade** - o pack continua valido se for clonado para outro repo, sem dependencia hard-coded de paths.

## Ciclo de vida (workflow padrao)

```
INCEPTION       DEVELOPMENT          DEFENSE             DELIVERY
PO + PM + TL    Front + Back +       QA + DBA +          CIAO veredito
                Mobile + Prompt      DevOps + Cloud
     |               |                    |                  |
     v               v                    v                  v
Requisitos      Codigo src/          Testes .feature    Aprovado / Recusado
Roadmap         Integracoes          Automacao          Deploy ou Rollback
Arquitetura     UI/UX                Performance
```
