# Core Agents (15 gens canonicas)

Quinze personas-base do Feltrim Agents Framework, todas sanitizadas para uso
generico (sem referencias a clientes ou domino especifico da empresa Rafael).

Cada gem traz comentario `<!-- origem: ... sanitizada em ... -->` apontando
para a versao mais rica disponivel na origem.

## Roster por area

### CIAO (gate executivo)
- `gem_sofia_ciao.md` - Sofia - Chief Intelligence & Auditing Officer

### Produto e Gestao
- `gem_marlon_po.md` - Marlon - Product Owner
- `gem_claudia_pm.md` - Claudia - Project Manager

### Tech e Arquitetura
- `gem_beatriz_tl.md` - Beatriz - Tech Lead
- `gem_aline_cloud.md` - Aline - Cloud Architect

### Engenharia
- `gem_joao_backend.md` - Joao - Backend Engineer
- `gem_fabio_frontend.md` - Fabio - Frontend Core React
- `gem_cleber_mobile.md` - Cleber - Mobile Developer
- `gem_camila_devops.md` - Camila - DevOps CI/CD

### Dados
- `gem_emerson_supabase.md` - Emerson - Supabase / Postgres Engineer
- `gem_pedro_dba.md` - Pedro - DBA & Analytics

### Design e UX
- `gem_laura_ui.md` - Laura - UI/UX Senior Design System
- `gem_ana_tdah.md` - Ana - TDAH UX Ally

### IA e Qualidade
- `gem_mariana_prompt.md` - Mariana - Prompt Engineer
- `gem_rafael_qa.md` - Rafael - QA SDET

## Equidade

15 personas com distribuicao por genero (mantida da v1 do FF):

- 7 nomes femininos: Sofia, Claudia, Beatriz, Aline, Camila, Laura, Ana, Mariana (8)
- 7 nomes masculinos: Marlon, Joao, Fabio, Cleber, Emerson, Pedro, Rafael (7)

## Como criar uma gem nova

1. Copie `_template/gem-skeleton.md` para `core/agents/gem_<nome>_<funcao>.md`.
2. Preencha todos os placeholders.
3. Adicione no `core/docs/SQUAD_INDEX.md` na linha correspondente.
4. Se nivel >= N3 com brain proprio, crie `core/memory/agents/<slug>/brain.md`.
5. Atualize `core/agents/README.md` (este arquivo).

## Template

Ver `_template/` para esqueleto, INDEX_TEMPLATE e SETUP_TEMPLATE de novos
projetos/packs.
