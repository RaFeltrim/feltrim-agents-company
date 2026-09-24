# Exemplo: benchmark de modelos LLM

> Template para comparar 2-N modelos com **input identico** e medir
> qualidade, latencia e custo. Util quando lancar novo modelo
> (proxima geracao Codex / Claude Opus / GPT / equivalente) e voce
> quer validar antes de adotar.

## Cenario

Novo modelo `<NOVO_MODELO>` acabou de lancar. Voce quer saber se vale
trocar o padrao atual `<MODELO_ATUAL>` por ele em algum modo de
ativacao (SOLO/PAR/MINI/FULL).

## Pre-requisitos

- Acesso a API ou IDE dos modelos a comparar.
- Conjunto de tarefas representativas do seu uso real (3-5 tarefas
  por modo de ativacao).
- Brain do agente envolvido como input controlado (mesma janela de
  contexto pros 2 modelos).
- Tabela de pricing atualizada de cada modelo.

## Metodologia

### 1. Definir as tarefas a testar

Para cada **modo de ativacao** (ver `core/docs/AGENT_ACTIVATION_POLICY.md`),
escolher 1-2 tarefas reais ja resolvidas (para ter ground truth):

| Modo | Tarefa exemplo | Agente | Output esperado |
|------|----------------|--------|------------------|
| SOLO | Ajustar copy de CTA | Laura | 1-3 alternativas com justificativa |
| PAR | Implementar endpoint POST /orders | Joao + Rafael | Plano tecnico + BDD |
| MINI | Feature de exportar CSV | Fabio + Joao + Pedro + Rafael + Claudia | Artefato feature-init |
| FULL | Revisar release v2 (use case us-avaliator) | 14 agentes | 14 relatorios + veredito Sofia |

### 2. Padronizar input

Para cada tarefa:

- Carregar o **mesmo conjunto de gens** em ambos os modelos.
- Usar a **mesma instrucao base** (`example-feature-lean.md` ou
  `example-spawn-team-meeting.md`).
- **Mesma janela de contexto** (mesmo limite de tokens input).
- **Mesma temperatura** (ideal: 0.2 para reduzir variancia).

### 3. Medir saida

Por execucao:

| Metrica | Como medir |
|---------|------------|
| **Qualidade** | Comparar com ground truth: % de pontos cobertos, ausencia de alucinacao, aderencia ao formato esperado |
| **Latencia** | Tempo total entre prompt enviado e resposta completa |
| **Tokens input** | Reportado pela API |
| **Tokens output** | Reportado pela API |
| **Custo USD** | `(tokens_input * price_input + tokens_output * price_output)` |
| **Aderencia a anti-patterns** | Modelo respeitou "nao fazer code review automatico"? Convocou agentes corretos? Aceitou downgrade? |
| **Profundidade de raciocinio** | Identificou risco que ground truth tambem identificou? Sugeriu mitigacao? |
| **Output formal** | Markdown bem estruturado, sem texto duplicado, sem prosa fluffy? |

### 4. Repetir N vezes

3-5 execucoes por tarefa, calcular media e desvio padrao. Modelo bom
e **consistente**, nao so "as vezes brilhante".

### 5. Consolidar

Tabela final:

| Modo / Tarefa | Modelo A | Modelo B | Vencedor | Por que |
|---------------|----------|----------|----------|---------|
| SOLO - copy | <metricas> | <metricas> | <A ou B> | <razao> |
| PAR - endpoint | <metricas> | <metricas> | <A ou B> | <razao> |
| MINI - CSV | <metricas> | <metricas> | <A ou B> | <razao> |
| FULL - release | <metricas> | <metricas> | <A ou B> | <razao> |

### 6. Recomendacao por modo

Para cada modo, definir **modelo default** apos o benchmark:

```text
SOLO: <modelo escolhido> - custo $X/sessao, latencia Y, qualidade Z
PAR: <modelo escolhido> - custo $X/sessao, latencia Y, qualidade Z
MINI: <modelo escolhido> - custo $X/sessao, latencia Y, qualidade Z
FULL operacional (14 agentes): <modelo escolhido>
FULL Sofia consolida: <modelo premium escolhido>
```

Atualizar a tabela em `core/docs/TOKEN_ECONOMY.md` secao "Modelos
sugeridos por modo de ativacao".

## Template de relatorio

```markdown
# Benchmark: <modelo A> vs <modelo B>

**Data:** YYYY-MM-DD
**Executado por:** <decisor humano>
**Repeticoes por tarefa:** N

## Resultados por modo

### SOLO
| Metrica | Modelo A | Modelo B |
|---------|----------|----------|
| Qualidade (0-10) | | |
| Latencia (s) | | |
| Custo/sessao (USD) | | |
| Aderencia anti-pattern | | |
| Vencedor: | | |

### PAR
<idem>

### MINI
<idem>

### FULL
<idem>

## Conclusao

| Modo | Modelo recomendado | Razao |
|------|---------------------|-------|
| SOLO | | |
| PAR | | |
| MINI | | |
| FULL operacional | | |
| FULL Sofia (consolida) | | |

## Ressalvas

- <quando modelo X falha mesmo sendo bom em media>
- <quando vale pagar premium mesmo nao sendo o melhor custo>
- <quando latencia importa mais que qualidade>

## Atualizar

- [ ] `core/docs/TOKEN_ECONOMY.md` tabela "Modelos sugeridos por modo"
- [ ] `DECISIONS_PENDING.md` se houver decisao macro de stack
```

## Anti-patterns no benchmark

- **NAO** comparar com tarefas **diferentes** entre modelos.
- **NAO** comparar com **janelas de contexto diferentes**.
- **NAO** fazer **1 execucao so** (variancia alta).
- **NAO** ignorar **anti-patterns aceitos pelo modelo** (modelo que
  convoca todo mundo "por garantia" estoura custo na producao mesmo
  parecendo bom em benchmark).
- **NAO** julgar so por qualidade — custo importa, latencia importa.
- **NAO** generalizar de 1 tarefa para todos os modos (Codex pode ser
  excelente em PAR tecnico e pessimo em FULL executivo).

## Veja tambem

- `core/docs/TOKEN_ECONOMY.md` - tabela atualizada de modelos por modo
- `core/docs/AGENT_ACTIVATION_POLICY.md` - definicao dos 4 modos
- `examples/example-feature-lean.md` - tarefa exemplo para modo PAR/MINI
- `examples/example-spawn-team-meeting.md` - tarefa exemplo para modo FULL
- `packs/us-avaliator/` - case real de proposta executiva (input pronto para benchmark FULL)
