# Token Economy

> Diretrizes para usar o framework sem queimar token a toa. Complementa
> `core/docs/AGENT_ACTIVATION_POLICY.md`.

## Principio

> Token e recurso finito (custo $) e recurso de qualidade (janela de
> contexto). Cada token gasto deve ter contrapartida em qualidade de
> output. **Convocar mais agentes do que o necessario nao melhora resultado
> — ruido nao e qualidade.**

## As 7 regras de economia

### 1. Default: menor modo de ativacao que resolve

Ver `AGENT_ACTIVATION_POLICY.md`. Sempre comecar SOLO ou PAR. Subir so se aparecer divergencia ou complexidade que justifique.

### 2. Nao fazer code review automatico em init

Code review e ativado por:

- Abertura de PR/MR.
- Pre-merge de branch.
- Pos-incidente.

NUNCA por: "comecei a implementar essa feature, alguem revisa o codigo?".

### 3. Reusar contexto entre sessoes

Antes de carregar tudo novamente:

- Verificar se brain do agente (`core/memory/agents/<slug>/brain.md`) ja tem o contexto.
- Verificar se MEMORY.md indice aponta para conteudo relevante.
- So carregar gem completa se for novo invocacao "fria".

### 4. Carga seletiva de protocolos

Os 8 protocolos em `core/protocols/` totalizam centenas de linhas. Carregar so o relevante:

- Implementacao isolada: nenhum protocolo.
- Decisao multi-agente: `AGENT_IO_CONTRACT.md` + `ORCHESTRATION_POLICY.md`.
- Handoff entre agentes: `HANDOFF_PROTOCOL.md`.
- Memoria persistente: `MEMORY_AND_RAG_POLICY.md`.
- Avaliacao: `EVALS_AND_MONITORING.md`.

### 5. Output curto e estruturado

- Tabelas > paragrafos longos.
- Bullet acionavel > prosa explicativa.
- Codigo > descricao em texto do codigo.
- Diagramas Mermaid pequenos > Mermaid de 50+ nos.
- "Faca X" > "Considere talvez avaliar a possibilidade de X dependendo de Y".

### 6. Evitar duplicacao entre agentes

Quando 2 agentes opinam sobre o mesmo ponto:

- Primeiro agente da output completo.
- Segundo agente so diz "concordo com <agente1>" + delta proprio.
- NAO repetir o que o agente anterior ja disse.

### 7. Modelo por escopo

Casar modelo com nivel de criticidade da tarefa (ver tabela abaixo).

## Modelos sugeridos por modo de ativacao

> Tabela baseada em uso real (Maio/2026). Atualizar quando houver Codex 5.4 publicado e benchmarks rodando.

| Modo | Tarefa tipica | Modelo sugerido | Razao |
|------|---------------|-----------------|-------|
| SOLO | Copy/refactor/typo | GPT 5.5 max-high, Claude Haiku 4.5, Gemini 2.5 Flash | Tarefa simples, modelo barato resolve |
| PAR | Feature pequena, bug fix | GPT 5.5 max-high, Claude Sonnet 4.6, Codex 5.4 (quando publicado) | Bom custo/qualidade |
| MINI-SQUAD | Feature media multi-area | Claude Sonnet 4.6, GPT 5.5 max-high, Codex 5.4 | Janela maior, raciocinio cross |
| FULL TEAM (operacional) | Maioria dos agentes | GPT 5.5 max-high ou Claude Sonnet 4.6 | Custo controlado em volume |
| FULL TEAM (Sofia CIAO consolida) | Veredito final/Go-Live | Claude Opus 4.6 ou GPT 5.5 high-thinking | Qualidade premium so para consolidacao |
| Auditoria de IP / arquitetura critica | Sofia + Beatriz + Aline | Claude Opus 4.6 | Maior profundidade de raciocinio |

> Combinar **modelos baratos para os 14 agentes operacionais + modelo premium so para Sofia CIAO consolidar** reduz custo em ~70% sem perder qualidade no veredito final.

## Anti-patterns que estouram conta

| Anti-pattern | Custo extra | Mitigacao |
|--------------|-------------|-----------|
| Carregar todo `core/agents/*.md` em sessao de 1 feature | +50k-200k tokens | Carregar so as gens relevantes (Modo PAR/MINI) |
| Code review automatico em todo commit | +20k-100k tokens por iteracao | Code review so em PR/merge |
| Re-carregar contexto a cada turno | +10k-50k tokens por turno | Usar memoria/brain ou referencia curta |
| Pedir output completo quando so o delta importa | +30%-70% por resposta | Pedir "so o que mudou desde X" |
| Convocar Sofia CIAO em decisao tatica | +modelo premium gasto a toa | Sofia so em estrategico/Go-Live |
| Team-call para mudar copy | tudo desperdicado | Usar Modo SOLO (Laura ou Ana) |
| Aceitar agente que so diz "ok, concordo" | tokens gastos sem decisao | Forcar agente a justificar OU sair da convocacao |
| Repetir convocacao identica entre features parecidas | N x mesmo custo | Transformar em ritual com gem dedicada ou script |

## Metricas sugeridas (opcional)

Por sessao:

- `modo_ativacao`
- `agentes_invocados` (lista)
- `agentes_que_contribuiram_com_delta` (lista)
- `tokens_input_estimados`
- `tokens_output_estimados`
- `modelo_usado`
- `deliverable_path`
- `decisao_tomada` (sim/nao)

Por semana / sprint:

- Custo total em USD (por modelo).
- % de sessoes em cada modo (SOLO/PAR/MINI/FULL).
- Razao "agentes_invocados / agentes_que_contribuiram" (ideal: ~1).
- Token cost por feature entregue.
- Token cost por bug resolvido.

> Estas metricas sao **operacionais**, nao "XP de agente". Ver
> `governance/RITUALS_GUARDRAILS.md` para a separacao simbolico vs
> operacional.

## Quando vale a pena gastar mais

Token nao e o unico custo. As vezes gastar mais salva muito:

| Situacao | Vale FULL TEAM mesmo caro |
|----------|---------------------------|
| Release de mudanca arquitetural | Sim. Custo de 1 bug em prod >> custo de 50k tokens |
| Pos-incidente critico | Sim. Aprendizado vale o token |
| Decisao com impacto > 6 meses | Sim. Reduz risco de retrabalho |
| Auditoria de compliance | Sim. Custo regulatorio >> token |
| Demo/proposta executiva (us-avaliator case) | Sim. Esta na cara do cliente |

## Veja tambem

- `core/docs/AGENT_ACTIVATION_POLICY.md` — os 4 modos detalhados
- `core/docs/SQUAD_INDEX.md` — "Quando NAO invocar" por agente
- `core/memory/team-rituals/feature-init.md` — ritual lean
- `examples/example-feature-lean.md` — caso PAR/MINI
- `examples/example-model-benchmark.md` — template para comparar modelos
- `governance/SECURITY_AND_PRIVACY.md` — consumo de token como risco operacional
