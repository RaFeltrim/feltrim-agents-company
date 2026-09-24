# Problemas e Solucoes

Este arquivo consolida o historico operacional do projeto.

Registre aqui:
- problemas recorrentes
- causa raiz
- solucao aplicada
- forma de prevencao

## Dependencia de saida textual repetida

- Data: `2026-03-20 00:00:00`
- Categoria: `Arquitetura de fluxo`
- Status: `Resolvido`
- Arquivos relacionados: `PROMPT_GPT_5_4_ECONOMICO.md, FERRAMENTAS/gerar_artefatos.py, FONTES-ESTRUTURADAS/`

### Contexto

O pacote dependia quase totalmente de geracao textual direta pelo modelo para produzir analise, planilha e feature. Isso repetia o mesmo conteudo em mais de um artefato e elevava o gasto de tokens.

### Causa raiz

Nao existia uma fonte estruturada unica capaz de servir como base para todos os artefatos derivados.

### Solucao aplicada

Foi criado o diretorio `FONTES-ESTRUTURADAS/` com um modelo JSON unico por PI/US, e o script `FERRAMENTAS/gerar_artefatos.py` passou a gerar analise, planilha e feature a partir dessa fonte.

### Prevencao

Sempre atualizar primeiro a fonte estruturada e gerar os artefatos finais por script, evitando reescrita manual do mesmo conteudo em varios arquivos.

## Ausencia de memoria operacional consolidada

- Data: `2026-03-20 00:00:00`
- Categoria: `Governanca`
- Status: `Resolvido`
- Arquivos relacionados: `MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md, FERRAMENTAS/registrar_problema.py`

### Contexto

Problemas enfrentados durante o uso do pacote nao ficavam consolidados em um historico unico, o que dificultava onboarding, prevencao de recorrencia e manutencao futura.

### Causa raiz

Faltava um mecanismo simples e padronizado para registrar contexto, causa raiz, solucao e prevencao.

### Solucao aplicada

Foi criado o relatorio `MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md` junto com o utilitario `FERRAMENTAS/registrar_problema.py` para anexar novos registros de forma padronizada.

### Prevencao

Sempre que houver bloqueio, retrabalho evitado, inconsistencia ou descoberta relevante, registrar o ocorrido no relatorio antes de encerrar a atividade.

## Validacao inicial do modo economico

- Data: `2026-03-20 17:58:30`
- Categoria: `Validacao`
- Status: `Resolvido`
- Arquivos relacionados: `FONTES-ESTRUTURADAS/PROJETO-EXEMPLO.json, FERRAMENTAS/gerar_artefatos.py`

### Contexto

Foi realizada a primeira validacao do fluxo com fonte estruturada e geracao automatica de artefatos.

### Causa raiz

Era necessario confirmar que o fluxo gerava os tres artefatos a partir de uma unica fonte sem perda de cobertura.

### Solucao aplicada

Executado o gerador local com a fonte PROJETO-EXEMPLO.json e mantido o historico na memoria operacional.

### Prevencao

Sempre validar o gerador com a fonte exemplo depois de evolucoes relevantes.

## Resolucao de caminho dependente do diretorio atual

- Data: `2026-03-20 17:59:41`
- Categoria: `Ferramenta local`
- Status: `Resolvido`
- Arquivos relacionados: `FERRAMENTAS/gerar_artefatos.py, PROMPT_GPT_5_4_ECONOMICO.md`

### Contexto

Na primeira validacao do gerador, o comando falhou quando a fonte foi informada com caminho relativo partindo da raiz do workspace.

### Causa raiz

O script resolvia caminhos relativos apenas a partir da pasta CMS-Gherkin, o que duplicava o prefixo quando o comando era executado do workspace raiz.

### Solucao aplicada

A resolucao de fontes passou a testar caminho absoluto, caminho relativo ao diretorio atual, caminho relativo a CMS-Gherkin e nome dentro de FONTES-ESTRUTURADAS.

### Prevencao

Manter a validacao do gerador em mais de um diretorio de execucao sempre que houver evolucoes no fluxo.

## README com referencias a arquivos inexistentes

- Data: `2026-03-20 18:00:12`
- Categoria: `Documentacao`
- Status: `Resolvido`
- Arquivos relacionados: `README-INICIO-RAPIDO.md`

### Contexto

O inicio rapido listava arquivos auxiliares que nao estavam presentes no pacote entregue.

### Causa raiz

A lista de conteudo do pacote nao foi sincronizada com o conjunto real de arquivos disponiveis.

### Solucao aplicada

Foram removidas do README as referencias a arquivos inexistentes para manter o pacote alinhado com o que realmente pode ser aberto no workspace.

### Prevencao

Revisar a secao 'O que ha neste pacote' sempre que arquivos forem adicionados, removidos ou renomeados.
