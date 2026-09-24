# Delivery and Product Surfaces

## Objetivo

Definir como o trabalho dos agentes vira artefato utilizavel por humanos,
processos ou superficies de produto.

## Tipos de entrega

### 1. Human-readable

- markdown
- ADR
- backlog
- status report
- QA plan

### 2. Machine-readable

- JSON
- YAML
- CSV
- contract specs

### 3. Execution-ready

- codigo
- config
- pipeline
- migration
- test suite

### 4. Product surface

- CLI
- bot de chat
- dashboard
- webhook/API
- painel interno

## Regra de empacotamento

Toda entrega deveria deixar claro:

- nome do artefato
- publico alvo
- formato
- local de uso
- se e final ou rascunho

## Canais recomendados

- `Markdown` para decisao e leitura humana
- `JSON/YAML` para consumo de sistema
- `ZIP` quando o pacote precisa viajar como unidade unica
- `Bot/UI` quando o output precisa virar produto recorrente

## Productization checklist

Antes de transformar um fluxo em produto:

1. contrato de entrada definido
2. contrato de saida definido
3. logs minimos definidos
4. estrategia de memoria definida
5. fallback humano definido
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
