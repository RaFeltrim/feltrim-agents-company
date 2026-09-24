# Guia de Passagem de Conhecimento

Leitura complementar obrigatória: `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.

## 1. Objetivo

Este pacote existe para padronizar a avaliação de USs/PIs e a criação de Gherkins/BDDs no contexto do `CMS-Gherkin`.

O objetivo não é apenas gerar cenários. O objetivo é transformar uma US em um conjunto auditável de artefatos:

- análise detalhada da US
- ACs oficiais consolidados
- rastreabilidade AC -> cenário
- planilha no padrão do time
- arquivo `.feature` pronto para uso

## 2. Estrutura operacional

| Caminho | Finalidade |
|---|---|
| `USs-Avaliar/` | entrada de novas USs ou PIs |
| `FONTES-ESTRUTURADAS/` | fonte unica em JSON por PI/US |
| `Padrao-a-Seguir/` | referência de formato aprovado |
| `Processados_BDD/` | saídas finais em planilha |
| `xray_export/` | saídas em `.feature` |
| `ANALISES/` | análise detalhada e raciocínio de construção |
| `FERRAMENTAS/` | geradores e conversores locais |
| `MEMORIA-OPERACIONAL/` | historico de problemas e solucoes |
| `PROMPT_*.md` | prompts prontos para Gemini, Claude e GPT/Codex |

## 3. Fluxo padrão de trabalho

1. Ler o pacote inteiro antes de gerar qualquer novo artefato.
2. Estudar a US fonte.
3. Extrair contexto funcional, critérios de aceite, regras de negócio, dependências, riscos e massas.
4. Consolidar os ACs oficiais.
5. Criar ou atualizar a fonte em `FONTES-ESTRUTURADAS/`.
6. Gerar análise, planilha e `.feature` com `FERRAMENTAS/gerar_artefatos.py`.
7. Validar a coerência entre planilha, análise e `.feature`.
8. Registrar problemas e soluções em `MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md`.

O fluxo operacional detalhado para novas pastas locais de projeto está em:

- `GUIA-DE-USO-OPERACIONAL-NOVA-PASTA-DE-PROJETO.md`

## 4. O padrão obrigatório de cada PI

Cada PI deve ter, no mínimo:

- `1` documento de análise detalhada em `ANALISES/`
- `1` planilha final em `Processados_BDD/`
- `1` arquivo `.feature` em `xray_export/`

Quando a PI estiver no padrão rico, a planilha deve conter:

- título da PI
- resumo
- dependências principais
- riscos principais
- massas de teste sugeridas
- critérios de aceite consolidados
- temas / pontos de atenção
- tabela de ACs oficiais
- tabela de cenários com `# | Cenário | BDD | AC Relacionado`

## 5. Regras não negociáveis

- analisar o `CMS-Gherkin` antes de qualquer execução
- usar o `Padrao-a-Seguir` como âncora de formato
- manter `100%` de cobertura dos ACs
- preservar mensagens literais quando existirem
- não inventar regras de negócio sem base documental
- reutilizar a fonte estruturada antes de reescrever artefatos
- manter planilha e `.feature` sincronizados
- registrar o raciocínio da construção no documento de análise

## 6. Como extrair valor máximo do repositório

### Fluxo recomendado com 3 modelos

1. `Gemini 3.1 Pro`
   Use para leitura pesada de contexto, decomposição da US e extração inicial.
2. `Claude Opus 4.6`
   Use para blindagem textual, refinamento de nomes e limpeza editorial.
3. `GPT-5.4 / Codex`
   Use para execução final, consistência dos artefatos e organização no repositório.

### Fluxo recomendado com apenas 1 modelo

Se houver pouco tempo, use o prompt operacional do `GPT-5.4 / Codex` para fazer a leitura do pacote, a consolidação e a verificação final em um único fluxo.

### Fluxo recomendado para economia de tokens

Quando o objetivo for reduzir custo e retrabalho, use:

1. `PROMPT_GPT_5_4_ECONOMICO.md`
2. `FONTES-ESTRUTURADAS/MODELO-FONTE-ESTRUTURADA.json`
3. `FERRAMENTAS/gerar_artefatos.py`
4. `FERRAMENTAS/registrar_problema.py`

## 7. Taxa de efetividade e ganho de velocidade

### Dado real observado no acervo

- cobertura funcional alvo: `100%` dos ACs
- rastreabilidade entre análise, planilha e `.feature`
- possibilidade de onboarding rápido com documentação pronta

### Estimativa operacional conservadora

- PI média feita manualmente: `60 a 120 min`
- PI média usando o pacote + prompt correto: `15 a 45 min`
- economia operacional estimada: `50% a 75%`
- taxa de primeira versão estruturalmente aproveitável para revisão: `>= 90%`

### Como medir

- `Taxa de efetividade = (cenários aceitos sem reescrita estrutural / cenários gerados) x 100`
- `Ganho de velocidade = ((tempo manual - tempo com repositório) / tempo manual) x 100`
- `Cobertura real = (ACs cobertos / ACs oficiais) x 100`

## 8. Conduta adotada neste pacote

O método utilizado segue uma disciplina simples e repetível:

1. partir da fonte
2. quebrar a US em blocos funcionais
3. transformar critério em AC verificável
4. transformar AC em cenário rastreável
5. blindar a consistência entre artefatos

Essa conduta está detalhada em `CONDUTA-E-FELTRIMS-FRAMEWORK.md`.

## 9. Resultado esperado para um novo usuário

Mesmo uma pessoa que não conheça o prompt ideal consegue usar o pacote se seguir esta ordem:

1. abrir este guia
2. abrir o arquivo de segurança
3. abrir um dos `PROMPT_*.md`
4. colocar a nova US em `USs-Avaliar/`
5. executar o prompt no modelo escolhido
6. revisar a planilha, o `.feature` e a análise detalhada

## 10. Fechamento

O ganho deste pacote não está apenas em acelerar a escrita. O ganho principal está em reduzir variação entre pessoas, aumentar rastreabilidade, diminuir repetição de tokens e manter o histórico de decisão funcional junto do resultado final.
