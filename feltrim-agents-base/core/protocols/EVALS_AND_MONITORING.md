# Evals and Monitoring

## Objetivo

Dar um minimo de confiabilidade operacional para o sistema de agentes da `blueprintv3`.

## O que medir por resposta

```yaml
response_scorecard:
  schema_adherence: 1-5
  usefulness: 1-5
  factual_grounding: 1-5
  handoff_quality: 1-5
  latency_fit: 1-5
  cost_fit: 1-5
```

## O que medir por agente

- taxa de output reaproveitado sem retrabalho
- taxa de handoff aceito sem devolucao
- taxa de aderencia ao contrato de output
- taxa de risco relevante detectado antes da execucao

## O que logar

Logue pelo menos:

- agente chamado
- tipo de tarefa
- artefatos consumidos
- artefatos gerados
- se houve handoff
- se houve bloqueio
- se algo foi para memoria

## Gates minimos da v3

### Gate de contrato

O output respeitou o envelope combinado?

### Gate de utilidade

A resposta gerou decisao, artefato ou proximo passo claro?

### Gate de risco

Os riscos relevantes foram expostos?

### Gate de colaboracao

Se outro agente era necessario, o handoff ficou claro?

## Regra de promocao

Nao promova um comportamento recorrente para producao se ele:

- quebra schema com frequencia
- alucina fatos criticos
- custa caro demais para o valor gerado
- exige retrabalho manual constante
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
