# Casos de Uso - Feltrim Agents Base

> 5 casos de uso concretos do framework, com snippet de invocacao e
> resultado esperado. Use como inspiracao para os primeiros experimentos.

## Caso 1 - QA BDD a partir de User Story

**Problema:** Voce tem uma US escrita em texto livre e precisa de cenarios
de teste Gherkin em portugues, com cobertura de happy path + casos de erro
+ regras de negocio.

**Squad:** SOLO. Rafael QA SDET.

**Pack:** `cms-gherkin` (se for projeto recorrente de BDD) ou apenas
`core/agents/gem_rafael_qa.md`.

**Snippet:**

```text
Voce eh gem_rafael_qa.md (QA SDET, N3, certs FA-FOUND + BDD-AUDIT).

Contexto: leia core/agents/gem_rafael_qa.md inteiro.

User Story:
> Como usuario logado, quero alterar minha senha,
> Para manter minha conta segura.
>
> Criterios de aceite:
> - senha atual obrigatoria
> - nova senha tem 12+ caracteres com letra, numero e simbolo
> - apos sucesso, sessao continua valida
> - notificacao por email apos alteracao bem-sucedida

Tarefa: gere arquivo .feature em portugues com:
- 1 cenario happy path
- 2 cenarios de erro (senha atual errada, nova senha fraca)
- 1 cenario de regra de negocio (notificacao enviada)
- 1 cenario de seguranca (rate limit em tentativas)

Use estrutura Dado/Quando/Entao/E. Sem comentarios extras.
```

**Resultado esperado:** Arquivo `.feature` com 5 cenarios pronto para Xray
ou Playwright.

**Custo aproximado:** SOLO, 1 chamada, modelo medio (ex.: Claude Sonnet 4.5 / GPT-4.1).

---

## Caso 2 - Decisao de stack para nova feature

**Problema:** Time vai construir feature nova. Stack tem 3 opcoes
plausiveis (Supabase vs PostgreSQL self-hosted vs Firebase). Precisa de
recomendacao com trade-offs auditaveis.

**Squad:** PAR. Beatriz TL + Aline Cloud.

**Snippet:**

```text
Voce eh gem_beatriz_tl.md (Tech Lead, N4).
Co-piloto: gem_aline_cloud.md (Cloud Architect, N3).

Carreguem core/protocols/HANDOFF_PROTOCOL.md e
core/protocols/DELIVERY_AND_PRODUCT_SURFACES.md.

Contexto: feature de "mural de avisos" com 10k usuarios ativos, leitura
500x mais frequente que escrita, regiao Brasil, time de 2 backend
engineers, orcamento mensal max R$ 800.

Tarefa:
1. Beatriz: liste 3 stacks plausiveis com pro/contra arquitetural.
2. Aline: para cada stack, estime custo mensal + DR posture +
   complexidade operacional.
3. Beatriz: recomende UMA stack e abra ADR completo com:
   - Contexto
   - Alternativas consideradas
   - Decisao
   - Consequencias
   - Reversibilidade

Saida: ADR em markdown.
```

**Resultado esperado:** ADR pronto para PR em `core/docs/adr/`.

**Custo aproximado:** PAR, 2-3 chamadas, modelo medio.

---

## Caso 3 - Code review pre-PR sem code review automatico em init

**Problema:** PR esta pronto, voce quer revisao tecnica especifica focada
em areas onde pode falhar (sem invocar a squad inteira).

**Squad:** SOLO ou PAR, baseado no escopo.

**Anti-pattern (evitar):** convocar Sofia CIAO + Beatriz TL para revisar
um fix de typo. Custa 10x mais do que precisava.

**Snippet (SOLO - PR de backend):**

```text
Voce eh gem_joao_backend.md (Backend Engineer, N3).
Carregue core/protocols/EVALS_AND_MONITORING.md.

PR: <link ou diff abaixo>

Diff:
<colar diff aqui>

Tarefa: review focada em:
- Validacao de input (todo input externo)
- Tratamento de erro (catch generico vs especifico)
- N+1 em queries
- Falta de logs de operacao critica

Saida: 5-10 comentarios objetivos, sem opinioes de estilo. Cada
comentario com:
- linha
- categoria (input / erro / query / log / outra)
- severidade (block / major / minor / nit)
- recomendacao concreta
```

**Resultado esperado:** Lista de comentarios estruturada para colar em
review do GitHub.

**Quando subir para FULL:** se for PR de Go-Live, mudanca de arquitetura
critica, ou se Sofia CIAO ja sinalizou veto em PR similar anterior. Ver
`core/docs/AGENT_ACTIVATION_POLICY.md`.

---

## Caso 4 - Audit Go/No-Go antes de deploy critico

**Problema:** Voce vai fazer deploy em producao em janela de baixo
trafego, mas a feature toca pagamento. Precisa de audit antes.

**Squad:** FULL. Liderada por Sofia CIAO.

**Quando faz sentido FULL:** deploy critico, pos-incidente, mudanca
arquitetural, auditoria de seguranca. Custa caro - so use quando
justificado.

**Snippet:**

```text
Squad convocada (modo FULL):
- gem_sofia_ciao.md (lider, N5, veto tecnico)
- gem_beatriz_tl.md (Tech Lead, N4)
- gem_rafael_qa.md (QA SDET, N3, certs BDD-AUDIT + PLAYWRIGHT-AUDIT)
- gem_camila_devops.md (DevOps, N3)
- gem_joao_backend.md (Backend, N3)

Carreguem core/memory/team-rituals/team-call.md.

Contexto:
- Feature: refatoracao do fluxo de pagamento (PIX + cartao).
- Mudanca em 8 arquivos, ~600 linhas.
- Cobertura de teste atual: 78%.
- Janela de deploy: domingo 03h-05h.
- Plano de rollback: feature flag desligavel em 30s.

Tarefa (rodar nesta ordem):
1. Rafael QA: verifique cobertura de teste especifica para pagamento.
   Lista buracos.
2. Joao Backend: confirme que nenhum endpoint critico mudou contrato.
3. Camila DevOps: confirme que rollback de feature flag esta testado.
4. Beatriz TL: analise se algum trade-off arquitetural ficou em divida
   tecnica.
5. Sofia CIAO: emita veredito Go/No-Go com:
   - Veredito (GO / GO COM RESSALVA / NO-GO)
   - Riscos aceitos
   - Riscos NAO aceitos (block)
   - Acao se algum risco materializar
   - Owner de cada acao

Saida: ata estruturada de team-call.
```

**Resultado esperado:** Ata Go/No-Go publicavel com responsaveis.

**Custo aproximado:** FULL, 5+ chamadas, modelo premium para Sofia
(ex.: Claude Opus 4.5 / GPT-5 / equivalente). ~10x SOLO.

---

## Caso 5 - Onboarding de novo time / novo agente

**Problema:** Voce vai colocar um novo desenvolvedor (humano) para
trabalhar no projeto, e quer que ele entenda o framework Feltrim em
1-2 horas.

**Squad:** PAR. Ana TDAH UX + Marlon PO.

**Snippet:**

```text
Voce eh gem_ana_tdah.md (TDAH UX Ally, N2, certs FA-FOUND).
Co-piloto: gem_marlon_po.md (Product Owner, N3).

Carreguem core/docs/ONBOARDING.md.

Contexto: novo dev backend chegou. Tem 3 anos de experiencia em
TypeScript/Node mas ZERO experiencia com sistemas multi-agente.

Tarefa:
1. Ana: monte trilha de leitura em 5 passos, cada um com:
   - tempo estimado max 15min
   - resumo de 2-3 frases
   - "fica claro se voce conseguir explicar X"
2. Marlon: para cada passo, indique a primeira tarefa real que o dev
   deve executar para validar o aprendizado.

Saida: tabela markdown com colunas: Passo / Tempo / O que ler / Como
validar / Primeira tarefa.
```

**Resultado esperado:** Onboarding personalizado em tabela navegavel.

**Onde guardar:** `core/memory/agents/<novo-dev>/onboarding.md` (se for
agente novo) ou compartilhar com humano direto (se for pessoa).

---

## Anti-patterns recorrentes

Evite esses padroes ou voce gasta token sem agregar valor:

| Anti-pattern | Por que falha | Faca em vez |
|--------------|---------------|-------------|
| "Vou convocar a squad inteira pra ouvir opiniao" | Cada gem custa, sem decisao em jogo nao agrega | Use modo SOLO ou PAR. Convoque FULL so com decisao concreta. |
| "Vou rodar code review automatico em todo PR" | Maioria dos PRs nao precisa de review profunda. Custo recorrente alto. | Trigger review so quando arquivo critico mudar (definir lista). |
| "Sofia CIAO vai opinar nessa decisao tatica" | Sofia eh para Go/No-Go executivo. Em tatico vira ruido. | Use Beatriz TL ou Orchestrator do pack. |
| "Vou convocar team-call pra mudanca de copy" | team-call eh FULL. Copy eh SOLO de Laura. | Convoque so Laura UI ou Ana TDAH. |
| "Vou perguntar pra ver se a gem concorda" | Gem nao "concorda" - executa contrato. | Defina o request packet completo e avalie saida vs scorecard. |

Detalhes em `core/docs/AGENT_ACTIVATION_POLICY.md` e
`core/docs/TOKEN_ECONOMY.md`.

## Veja tambem

- `docs/GETTING_STARTED.md` - 5 minutos do zero ao primeiro agente
- `docs/COMPARISON.md` - vs LangChain, CrewAI, AutoGen, BMAD
- `examples/` - exemplos prontos de spawn de squad
- `core/docs/SQUAD_INDEX.md` - mapa de invocacao por trigger
