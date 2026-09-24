<!-- origem: <gherkin-manager-source>/Proposta_Final_Substituicao_Copilot.md -->
<!-- migrada para pack us-avaliator em 2026-05-16: valores em moeda local, nomes de equipe e tamanho de time redigidos para placeholders. Autoria de Rafael Feltrim preservada apenas em credits e rodape conforme governance/SECURITY_AND_PRIVACY.md. -->
<!-- nota sobre modelos LLM: identificadores como "GPT-5.4 nano/mini/full" representam a notacao interna usada na epoca de criacao da Proposta para distinguir geracoes/linhas de modelo (ex.: "Codex no VS Code" linha 4.x). Substitua pelos nomes reais disponiveis na sua conta no momento da execucao. -->

# Proposta Executiva — Substituição das Licenças Copilot Pro por APIs de IA para o Studio de QA

**De:** Rafael Feltrim — QA Engineer  
**Para:** <lider> — Liderança  
**Data:** 24 de Março de 2026  
**Assunto:** Substituição das <N licencas> Copilot Pro por stack de IA dedicado ao Ecossistema de Aceleradores QA  
**Classificação:** Proposta de Otimização de Custos + Plataforma de Aceleração do Studio de QA

---

## Resumo Executivo

Proponho **cancelar as <N licencas> do Copilot Pro** (usadas exclusivamente por QAs) e redirecionar o orçamento para **APIs de IA por token + um servidor Ollama local** (usando infraestrutura local existente), alimentando um **ecossistema de aceleradores QA** — não apenas uma ferramenta, mas uma plataforma completa.

**Resultado:**
- De **~<custo-redigido>** (Copilot Pro) para **~<custo-redigido>** (APIs + servidor local mantido)
- **Economia estimada: ~<custo-redigido>**
- **Mesma chave de API** alimenta múltiplos aceleradores: Gherkin Manager, Kanban QA, Dashboard Executivo e mais
- Capacidades que o Copilot Pro **não oferece**: análise de US, geração de Gherkin, Guard-Rails BDD, Kanban inteligente, status reports automáticos, integração Jira/Zephyr, conformidade LGPD via processamento local

---

## 1. O Problema: Copilot Pro × Necessidades do Studio de QA

| O que os QAs precisam | Copilot Pro entrega? | Gherkin Manager + APIs entrega? |
|:---|:---:|:---:|
| Analisar User Stories (completude, ambiguidade) | ❌ | ✅ |
| Criar/sugerir User Stories (formato Como/Quero/Para) | ❌ | ✅ |
| Gerar cenários Gherkin (Dado/Quando/Então) | Genérico, sem padrão | ✅ Com Feltrim's Framework |
| Gerar BDDs no padrão Processados_BDD | ❌ | ✅ |
| Guard-Rails de vocabulário (proibir API, JSON, SQL) | ❌ | ✅ 48 padrões regex |
| Exportar para Zephyr Scale (CSV/HTML) | ❌ | ✅ |
| Integrar com Jira/Azure DevOps | ❌ | ✅ Via extensão Chrome |
| Processamento on-premises (compliance LGPD) | ❌ | ✅ Via Ollama local |

**Conclusão:** Estamos pagando **~<custo-redigido>** por uma ferramenta genérica de autocomplete de código que **não atende nenhuma das necessidades específicas de QA**.

---

## 2. A Solução Proposta

### Gherkin Manager + Feltrim's Framework + IA

```
Fluxo proposto para os <N QAs>:

  QA abre US no Jira/Azure (via Extensão Chrome no navegador)
       │
       ▼
  Extensão extrai texto da US com 1 clique
       │
       ▼
  Back-end (FastAPI) recebe a US e:
       │
       ├─── [1] Avalia qualidade da US (completude, ambiguidade, testabilidade)
       ├─── [2] Sugere melhorias na US (se necessário)
       ├─── [3] Gera cenários Gherkin (Dado/Quando/Então)
       ├─── [4] Aplica Guard-Rails (Feltrim's Framework — agnosticismo + foco funcional)
       ├─── [5] Formata no padrão Processados_BDD
       └─── [6] Exporta CSV Zephyr / HTML para revisão
       │
       ▼
  QA recebe tudo no Side Panel do navegador
  → Copiar, editar ou enviar direto para Zephyr Scale
```

### Ownership e Manutenção

| Papel | Responsável | Escopo |
|:---|:---|:---|
| **Owner técnico** | Rafael Feltrim | Código Python, Guard-Rails, prompts, integrações de IA |
| **Owner de negócio** | <lider> | Priorização, aprovação de mudanças, budget |
| **Documentação** | autor + <lider> (revisor) | Documentação completa de manutenção, onboarding, troubleshooting |
| **Suporte ao time** | Rafael + documentação self-service | Onboarding de QAs, FAQ, guia de uso da extensão |

> Toda a documentação de manutenção será entregue junto com o sistema, garantindo continuidade mesmo em caso de rotação do time.

---

## 2.1. Ecossistema de Aceleradores QA — Uma Chave, Múltiplos Retornos

A infraestrutura de APIs não serve apenas ao Gherkin Manager. A **mesma chave de API** e o **mesmo back-end** podem alimentar diversos aceleradores que pretendemos construir e melhorar para o Studio de QA:

```
                    ┌─────────────────────────────────────────────┐
                    │        BACK-END COMPARTILHADO (FastAPI)      │
                    │    Groq / Qwen / Gemini / Ollama (local)    │
                    │         Mesma chave de API para tudo        │
                    └──────────┬──────────┬──────────┬────────────┘
                               │          │          │
              ┌────────────────┤          │          ├────────────────┐
              ▼                ▼          ▼          ▼                ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │   GHERKIN    │  │  KANBAN QA   │  │  DASHBOARD   │  │  FUTUROS     │
    │   MANAGER    │  │ INTELIGENTE  │  │  EXECUTIVO   │  │ ACELERADORES │
    └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
```

### Aceleradores Planejados

| # | Acelerador | O que faz | Como a IA ajuda | Status |
|:---:|:---|:---|:---|:---:|
| 1 | **Gherkin Manager** | Analisa US, gera cenários BDD, aplica Guard-Rails, exporta CSV/HTML Zephyr | Geração e validação de Gherkin via IA | 🟢 Funcional |
| 2 | **Kanban QA** | Organização do time de QA: tarefas, prioridades, bloqueios, alocação | IA sugere priorização com base em risco, dependências e carga de trabalho | 🟡 Planejado |
| 3 | **Dashboard Executivo** | Status reports automáticos para liderança, consolidação de métricas QA | IA gera resumos executivos a partir de planilhas/dados de teste atualizados | 🟡 Planejado |
| 4 | **Processados_BDD Avançado** | Nosso padrão interno de entrega BDD, com rastreabilidade completa | IA formata e valida saídas no padrão da empresa | 🟡 Melhoria |

### Detalhamento dos Novos Aceleradores

#### 📋 Kanban QA Inteligente

| Funcionalidade | Descrição |
|:---|:---|
| Board visual | Colunas: Backlog → Em Análise → Em Teste → Review → Done |
| Distribuição de carga | IA analisa velocidade de cada QA e sugere redistribuição |
| Alertas de bloqueio | IA identifica tarefas paradas há mais de X dias e alerta |
| Priorização por risco | IA cruza criticidade da US com histórico de defeitos |
| Relatório semanal | Gera resumo semanal automático da produtividade do time |

#### 📊 Dashboard Executivo com Status Reports

| Funcionalidade | Descrição |
|:---|:---|
| Consolidação de métricas | Puxa dados de planilhas existentes e consolida automaticamente |
| Status report automático | IA gera texto executivo: "Esta semana, X cenários criados, Y US analisadas, Z bloqueios" |
| Visão por sprint | Gráficos de progresso, cobertura de cenários, velocidade do time |
| Atualização via planilha | QAs atualizam planilha existente → dashboard reflete em tempo real |
| Export para e-mail/PPT | Gera relatório pronto para enviar à liderança |

### Impacto no Custo: Zero Adicional

| Item | Custo adicional |
|:---|:---:|
| Nova chave de API para Kanban | **<custo-redigido>** — usa a mesma chave |
| Nova chave de API para Dashboard | **<custo-redigido>** — usa a mesma chave |
| Chamadas extras de IA (est.) | **+<custo-redigido>** (marginal) |
| Desenvolvimento | tempo do autor + documentação |

> **Ponto-chave para o <lider>:** Estamos propondo uma **plataforma**, não uma ferramenta isolada. Cada novo acelerador que construirmos usa a mesma infraestrutura de IA já aprovada — sem custo adicional de licença, sem nova aprovação de vendor, sem novo contrato.

---

## 3. Comparativo Completo de Provedores — Todos os Ecossistemas

### Metodologia
- **Preços oficiais** por 1M tokens (data: 24/03/2026)
- **Custo normalizado:** 400 tokens input + 400 tokens output por chamada
- **Benchmarks reais** executados no 98_Gherkin-Manager com o prompt vencedor
- **Conversão Qwen:** CNY → USD usando 1 CNY ≈ $0.1447 (ref. 06/03/2026)
- **Conversão geral:** USD → BRL usando $1 ≈ <custo-redigido>

| # | Provedor | Modelo | $/1M in | $/1M out | $/chamada | <custo-mensal-redigido> (<N QAs>)¹ | Benchmark | Leitura |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | **Groq** ⭐ | llama-3.1-8b | $0.05 | $0.08 | $0.000052 | **<custo-redigido>** | ✅ 100/100, 1.21s | **Melhor custo-benefício** |
| 2 | **Ollama** | Llama 3.1 8B (local) | $0 | $0 | $0 | **<custo-redigido>**² | Não medido | Dados ficam na empresa |
| 3 | **Qwen** | qwen-turbo (intl) | ~$0.053 | ~$0.212 | $0.000106 | <custo-redigido> | ✅ 100/100, 11.65s | Barato, lento |
| 4 | **Gemini** | 2.5 Flash-Lite | $0.10 | $0.40 | $0.000200 | <custo-redigido> | ✅ 100/100, 1.82s | Melhor opção Google |
| 5 | **Groq** | qwen3-32b | $0.29 | $0.59 | $0.000352 | <custo-redigido> | ✅ 100/100, 1.40s | Bom, perde pro Llama |
| 6 | **OpenAI** | GPT-5.4 nano | $0.20 | $1.25 | $0.000580 | <custo-redigido> | Não medido | Entrada barata OpenAI |
| 7 | **Qwen** | qwen-plus (intl) | ~$0.425 | ~$1.274 | $0.000680 | <custo-redigido> | ✅ 100/100, 11.82s | Sem vantagem vs Turbo |
| 8 | **Gemini** | 3 Flash Preview | $0.50 | $3.00 | $0.001400 | <custo-redigido> | Não medido | Menos eficiente |
| 9 | **OpenAI** | GPT-5.4 mini | $0.75 | $4.50 | $0.002100 | <custo-redigido> | Não medido | Ponte custo/qualidade |
| 10 | **Anthropic** | Claude Haiku 4.5 | $1.00 | $5.00 | $0.002400 | <custo-redigido> | Não medido | Menor custo Anthropic |
| 11 | **Gemini** | 3 Pro Preview | $2.00 | $12.00 | $0.005600 | <custo-redigido> | Não medido | Forte, caro para BDD |
| 12 | **OpenAI** | GPT-5.4 (full) | $2.50 | $15.00 | $0.007000 | <custo-redigido> | Não medido | Para casos difíceis |
| 13 | **Anthropic** | Claude Sonnet 4.6 | $3.00 | $15.00 | $0.007200 | <custo-redigido> | Não medido | Excelente, caro |
| 14 | **Anthropic** | Claude Opus 4.6 | $5.00 | $25.00 | $0.012000 | <custo-redigido> | Não medido | Premium absoluto |
| — | **Copilot Pro** | (assinatura) | — | — | ~$0.027 | **<custo-redigido>** | N/A | **Referência atual** |

¹ *Estimativa: 15 US/QA/dia × <N QAs> × 30 dias = ~13.500 chamadas/mês*  
² *Custo de operação do PC (energia + internet + manutenção), detalhado na seção 4*

### Fator de Economia vs Copilot Pro

```
Groq llama-3.1-8b      <custo-redigido>   → 921x mais barato que Copilot Pro
Qwen Turbo (intl)       <custo-redigido>   → 450x mais barato que Copilot Pro
Gemini 2.5 Flash-Lite   <custo-redigido>   → 238x mais barato que Copilot Pro
Ollama (PC local)       <custo-redigido>   →   9x mais barato que Copilot Pro  
GPT-5.4 (full)          <custo-redigido>   →   6x mais barato que Copilot Pro
Copilot Pro             <custo-redigido>   → referência
```

---

## 4. Ollama no PC Existente — Cálculo de Custo Real

### Hardware Disponível (servidor on-premises dedicado)

| Componente | Especificação | Observação |
|:---|:---|:---|
| CPU | Intel i7 3770 (4C/8T, 3.4GHz) | 3ª geração, TDP 77W |
| RAM | 16 GB DDR3 | Suficiente para Llama 3.1 8B (~8GB necessários) |
| GPU | AMD RX 550 4GB | **Sem suporte ROCm** — IA rodará apenas em CPU |
| Disco | 1 TB HDD | Funcional, mas lento para carga de modelos |
| Valor residual | ~<custo-redigido> (ocioso) | **Sem custo de aquisição** |

### Performance Estimada (Ollama em CPU)

| Métrica | Estimativa | Observação |
|:---|:---|:---|
| Latência por resposta | **20-45 segundos** | Aceitável para processamento de US sensíveis |
| Throughput | ~1-2 req/minuto | Suficiente para demanda de compliance |
| Capacidade diária (8h) | **~80-120 requisições/dia** | Atende confortavelmente <N QAs subset> trabalhando com US sensíveis |
| Capacidade mensal | **~1.600-2.400 req/mês** | Com folga para picos de demanda |
| Modelos suportados | Llama 3.1 8B, Qwen2 7B, Mistral 7B | Modelos compactos e eficientes |

### Custo Mensal de Operação

| Item | Cálculo | Custo/mês |
|:---|:---|:---:|
| **Energia elétrica** | ~180W × 24h × 30d = <consumo-redigido> × <custo-redigido>/kWh¹ | **~<custo-redigido>** |
| **Nobreak (UPS)** | 1500VA (~1-2h de autonomia a 180W) = amortizado em 24 meses² | **~<custo-redigido>** |
| **Manutenção técnica** | Manutenção preventiva e corretiva pelo técnico responsável (limpeza, monitoramento, troubleshooting, atualizações de SO e modelos, reposição de peças, garantia de uptime)³ | **~<custo-redigido>** |
| **Internet** | Fração proporcional do plano de internet dedicada ao servidor (banda e disponibilidade 24/7)⁴ | **~<custo-redigido>** |
| **Hospedagem física** | Já está no local, sem rack ou datacenter | <custo-redigido> |
| **Software** | Ollama é open-source, OS pode ser Linux gratuito | <custo-redigido> |
| **Total** | | **~<custo-redigido>** |

¹ *Tarifa média Brasil 2026 com bandeira amarela, incluindo ICMS. Varia por estado e distribuidora.*  
² *Nobreak 1500VA (ex: SMS, APC Back-UPS Pro) suporta ~1-2h com carga de 180W. Troca de bateria a cada ~2 anos.*  
³ *Rafael Feltrim é técnico em hardware e responsável pela operação contínua do servidor. Inclui: inspeção mensal de hardware, troca de pasta térmica, monitoramento de logs, atualização de modelos de IA e sistema operacional, reposição de componentes, troubleshooting de falhas.*  
⁴ *Fração proporcional do plano de internet residencial, considerando que o servidor exige banda e disponibilidade contínua.*

### Quando o Ollama Local Faz Sentido

| Cenário | Ollama local (on-premises) | API cloud (Groq/Qwen) |
|:---|:---:|:---:|
| **Compliance LGPD / dados sensíveis** | ✅ Dados nunca saem da empresa | ⚠️ Dados vão para cloud de terceiros |
| **Custo por token** | $0 | $0.000052+ |
| **Custo fixo mensal** | ~<custo-redigido> | ~<custo-redigido> |
| **Latência** | 20-45s | 1.2-1.8s |
| **Disponibilidade** | ✅ 24/7 com nobreak e manutenção técnica dedicada | ✅ SLA do provedor |
| **Capacidade** | <N QAs subset> simultâneos (~120 req/dia) | ✅ <N QAs> simultâneos |

> **Veredicto Ollama:** Viável como **servidor de privacidade/compliance** para USs com dados sensíveis. Complementa as APIs cloud cobrindo o gap de LGPD, com capacidade para atender <N QAs subset> por dia e folga para picos — usando infraestrutura local existente.

---

## 5. Compliance e LGPD

> Considerando que User Stories podem conter dados sensíveis de clientes:

| Camada | Solução | Dados saem da empresa? |
|:---|:---|:---:|
| **Processamento padrão** | Groq/Qwen/Gemini (cloud) | Sim — dados transitem pela API |
| **Processamento sensível** | Ollama local (servidor on-premises dedicado) | **Não — tudo on-premises** |
| **Guard-Rails** | guardrails.py (local, Python) | Não |
| **Export CSV/HTML** | Local | Não |

### Estratégia Proposta

```
US sem dados sensíveis → API cloud (Groq, rápido e barato)
US com dados sensíveis → Ollama local (PC, lento mas seguro)
```

O roteamento pode ser manual (QA escolhe) ou automatizado (Guard-Rails detectam termos sensíveis e redirecionam).

---

## 6. Cenários de Stack — Com Custos em BRL

### Cenário A: "Cloud Puro" — Mais rápido e barato

| Componente | Provedor | <custo-mensal-redigido> |
|:---|:---|:---:|
| Primário | Groq + llama-3.1-8b | ~<custo-redigido> |
| Fallback pt-BR | Qwen Turbo (intl) | ~<custo-redigido> |
| Backup | Gemini 2.5 Flash-Lite | ~<custo-redigido> |
| **Total** | | **~<custo-redigido>** |

⚠️ Dados saem da empresa. Sem compliance LGPD para US sensíveis.

### Cenário B: "Cloud + On-Premises" — ⭐ RECOMENDADO

| Componente | Provedor | <custo-mensal-redigido> |
|:---|:---|:---:|
| Primário (US normais) | Groq + llama-3.1-8b | ~<custo-redigido> |
| Fallback pt-BR | Qwen Turbo (intl) | ~<custo-redigido> |
| Fallback premium | Gemini 2.5 Flash-Lite | ~<custo-redigido> |
| Sensível (LGPD) | Ollama em servidor on-premises dedicado | ~<custo-redigido> |
| **Total** | | **~<custo-redigido>** |

✅ Cobre compliance. Usa hardware existente. Múltiplos fallbacks.

### Cenário C: "Premium Cloud" — Qualidade máxima

| Componente | Provedor | <custo-mensal-redigido> |
|:---|:---|:---:|
| Primário | GPT-5.4 nano | ~<custo-redigido> |
| Qualidade | GPT-5.4 full | ~<custo-redigido> |
| Fallback | Claude Sonnet 4.6 | ~<custo-redigido> |
| **Total** | | **~<custo-redigido>** |

⚠️ Ainda mais barato que Copilot Pro, mas overkill para BDD estruturado.

### Cenário D: "100% On-Premises" — Privacidade total

| Componente | Provedor | <custo-mensal-redigido> |
|:---|:---|:---:|
| Único | Ollama em servidor on-premises dedicado | ~<custo-redigido> |
| **Total** | | **~<custo-redigido>** |

✅ Zero dados na nuvem. ⚠️ Latência alta (20-45s). ⚠️ Não atende <N QAs> simultâneos.

---

## 7. Comparativo Final: Economia Anual

| Stack | <custo-mensal-redigido> | <custo-anual-redigido> | vs Copilot Pro (<custo-redigido>) | Economia |
|:---|:---:|:---:|:---:|:---:|
| **A: Cloud puro** | ~<custo-redigido> | ~<custo-redigido> | -99,5% | **<custo-redigido>** |
| **B: Cloud + Ollama** ⭐ | ~<custo-redigido> | ~<custo-redigido> | -88,3% | **<custo-redigido>** |
| **C: Premium cloud** | ~<custo-redigido> | ~<custo-redigido> | -69,6% | **<custo-redigido>** |
| **D: 100% on-prem** | ~<custo-redigido> | ~<custo-redigido> | -89,1% | **<custo-redigido>** |
| **Copilot Pro (atual)** | **<custo-redigido>** | **<custo-redigido>** | referência | — |

---

## 8. Tabela de Decisão — Notas 0-10

| Critério (peso) | A: Cloud | B: Cloud+Ollama ⭐ | C: Premium | D: On-Prem |
|:---|:---:|:---:|:---:|:---:|
| Custo (25%) | 10 | 8 | 5 | 8 |
| Qualidade BDD (25%) | 8 | 8 | 10 | 7 |
| Latência/UX (20%) | 10 | 8 | 8 | 3 |
| Compliance/LGPD (15%) | 3 | 8 | 3 | 10 |
| Manutenção/Operação (15%) | 9 | 7 | 7 | 5 |
| **Nota Final** | **8.2** | **7.9** ⭐ | **6.8** | **6.3** |

> **Se compliance/LGPD for requisito obrigatório**, o Cenário B é o vencedor claro — combina o melhor de cloud (velocidade e custo) com on-premises (privacidade), usando um PC que já temos parado.

> **Se compliance NÃO for blocker**, o Cenário A é imbatível: <custo-redigido> para <N QAs>.

---

## 9. Escopo Completo — Ecossistema de Aceleradores QA

### 9.1 Gherkin Manager (Core)

| Capacidade | Descrição | Usa IA? |
|:---|:---|:---:|
| **Analisar US** | Avalia completude, ambiguidade e testabilidade de User Stories | ✅ |
| **Criar/Sugerir US** | Gera User Stories no formato "Como/Quero/Para" a partir de requisitos brutos | ✅ |
| **Gerar Cenários Gherkin** | Dado/Quando/Então com Feltrim's Framework | ✅ |
| **Gerar BDDs Completos** | Cenários completos com test data, expected results, hierarchy | ✅ |
| **Processados_BDD** | Exporta no nosso padrão interno, pronto para Zephyr Scale | Parcial |
| **Guard-Rails** | 48 padrões regex que bloqueiam termos técnicos proibidos | ❌ (Python puro) |
| **Export CSV Zephyr** | 29 colunas, 3 linhas por Test Case | ❌ (Python puro) |
| **Export Compacto** | 20 colunas, 1 linha por TC (visão gerencial) | ❌ (Python puro) |
| **HTML Viewer** | Visualização para revisão com stakeholders | ❌ (Python puro) |
| **Extensão Chrome** | Lê US do Jira/Azure com 1 clique, exibe resultado em Side Panel | ❌ (JS/HTML) |

### 9.2 Kanban QA (Planejado)

| Capacidade | Descrição | Usa IA? |
|:---|:---|:---:|
| **Board visual** | Colunas: Backlog → Análise → Teste → Review → Done | ❌ |
| **Distribuição de carga** | IA analisa velocidade e sugere redistribuição | ✅ |
| **Alertas de bloqueio** | Detecta tarefas paradas e notifica | ✅ |
| **Priorização por risco** | Cruza criticidade da US com histórico | ✅ |
| **Relatório semanal** | Resumo automático do time | ✅ |

### 9.3 Dashboard Executivo (Planejado)

| Capacidade | Descrição | Usa IA? |
|:---|:---|:---:|
| **Consolidação de métricas** | Puxa dados de planilhas e consolida | Parcial |
| **Status report automático** | Gera texto executivo por sprint | ✅ |
| **Visão por sprint** | Progresso, cobertura, velocidade | ❌ |
| **Atualização via planilha** | QAs atualizam planilha → dashboard atualiza | ❌ |
| **Export e-mail/PPT** | Relatório pronto para liderança | ✅ |

---

## 10. Plano de Transição

| Sprint | Semanas | Entrega | Dependência | Custo |
|:---:|:---:|:---|:---|:---:|
| **Sprint 1** | 1-2 | Fix encoding, testes unitários, CI (GitHub Actions) | Nenhuma | <custo-redigido> |
| **Sprint 2** | 3-4 | FastAPI + integração Groq/Qwen + Ollama no PC | APIs aprovadas | <custo-redigido> |
| **Sprint 3** | 5-6 | Extensão Chrome (Manifest V3) + Side Panel | Sprint 2 | <custo-redigido> |
| **Sprint 4** | 7-8 | Beta com <N QAs subset> + documentação completa de manutenção | Sprint 3 | <custo-redigido> |
| **Rollout** | 9-10 | Distribuição para os <N QAs> + cancelamento Copilot Pro | Beta OK | **-<custo-redigido>** |

> **Sprint 1 pode começar amanhã sem nenhum custo ou aprovação.** O cancelamento do Copilot Pro só ocorre após o rollout bem-sucedido (Sprint 5), eliminando risco de ficar sem ferramenta.

---

## 11. O que Solicitamos

| # | Solicitação | Impacto | Custo |
|:---:|:---|:---|:---:|
| 1 | Aprovar uso das APIs cloud (Groq/Qwen/Gemini) | Habilita IA no Gherkin Manager | **<custo-redigido>** |
| 2 | Autorizar uso de servidor on-premises dedicado para Ollama | Cobre compliance LGPD | **~<custo-redigido>** (energia) |
| 3 | Alocar 4 sprints de desenvolvimento (8 semanas) | Entrega a solução completa | tempo do autor |
| 4 | Avaliar cancelamento das <N licencas> Copilot Pro | Libera <custo-redigido> | **-<custo-redigido>** |
| 5 | Definir ownership conjunto (Rafael + <lider>) | Garante continuidade | Documentação |

**Saldo líquido:** De <custo-redigido> para ~<custo-redigido> = **economia de ~<custo-redigido> (~<custo-redigido>)**

---

## 12. Notas Técnicas e Transparência

- As chaves de API utilizadas nos benchmarks eram pessoais do Rafael, para fins de teste. A empresa precisará provisionar suas próprias chaves
- A chave Gemini pessoal estava com quota esgotada. Os benchmarks Gemini foram feitos com o modelo `gemini-2.5-flash-lite`
- A conta Qwen está na região **internacional** do Alibaba Cloud. O endpoint obrigatório é `dashscope-intl.aliyuncs.com` (não o da China)
- A GPU do servidor on-premises atual não suporta aceleração para IA (sem ROCm/CUDA). A IA rodará em CPU dedicada, resultando em latência de ~20-45s por resposta. Um upgrade futuro com SSD (~<custo-redigido>) e/ou GPU NVIDIA usada (~<custo-redigido>) melhoraria significativamente a performance

---

## Fontes Oficiais de Pricing

| Provedor | URL |
|:---|:---|
| Groq | [groq.com/pricing](https://groq.com/pricing) |
| Google Vertex AI | [cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Gemini API | [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| OpenAI | [openai.com/api/pricing](https://openai.com/api/pricing/) |
| Anthropic | [platform.claude.com/docs/models/overview](https://platform.claude.com/docs/en/about-claude/models/overview) |
| Alibaba Model Studio | [help.aliyun.com/model-studio/model-pricing](https://help.aliyun.com/zh/model-studio/model-pricing) |
| Câmbio CNY/USD | [bsp.gov.ph ref. 06/03/2026](https://www.bsp.gov.ph/Lists/RERB/Attachments/2228/06Mar2026.pdf) |

---

## Evidência: Benchmarks Reais

Todos os benchmarks foram executados no dia 24/03/2026 diretamente no repositório 98_Gherkin-Manager:

| Benchmark | Resultado |
|:---|:---|
| Groq vs Qwen (via Groq) | [report.md](file:///<us-avaliator-repo>/98_Gherkin-Manager/BENCHMARKS/groq_qwen_benchmark/report.md) |
| Gemini 2.5 Flash-Lite | [report.md](file:///<us-avaliator-repo>/98_Gherkin-Manager/BENCHMARKS/gemini_flash_lite_benchmark/report.md) |
| Qwen Turbo/Plus (direto Alibaba) | [report.md](file:///<us-avaliator-repo>/98_Gherkin-Manager/BENCHMARKS/qwen_direct_benchmark/report.md) |

---

**Fico à disposição para apresentar o relatório técnico completo e iniciar a Sprint 1 imediatamente.**

*Rafael Feltrim · Março 2026*  
*<lider> — Liderança · Co-Owner*

---

*Créditos: Rafael Feltrim. Todo o conteúdo deste documento, os benchmarks, o Gherkin Manager e o Feltrim's Framework foram estruturados e produzidos por Rafael Feltrim.*
