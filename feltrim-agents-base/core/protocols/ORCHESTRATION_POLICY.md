# Orchestration Policy

## Objetivo

Definir quando trabalhar com um agente, quando montar uma squad e como resolver
conflitos entre especialistas.

## Modos de operacao

### Solo mode

Use quando o problema cabe em um unico dominio.

### Paired mode

Use quando ha dependencia entre duas disciplinas fortemente acopladas.

Exemplos:

- `PO + QA`
- `Frontend + UI/UX`
- `Backend + DBA`

### Squad mode

Use quando a decisao cruza negocio, engenharia, qualidade e entrega.

## Regra do caminho critico

O agente principal deve ser aquele cujo output desbloqueia os demais.

Exemplos:

- sem backlog claro, `PO` abre a fila
- sem arquitetura, `TL` ou `Aline` abre a fila
- sem release gate, `QA` ou `DevOps` abre a fila

## Reuniao de time

Quando o orquestrador pedir uma reuniao de time:

1. escolha de 3 a 6 agentes relevantes
2. cada um responde no proprio dominio
3. uma sintese final consolida convergencias e conflitos
4. conflitos nao resolvidos sobem para `Sofia`

## Politica de conflito

### Conflito de negocio vs tecnologia

`Marlon` e `Beatriz` negociam trade-off. `Sofia` arbitra se o impacto for estrutural.

### Conflito de prazo vs qualidade

`Claudia` e `Rafael` explicitam o risco. `Sofia` decide se o gate pode ser flexibilizado.

### Conflito de arquitetura

`Aline` propÃµe, `Beatriz` detalha, `Sofia` aprova ou veta.
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
