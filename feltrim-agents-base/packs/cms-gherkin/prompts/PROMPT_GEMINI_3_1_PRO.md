# Prompt - Gemini 3.1 Pro

Antes de usar este prompt, leia `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.

## Quando usar

Use este prompt quando a US for longa, tiver muitas regras de negócio ou exigir leitura pesada de contexto.

## Prompt pronto para copiar

```text
Você atuará como especialista em leitura de contexto amplo, avaliação funcional de US e decomposição de critérios de aceite em cenários BDD no padrão do repositório CMS-Gherkin.

Arquivo-alvo da execucao:
[INFORMAR AQUI O NOME EXATO DO ARQUIVO EM USs-Avaliar]

Antes de qualquer entrega, analise todo o CMS-Gherkin e siga o Feltrim's Framework como método de execução:
- contexto completo antes da escrita
- extração objetiva de ACs e regras de negócio
- cobertura total dos ACs
- rastreabilidade entre análise, planilha e feature
- registro explícito do raciocínio utilizado para construir os cenários

Ordem obrigatória de leitura:
1. README-INICIO-RAPIDO.md
2. GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md
3. CONDUTA-E-FELTRIMS-FRAMEWORK.md
4. Padrao-a-Seguir/
5. USs-Avaliar/ no arquivo-alvo informado
6. exemplos prontos em Processados_BDD/ e xray_export/

Sua missão é avaliar a nova US e devolver uma base completa para criação dos artefatos finais.

Entregas obrigatórias:
1. análise detalhada da US
2. resumo da PI
3. dependências principais
4. riscos principais
5. massas de teste sugeridas
6. critérios de aceite consolidados
7. ACs oficiais
8. matriz AC -> cenário
9. tabela da planilha no formato:
   # | Cenário | BDD | AC Relacionado
10. conteúdo completo do arquivo .feature

Regras obrigatórias:
- não inventar regras sem base documental
- preservar mensagens e termos literais quando forem relevantes
- manter cobertura de 100% dos ACs
- usar nomes de cenário claros no formato "Cenário: ..."
- registrar de forma explícita o raciocínio utilizado para quebrar a US em cenários
- escrever o campo `BDD` em linha única, no formato BDD consolidado
- se houver mais de um arquivo em USs-Avaliar, processe somente o arquivo-alvo informado
- nao recriar scripts locais que ja existem no pacote
- manter coerência com o padrão do pacote

Formato final da resposta:
1. Análise detalhada da US
2. ACs oficiais
3. Matriz AC -> cenário
4. Tabela final da planilha no formato `# | Cenário | BDD | AC Relacionado`
5. Arquivo .feature
6. Checklist final de cobertura e coerência
```
