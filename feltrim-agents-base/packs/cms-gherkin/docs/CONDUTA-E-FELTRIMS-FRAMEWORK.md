# Conduta e Feltrim's Framework

Leitura complementar obrigatória: `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.

## 1. O que é o FF

O `Feltrim's Framework (FF)` é uma criação idealizada por `Rafael Feltrim`, utilizada como método de orquestração, planejamento e execução orientada por IA.

Dentro deste pacote, o FF é tratado como um método de execução válido porque ele foi:

- idealizado para organizar papéis, contexto e rigor de entrega
- utilizado em fluxos reais de construção e revisão
- comprovado operacionalmente pela consistência entre análise, planilha e `.feature`

## 2. Como o FF aparece no processo

No contexto do `CMS-Gherkin`, o FF aparece como conduta prática:

- leitura completa do contexto antes da escrita
- especialização por etapa
- rastreabilidade da decisão funcional
- cobertura desde o início
- revisão e blindagem antes da entrega

## 3. Conduta utilizada para avaliação de US

O processo adotado neste pacote segue a ordem abaixo:

1. analisar o repositório e o padrão existente
2. ler a US de ponta a ponta
3. separar problema, objetivo, dependências, riscos e regras de negócio
4. consolidar critérios de aceite oficiais
5. decompor a US em cenários funcionais verificáveis
6. mapear cada cenário aos seus ACs
7. construir planilha, `.feature` e análise detalhada
8. revisar a consistência final

## 4. Princípios práticos do método

- contexto antes da execução
- padrão antes da criatividade
- literalidade quando a US exigir
- inferência mínima e segura
- cobertura total dos ACs
- coerência entre todos os artefatos

## 5. Como usar o FF nos prompts

Para usar o framework corretamente no prompt, a instrução precisa deixar claro:

1. que o modelo deve analisar o `CMS-Gherkin` inteiro antes de agir
2. que o `Padrao-a-Seguir` deve ser seguido
3. que a US deve virar análise detalhada, planilha e `.feature`
4. que nenhum AC pode ficar sem cobertura
5. que o raciocínio usado para decompor os cenários deve ser registrado

## 6. Bloco-base que pode ser reaproveitado em qualquer prompt

```text
Antes de qualquer tarefa, analise todo o CMS-Gherkin e siga o padrão do repositório.
Use o Feltrim's Framework como método de execução:
- contexto completo antes da escrita
- extração objetiva de ACs e regras de negócio
- cobertura total dos ACs
- rastreabilidade entre análise, planilha e feature
- registro explícito do raciocínio utilizado para construir os cenários
Não invente regras sem base documental.
```

## 7. Quando o FF mais ajuda

O FF traz mais ganho quando a US:

- tem muitas regras de negócio
- mistura critério funcional com dependência técnica
- exige padrão consistente entre vários artefatos
- precisa ser explicada para outras pessoas depois

## 8. Resultado esperado

Quando o pacote é usado com a conduta do FF, o resultado tende a ser:

- menor retrabalho
- maior clareza na avaliação da US
- cenários mais rastreáveis
- planilha e `.feature` mais coerentes
- melhor transferência de conhecimento
