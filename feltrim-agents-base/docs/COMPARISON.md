# Comparison - Feltrim Agents Framework vs Alternativas

> Comparacao honesta entre Feltrim Agents Base e outros frameworks
> multi-agente populares em 2026. Cada framework tem um sweet spot
> diferente. Este doc ajuda voce a decidir.

## TL;DR

| Framework | Sweet spot | Nao serve para |
|-----------|-----------|----------------|
| **Feltrim Agents Base** | Times que precisam de governanca real, hierarquia, niveis/certificacoes e separacao core/pack. Producao com auditoria. | Quem so quer prototipo rapido sem governanca. |
| **LangChain / LangGraph** | Encadeamento de LLM calls com state machine, integracao com 200+ tools. Pipelines automatizados. | Quem quer agentes com persona, cultura, hierarquia. |
| **CrewAI** | Squad de agentes com papeis simples (researcher, writer, etc.) executando task list. Rapido de aprender. | Quem precisa de governanca real, niveis, audit trail. |
| **AutoGen (Microsoft)** | Pesquisa academica, conversational AI, code execution sandbox. | Producao com governanca formalizada. |
| **BMAD-METHOD** | Agile com BDD/TDD, ciclos curtos guiados por scrum cerimonias. | Quem precisa de chat-to-artifact promotion ou separacao pack/core. |

## Matriz detalhada

| Caracteristica | Feltrim | LangChain | CrewAI | AutoGen | BMAD |
|----------------|---------|-----------|--------|---------|------|
| **Persona de agente** | Sim, 15 canonicas + custom | Limitado (system prompt) | Sim, simples | Sim | Sim, scrum roles |
| **Hierarquia formal** | Sim (CEO/CIAO/TL/squad) | Nao | Manager/worker basico | Nao | Scrum master/dev/PO |
| **Sistema de niveis** | Sim, N1-N5 com criterios auditaveis | Nao | Nao | Nao | Nao |
| **Certificacoes internas** | Sim, com evidencia auditavel | Nao | Nao | Nao | Nao |
| **Unlocks (habilidades)** | Sim, sistema explicito | Nao | Nao | Nao | Nao |
| **Memoria operacional (brain.md)** | Sim, por agente | Sim, via Memory class | Limitado | Sim | Nao |
| **Rituais de equipe** | Sim, 12 rituais documentados | Nao | Nao | Nao | Sim, scrum cerimonias |
| **Modos de ativacao** (SOLO/PAR/MINI/FULL) | Sim, explicito + anti-patterns | Nao | Nao | Nao | Nao |
| **Token economy explicita** | Sim, severidades T1/T2/T3 | Nao | Nao | Nao | Nao |
| **Separacao core / pack** | Sim, opt-in por dominio | Nao | Nao (tudo em config) | Nao | Nao |
| **Protocolos sistemicos** | Sim, 8 protocolos canonicos | Implicito | Implicito | Implicito | Implicito |
| **Chat-to-artifact governance** | Sim, explicito | Nao | Nao | Nao | Sim, via scrum |
| **Audit de promocao/regressao** | Sim, capability review | Nao | Nao | Nao | Sim, sprint retro |
| **Cultura simbolica vs metricas reais** | Sim, separados por design | Nao se aplica | Nao se aplica | Nao se aplica | Nao se aplica |
| **Vendor lock-in** | Nenhum (markdown puro) | Codigo Python | Codigo Python | Codigo Python | Markdown |
| **Curva de aprendizado** | Media-alta (governanca) | Media (Python + abstrações) | Baixa (configuracao YAML) | Alta (Python + AsyncIO) | Media (scrum) |
| **Producao-ready** | Sim, com governanca | Sim, com codigo proprio | Sim, prototipo a producao | Pesquisa primaria | Sim |
| **Open source** | Proprietaria provisoria (decisao final pendente) | MIT | MIT | MIT | MIT |
| **Linguagem** | Markdown puro (linguagem-agnostic) | Python (TS em beta) | Python | Python | Markdown |

## Quando escolher Feltrim Agents Base

Use se voce precisa de **2 ou mais** destes itens:

1. Multiplos agentes com **papeis distintos** que evoluem ao longo do tempo.
2. **Governanca auditavel** (promocoes com evidencia, capability reviews,
   politicas de seguranca formalizadas).
3. Separacao clara entre **boilerplate generico** e **packs especificos de
   projeto/cliente** sem duplicacao.
4. **Hierarquia clara** com cadeia de escalada (gem -> Beatriz TL -> Sofia
   CIAO -> decisor humano).
5. **Cultura de time** (rituais, escala temporal simbolica, gamificacao
   leve) sem misturar com metricas reais de performance.
6. **Controle de custo de token** explicito (modos SOLO/PAR/MINI/FULL +
   anti-patterns por agente).
7. **Vendor-neutral**: markdown puro, funciona em qualquer LLM (Claude,
   GPT, Gemini, Llama) e qualquer CLI (Claude Code, Cursor, Codex CLI).

## Quando NAO escolher Feltrim Agents Base

- Voce so precisa de chained LLM calls -> use LangChain.
- Voce quer prototipar squad em 30 minutos sem governanca -> use CrewAI.
- Voce esta pesquisando arquitetura agentica academica -> use AutoGen.
- Voce ja tem framework agile maduro e quer adicionar BDD/TDD na squad ->
  use BMAD-METHOD.
- Voce nao precisa de mais que 1 agente -> use qualquer LLM direto sem
  framework.

## Compatibilidade

Feltrim Agents Base eh markdown puro, entao funciona em paralelo com
qualquer outro framework:

- **LangChain pode invocar uma gem do Feltrim** carregando o prompt do
  `core/agents/gem_<slug>.md` como system message.
- **CrewAI agents podem usar o squad Feltrim como referencia** de roles,
  mas precisaria adaptar para a sintaxe do CrewAI.
- **BMAD com Feltrim:** combinacao natural - BMAD para ciclo agile, Feltrim
  para governanca de agentes e packs especificos.

## Decisao via fluxograma

```mermaid
flowchart TD
    Q1{Precisa de governanca<br/>formalizada de agentes<br/>(niveis, certs)?}
    Q2{Trabalha com multiplos<br/>projetos/clientes?}
    Q3{Ja tem framework<br/>agile maduro?}
    Q4{Vai escrever codigo<br/>Python para orquestrar?}

    Feltrim[**Feltrim Agents Base**]:::reco
    FeltrimCore[Feltrim Agents Base<br/>so `core/`]:::reco
    BMAD[BMAD-METHOD]:::other
    LCAG[LangChain<br/>ou AutoGen]:::other
    CrewAI[CrewAI<br/>config YAML]:::other

    Q1 -->|Sim| Q2
    Q1 -->|Nao| Q3

    Q2 -->|Sim| Feltrim
    Q2 -->|Nao| FeltrimCore

    Q3 -->|Sim| BMAD
    Q3 -->|Nao| Q4

    Q4 -->|Sim| LCAG
    Q4 -->|Nao| CrewAI

    classDef reco fill:#1976d2,stroke:#fff,color:#fff,stroke-width:2px
    classDef other fill:#616161,stroke:#fff,color:#fff
```

## Inspiracoes assumidas

O Feltrim Agents Framework absorveu padroes de varios lugares e nao
esconde isso:

- **Hierarquia de governanca** inspirada em estruturas corporativas
  tradicionais (CEO -> CIAO -> TL -> Squad) adaptadas para IA.
- **Capability review** inspirado em performance review de empresas
  maduras + ADR de arquitetura.
- **Rituais simbolicos** inspirados em cultura agile (pre-daily, retro,
  hackathon) mas com guardrail explicito (`governance/RITUALS_GUARDRAILS.md`)
  separando simbolico de real.
- **Protocolos sistemicos** inspirados em "Operating Model" de
  organizacoes (descricao em `core/docs/OPERATING_MODEL.md`) e em padroes
  de message passing de sistemas distribuidos.
- **Token economy** resposta direta a feedback de uso real (Maio/2026)
  apontando consumo excessivo de modelos premium em tarefas taticas.

## Veja tambem

- `README.md` - visao geral
- `docs/GETTING_STARTED.md` - quickstart
- `docs/USE_CASES.md` - casos concretos
- `core/docs/manifesto/FELTRIMS_FRAMEWORK_MANIFESTO.md` - manifesto fundador
- `governance/COMPANY_CHARTER.md` - identidade da empresa adotante
