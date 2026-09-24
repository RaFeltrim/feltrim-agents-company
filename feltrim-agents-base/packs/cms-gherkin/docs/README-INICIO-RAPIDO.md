# CMS-Gherkin - Início Rápido

Leitura complementar obrigatória: `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.

Este pacote foi preparado para treinamento e passagem de conhecimento, com um exemplo totalmente fictício, chamado `Projeto exemplo`.

## O que há neste pacote

- `GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md`
- `GUIA-DE-USO-OPERACIONAL-NOVA-PASTA-DE-PROJETO.md`
- `CONDUTA-E-FELTRIMS-FRAMEWORK.md`
- `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`
- `PROMPT_GEMINI_3_1_PRO.md`
- `PROMPT_CLAUDE_OPUS_4_6.md`
- `PROMPT_GPT_5_4.md`
- `PROMPT_GPT_5_4_ECONOMICO.md`
- `MODO-ECONOMICO-DE-TOKENS.md`
- `FONTES-ESTRUTURADAS/MODELO-FONTE-ESTRUTURADA.json`
- `FERRAMENTAS/gerar_artefatos.py`
- `FERRAMENTAS/registrar_problema.py`
- `MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md`
- `Padrao-a-Seguir/EXEMPLO-PADRAO-APROVADO.md`
- `USs-Avaliar/PROJETO-EXEMPLO.docx`
- `FONTES-ESTRUTURADAS/PROJETO-EXEMPLO.json`
- `ANALISES/PROJETO-EXEMPLO-ANALISE-DETALHADA.md`
- `Processados_BDD/PROJETO-EXEMPLO.xlsx`
- `xray_export/PROJETO-EXEMPLO.feature`

## Como usar em 5 passos

1. Leia `GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md`.
2. Leia `GUIA-DE-USO-OPERACIONAL-NOVA-PASTA-DE-PROJETO.md`.
3. Leia `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.
4. Escolha o prompt do modelo desejado.
5. Gere ou revise a análise detalhada, a planilha e o `.feature`, mantendo cobertura total dos ACs.

## Como gastar menos tokens

Para economizar tokens de forma consistente, prefira este caminho:

1. Leia `MODO-ECONOMICO-DE-TOKENS.md`.
2. Use `PROMPT_GPT_5_4_ECONOMICO.md`.
3. Faça a IA criar ou atualizar `FONTES-ESTRUTURADAS/<NOME>.json`.
4. Gere os artefatos com `FERRAMENTAS/gerar_artefatos.py`.
5. Registre incidentes em `MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md`.

## Fluxo rápido para iniciantes

Se a pessoa nunca usou o pacote, a ordem mais simples é:

1. abrir `README-INICIO-RAPIDO.md`
2. abrir `GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md`
3. abrir `GUIA-DE-USO-OPERACIONAL-NOVA-PASTA-DE-PROJETO.md`
4. abrir `PROMPT_GPT_5_4_ECONOMICO.md`
5. estudar o `Projeto exemplo`
6. substituir o exemplo por uma nova US em `USs-Avaliar/`
7. criar ou atualizar a fonte em `FONTES-ESTRUTURADAS/`
8. gerar os artefatos pelo script local
9. validar se todos os ACs da US foram cobertos

## Critério de pronto

Considere a PI pronta quando existirem, de forma coerente entre si:

- `1` análise detalhada em `ANALISES/`
- `1` planilha final em `Processados_BDD/`
- `1` arquivo `.feature` em `xray_export/`
- `100%` dos ACs oficiais cobertos
- nenhuma regra inventada fora da US
- nenhuma divergência relevante entre análise, planilha e `.feature`

## O que este pacote não leva

- arquivos de teste temporários
- nomes internos de versões de trabalho
- referências diretas a projetos reais
- dados sensíveis
- exemplos de negócio identificáveis

## Referência linguística

Este pacote foi revisado para uso em português do Brasil, com linguagem formal, clara e adequada ao contexto corporativo e de treinamento.
