# Agent Runtime Wrapper

## Objetivo

Definir a ordem correta de composicao da instrucao de um agente na `blueprintv3`.

## Ordem de carga recomendada

1. Contexto do projeto
2. Este wrapper
3. `AGENT_IO_CONTRACT.md`
4. `HANDOFF_PROTOCOL.md`
5. `MEMORY_AND_RAG_POLICY.md`
6. `EVALS_AND_MONITORING.md`
7. Gem do agente
8. Request packet da tarefa

## Principios do runtime

### 1. Papel antes de estilo

Persona ajuda, mas nao substitui fronteira de responsabilidade.

### 2. Contrato antes de eloquencia

Se o output nao for parseavel ou acionavel, ele nao esta pronto.

### 3. Handoff antes de improviso

Se outro agente for necessario, a transicao deve ser explicita.

### 4. Memoria antes de repeticao cega

Recuperar contexto util e melhor do que reinventar a cada chamada.

### 5. Eval antes de promocao

Nenhum comportamento deve ir para uso recorrente sem um minimo de medicao.

## Regra de fallback

Se a tarefa chegar incompleta:

- liste lacunas
- faca assuncoes minimas
- deixe claro o nivel de confianca
- nao invente fatos criticos

## Envelope minimo esperado

Todo agente da v3 deve conseguir responder:

- qual foi o objetivo entendido
- qual foi a decisao tomada
- qual artefato gerado
- quais riscos ficaram abertos
- qual o proximo handoff ou proxima acao
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
