# Agent Levels and Certifications

> Documento canonico do Feltrim Agents Framework. Define a matriz de niveis
> operacionais dos agentes (N1-N5) e o sistema de certificacoes internas que
> reconhece competencias auditaveis ao longo da evolucao do agente.
>
> Origem: consolidacao de documentos internos + governanca Feltrim.

## Matriz de niveis

| Nivel | Nome | Autonomia | Tipo de tarefa | Supervisao necessaria |
|-------|------|-----------|----------------|----------------------|
| **N1** | Operacional assistido | Baixa | Execucao guiada de tarefas bem delimitadas com prompt detalhado | Revisao humana em cada saida |
| **N2** | Especialista de execucao | Media | Execucao de bloco funcional recorrente com guardrails e evidencia | Revisao por amostragem |
| **N3** | Senior / SR autonomo | Alta | Analise de trade-offs, identificacao de riscos, recomendacao com justificativa | Revisao apenas em decisao critica |
| **N4** | Lead / Orquestrador | Alta+ | Coordenacao de multiplos agentes, consolidacao de divergencias, plano de trabalho | Revisao apenas em decisao estrategica |
| **N5** | Auditor executivo / Go-No-Go | Maxima | Veto tecnico, auditoria de decisao final, recomendacao de continuidade ou interrupcao | Revisao humana apenas para overrides |

## Mapeamento de niveis para gens core

| Agente | Nivel default | Justificativa |
|--------|---------------|---------------|
| Sofia - CIAO | N5 | Veto executivo, gate Go-Live, auditoria de PR critico |
| Beatriz - TL | N4 | Coordena decisoes tecnicas multi-agente, abre ADRs |
| Aline - Cloud Architect | N3 | Recomenda arquitetura com trade-offs auditaveis |
| Marlon - PO | N3 | Decide priorizacao com WSJF, mas escala mudanca de roadmap |
| Claudia - PM | N3 | Detecta blockers e propoe replanejamento, escala dependencia externa |
| Camila - DevOps | N3 | Define rollback, escala deploy critico para CIAO |
| Joao - Backend | N3 | Implementa APIs/RPA, escala operacao destrutiva ou credencial nova |
| Fabio - Frontend | N3 | Implementa UI critica, escala mudanca de stack |
| Emerson - Supabase | N3 | Cria migrations RLS, escala schema irreversivel |
| Pedro - DBA | N3 | Recomenda indices/materialized views, escala particionamento >100M |
| Mariana - Prompt | N3 | Refatora system prompts, escala mudanca de provedor |
| Rafael - QA | N3 | Define estrategia de teste, abre bug critico, escala risco residual |
| Laura - UI/UX | N3 | Define tokens e microcopy, escala rebranding |
| Cleber - Mobile | N2 | Implementa PWA / mobile-first, escala arquitetura mobile completa |
| Ana - TDAH UX | N2 | Revisa onboarding/microcopy, escala mudanca de fluxo |

## Mapeamento sugerido para gens de pack

| Categoria | Nivel sugerido |
|-----------|----------------|
| QA Orchestrator de pack | N4 |
| Agentes operacionais de pack (CT execution, retest, evidence, status report) | N2-N3 |
| Playwright / RPA Runner de pack | N2 |
| Dashboard / consolidador de pack | N3 |
| Documentador / changelog de pack | N2 |

## Sistema de certificacoes

Certificacoes internas reconhecem competencias auditaveis. Cada certificacao
tem:

- **Codigo curto** (ex.: `FA-FOUND`, `BDD-AUDIT`).
- **Nome longo**.
- **Pre-requisitos** (nivel minimo + outras certs).
- **Evidencia exigida** (artefatos auditaveis para conquista).
- **Validade** (sem expiracao por default; pode haver re-certificacao se
  framework mudar).

Catalogo completo em `core/docs/AGENT_CERTIFICATIONS.md`. Politica de quem
emite e revoga em `governance/CERTIFICATION_POLICY.md`.

## Sistema de unlocks (habilidades desbloqueadas)

Unlocks sao habilidades operacionais que o agente pode usar sem autorizacao
nova depois que conquistou. Sao mais granulares que certificacoes - cada
unlock e uma acao especifica.

Catalogo completo em `core/docs/AGENT_UNLOCKS.md`.

## Promocao entre niveis

Promocao requer:

1. **Capability review** preenchida (template em
   `core/memory/agents/_templates/agent-capability-review-template.md`).
2. **Evidencias auditaveis** dos criterios para o nivel almejado
   (ver `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md`).
3. **Aprovacao**: Sofia CIAO (revisor agente) + decisor humano.

Promocao NUNCA acontece por antiguidade ou por presenca em rituais. So por
evidencia.

## Relacao com cultura simbolica

Niveis, certificacoes e unlocks sao reais (auditaveis, com efeito
operacional). XP, badges, escala temporal e rituais sao simbolicos (ver
`core/memory/agents/time-scale.md` e
`governance/RITUALS_GUARDRAILS.md`).

Nao confundir os dois sistemas: XP nao promove agente; capability review
promove. Ritual nao certifica agente; evidencia auditavel certifica.
