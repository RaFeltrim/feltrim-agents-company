# Guia de Uso Operacional - Nova Pasta de Projeto

Leitura complementar obrigatória: `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.

## 1. Objetivo deste guia

Este guia existe para garantir que qualquer nova pasta de projeto anexada localmente siga o mesmo fluxo operacional, com o mesmo padrão de inserção de arquivos, a mesma confiabilidade de uso e o mesmo aproveitamento do pacote `CMS-Gherkin`.

O objetivo é usar a IA como facilitadora completa do processo, sem abrir mão de controle, rastreabilidade e validação humana.

## 2. Princípio central

A IA não substitui a fonte de verdade do projeto. Ela acelera, organiza, consolida e valida.

Neste fluxo:

- a fonte de verdade continua sendo a documentação funcional anexada
- o `CMS-Gherkin` continua sendo a referência de padrão
- a IA atua como facilitadora de leitura, estruturação, consolidação e verificação
- a aprovação final continua dependendo da revisão funcional do time

## 3. Quando usar este fluxo

Use este fluxo sempre que houver:

- nova US
- nova PI
- nova pasta de projeto com documentos funcionais
- novo conjunto de anexos que precise virar análise, planilha e `.feature`

## 4. Estrutura padrão da nova pasta local

### Estrutura mínima recomendada

```text
Nome-do-Projeto/
  CMS-Gherkin/
    ANALISES/
    FONTES-ESTRUTURADAS/
    FERRAMENTAS/
    MEMORIA-OPERACIONAL/
    Padrao-a-Seguir/
    Processados_BDD/
    USs-Avaliar/
    xray_export/
    README-INICIO-RAPIDO.md
    MODO-ECONOMICO-DE-TOKENS.md
    GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md
    GUIA-DE-USO-OPERACIONAL-NOVA-PASTA-DE-PROJETO.md
    CONDUTA-E-FELTRIMS-FRAMEWORK.md
    SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md
    PROMPT_GEMINI_3_1_PRO.md
    PROMPT_CLAUDE_OPUS_4_6.md
    PROMPT_GPT_5_4.md
    PROMPT_GPT_5_4_ECONOMICO.md
```

## 5. Padrão correto de inserção dos arquivos

### Entrada

Tudo o que chega do negócio deve entrar primeiro em:

- `USs-Avaliar/`

Exemplos:

- `.docx`
- `.pdf`
- `.xlsx` de apoio funcional
- anexos complementares de regra de negócio

### Referência de padrão

Tudo o que servir como exemplo aprovado deve ficar em:

- `Padrao-a-Seguir/`

### Saídas finais

As saídas devem ser separadas assim:

- `FONTES-ESTRUTURADAS/` -> fonte única e reaproveitável da PI/US
- `ANALISES/` -> análise detalhada da US e raciocínio utilizado
- `Processados_BDD/` -> planilha final
- `xray_export/` -> arquivo `.feature`
- `MEMORIA-OPERACIONAL/` -> histórico de problemas, soluções e prevenção

## 6. Fluxo exato e completo de uso

### Etapa 1 - Preparar a pasta local

1. criar ou abrir a pasta do projeto na máquina local
2. garantir que a estrutura `CMS-Gherkin` esteja presente
3. confirmar que os prompts, o guia e o padrão de referência estão dentro da pasta

### Etapa 2 - Inserir a nova documentação

1. copiar a nova US ou PI para `USs-Avaliar/`
2. incluir anexos complementares, se existirem
3. evitar arquivos soltos fora da estrutura

### Etapa 3 - Ler o pacote antes da execução

Ler obrigatoriamente:

1. `README-INICIO-RAPIDO.md`
2. `GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md`
3. `GUIA-DE-USO-OPERACIONAL-NOVA-PASTA-DE-PROJETO.md`
4. `CONDUTA-E-FELTRIMS-FRAMEWORK.md`
5. `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`
6. `MODO-ECONOMICO-DE-TOKENS.md` se o objetivo for reduzir tokens

### Etapa 4 - Escolher a IA

Escolha o modelo conforme o objetivo:

- `Gemini 3.1 Pro` -> leitura pesada e extração inicial
- `Claude Opus 4.6` -> refinamento textual e blindagem
- `GPT-5.4 / Codex` -> execução final, consistência e organização dos artefatos

### Etapa 5 - Executar com o prompt correto

1. abrir o prompt do modelo escolhido
2. mandar a IA analisar todo o `CMS-Gherkin` antes de agir
3. pedir explicitamente:
   - análise detalhada
   - ACs oficiais
   - matriz AC -> cenário
   - planilha no padrão rico
   - tabela de cenários no formato `# | Cenário | BDD | AC Relacionado`
   - `.feature`
   - validação final de cobertura

### Etapa 5A - Modo economico recomendado

Quando o foco for custo e reaproveitamento:

1. abrir `PROMPT_GPT_5_4_ECONOMICO.md`
2. pedir para a IA criar ou atualizar `FONTES-ESTRUTURADAS/<NOME>.json`
3. mandar a IA rodar `FERRAMENTAS/gerar_artefatos.py`
4. mandar a IA registrar qualquer problema em `MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md`

### Etapa 6 - Gerar os artefatos

Ao final da execução, devem existir:

- `ANALISES/NOME-DO-EXEMPLO-ANALISE-DETALHADA.md`
- `Processados_BDD/NOME-DO-EXEMPLO.xlsx`
- `xray_export/NOME-DO-EXEMPLO.feature`

### Etapa 7 - Validar a confiabilidade

Antes de considerar pronto, validar:

- todos os ACs oficiais foram cobertos
- a planilha bate com o `.feature`
- a análise detalhada explica o raciocínio usado
- não houve invenção de regra fora da US
- nomes de arquivos seguem padrão limpo

## 7. Como extrair 100% do potencial do pacote

Para usar o pacote em seu máximo potencial, a recomendação é:

1. nunca pular a leitura do contexto
2. sempre usar o `Padrao-a-Seguir`
3. sempre registrar a análise detalhada
4. sempre manter a rastreabilidade AC -> cenário
5. sempre revisar o resultado final antes de compartilhar

O maior ganho acontece quando a IA é usada em sequência:

1. leitura e decomposição
2. blindagem textual
3. consolidação final no repositório

## 8. Confiabilidade operacional

Este fluxo foi desenhado para aumentar a confiabilidade por meio de:

- padronização de entrada
- separação clara entre entrada, referência e saída
- registro do raciocínio usado
- cobertura funcional obrigatória
- validação cruzada entre artefatos

Isso reduz:

- retrabalho
- perda de contexto
- divergência entre arquivos
- dependência de memória individual
- repetição desnecessária de tokens

## 9. Papel da IA como facilitadora completa

Neste modelo de trabalho, a IA ajuda a:

- ler grande volume de contexto
- consolidar critérios e regras
- organizar os ACs
- montar cenários rastreáveis
- acelerar a geração dos artefatos
- conferir consistência entre entregáveis

Mas ela deve sempre atuar:

- dentro do padrão do `CMS-Gherkin`
- com base documental
- com validação humana final

## 10. Critério de pronto para uma nova pasta de projeto

Considere a nova pasta pronta para uso confiável quando:

- a estrutura `CMS-Gherkin` estiver completa
- a nova US estiver em `USs-Avaliar/`
- os prompts estiverem disponíveis
- existir um exemplo em `Padrao-a-Seguir/`
- as regras de segurança tiverem sido lidas
- o time souber onde entram os arquivos e onde saem os artefatos

## 11. Fechamento

Sim, é possível usar este pacote como fluxo exato e repetível para novas pastas locais de projeto. A condição para isso funcionar com confiabilidade é seguir a estrutura, usar os prompts corretos, manter a rastreabilidade e tratar a IA como aceleradora disciplinada do processo.
