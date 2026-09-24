# Exemplo de Padrão Aprovado

Este arquivo existe para mostrar o formato esperado dos artefatos do pacote.

## Estrutura mínima da planilha

- título da PI
- resumo
- dependências principais
- riscos principais
- massas de teste sugeridas
- critérios de aceite consolidados
- tabela de ACs oficiais
- tabela de cenários no formato `# | Cenário | BDD | AC Relacionado`

## Exemplo de linha de cenário

| # | Cenário | BDD | AC Relacionado |
|---|---|---|---|
| 1 | Processamento do exemplo | Dado um contexto válido Quando o processamento for executado Então o resultado esperado deve ocorrer | AC 1 |

## Regras

- todo cenário deve estar ligado a pelo menos um AC
- o campo `BDD` deve estar em linha única
- a análise detalhada deve explicar o raciocínio de construção
- planilha e `.feature` devem ser coerentes entre si
