# Ritual: team-call (FULL)

> Ritual de equipe **completa** (modo FULL) com toda squad relevante
> presente. Usado em decisao critica, Go/No-Go, pos-incidente, mudanca
> arquitetural, auditoria de seguranca. Custa caro - so convocar quando
> justificado.

## Quando usar

- Go/No-Go de deploy critico (pagamento, autenticacao, dados sensiveis).
- Pos-incidente classificado como S1 ou S2.
- Mudanca arquitetural irreversivel ou de alto custo.
- Auditoria de seguranca / compliance.
- Decisao com impacto cross-team em 3+ areas.
- Promocao de nivel N4 -> N5 de agente (com decisor humano).

## Quando NAO usar

- Feature pequena ou media -> use `feature-init.md` (modo PAR ou MINI).
- Bug fix local -> modo SOLO direto.
- Mudanca de copy / typo / formatacao -> SOLO de Laura UI ou Ana TDAH.
- Sync rotineiro -> `pre-daily.md` (modo SOLO de varios).
- Brainstorm aberto sem decisao -> `flash-talks.md` (modo MINI).

## Custo aproximado

- 5+ chamadas de LLM, modelo premium para Sofia (ex.: Claude Opus / GPT-5 / equivalente).
- ~10x o custo de SOLO. ~5x o custo de PAR.
- Tempo equivalente do ritual: 60-120 min (mesmo que a "reuniao" seja
  sintetica entre agentes).
- Anexar custo estimado na ata para audit posterior.

## Participantes obrigatorios

| Papel | Quem (core) | Funcao |
|-------|-------------|--------|
| **Lider** | Sofia CIAO | Conduz, emite veredito final (Go / Go com ressalva / No-Go) |
| **Arquiteto** | Beatriz TL | Avalia trade-off arquitetural, divida tecnica |
| **Owner da feature/incidente** | gem da area (Joao Backend / Fabio Frontend / etc.) | Apresenta contexto tecnico |
| **QA** | Rafael QA | Cobertura de teste, evidencia, riscos de regressao |
| **DevOps** | Camila DevOps | Plano de rollback, observability, blast radius |
| **Decisor humano** | (humano real) | Aprovacao formal apos veredito Sofia |

## Participantes condicionais

Convocar adicionalmente se:

| Condicao | Gem extra |
|----------|-----------|
| Mudanca em UI/UX afeta usuario final | Laura UI |
| Fluxo critico para usuario com carga cognitiva alta | Ana TDAH |
| Mudanca em prompt / agente / LLM contract | Mariana Prompt |
| Mudanca em DB / migration / RLS | Emerson Supabase ou Pedro DBA |
| Mudanca em topologia cloud / custo | Aline Cloud |
| Impacto em prazo / dependencia cross-team | Claudia PM |
| Impacto em prioridade de produto | Marlon PO |

## Roteiro do ritual

### 1. Pre-call (assincrono, antes)

- **Owner** prepara dossie:
  - Contexto (1 paragrafo)
  - Mudanca proposta (link para PR / ADR / runbook)
  - Riscos conhecidos (tabela)
  - Plano de rollback (steps + tempo)
  - Cobertura de teste atual (%)
  - Janela de execucao proposta
- **Sofia CIAO** confirma quorum minimo.
- **Claudia PM** envia convocacao formal com agenda em
  `team-call-notes-template.md`.

### 2. Setup (3 min) - Sofia abre

```text
team-call FULL convocada para: <tema>
Justificativa: <Go-Live | Pos-incidente | Mudanca arquitetural | Auditoria>
Participantes: <lista>
Decisor humano: <nome>
Custo estimado: <X chamadas, modelo Y>
Dossie pre-call: <link>
```

### 3. Apresentacao do owner (5 min)

Owner faz pitch tecnico curto sem demo:

- O que muda
- Por que essa abordagem
- Trade-offs conhecidos
- Plano de rollback

### 4. Rodada de analise (15-30 min, sequencial)

Cada gem fala em ordem fixa, com tempo limitado, focando na SUA area:

1. **Rafael QA** (5 min):
   - Cobertura de teste especifica para a mudanca
   - Buracos identificados
   - Riscos de regressao
   - Recomendacao de teste adicional pre-deploy

2. **Owner tecnico** (5 min, ja apresentou contexto, agora responde):
   - Endpoints / contratos afetados
   - Compatibilidade backward
   - Dependencias externas

3. **Camila DevOps** (5 min):
   - Plano de rollback (validado em ambiente equivalente?)
   - Observability (dashboards, alertas)
   - Blast radius se rollback falhar
   - Feature flag disponivel?

4. **Beatriz TL** (5 min):
   - Avaliacao arquitetural
   - Divida tecnica criada / paga
   - Alinhamento com ADRs existentes
   - Necessidade de nova ADR

5. **Gems condicionais** (5 min cada se convocadas).

### 5. Veredito Sofia CIAO (5 min)

Sofia emite:

```text
Veredito: GO | GO COM RESSALVA | NO-GO

Riscos aceitos:
- <risco> | mitigacao planejada

Riscos NAO aceitos (block):
- <risco> | acao requerida antes de prosseguir

Acoes pre-deploy:
- [ ] <acao> | dono | prazo

Acoes pos-deploy:
- [ ] <acao> | dono | prazo

Owner do incidente se materializar:
- <nome>

Janela autorizada: <data + hora>
```

### 6. Aprovacao do decisor humano (assincrono ou imediato)

Decisor humano REGISTRA EXPLICITAMENTE no canal oficial:

```text
APROVO o veredito da team-call de <data>.
Veredito: <Go / Go com ressalva / No-Go>
Concordo com riscos aceitos: <sim/nao>
Concordo com acoes obrigatorias: <sim/nao>
Owner final do deploy: <nome>
```

Sem essa linha do decisor humano, **nao prosseguir**.

### 7. Pos-call

- **Claudia PM** publica ata final em
  `core/memory/team-rituals/notes/team-call-YYYY-MM-DD-<tema>.md`
  (criar pasta `notes/` se nao existir, ela e gitignored por padrao).
- **Sofia CIAO** atualiza `core/memory/MEMORY.md` se houver decisao
  arquitetural duradoura.
- **Beatriz TL** abre ADR se aplicavel.
- **Marlon PO** atualiza backlog com acoes geradas.

## Anti-patterns desta ritual

- Convocar team-call por costume ("toda quarta") sem decisao concreta em
  jogo. Custa caro e vira ritual vazio.
- Pular o veredito Sofia para "ir mais rapido". Sem veredito, nao houve
  team-call - houve grupo de conversa.
- Pular o registro do decisor humano. Sem ele, nao houve aprovacao.
- Convocar agentes que nao tem opiniao na area da mudanca. Eh ruido.
- Usar team-call como sync semanal -> use `pre-daily.md` ou
  `flash-talks.md`.
- Nao registrar custo (chamadas + modelo) na ata. Sem registro nao da pra
  calibrar uso futuro.

## Modelo de ata

Use `team-call-notes-template.md` desta mesma pasta.

## Veja tambem

- `core/docs/AGENT_ACTIVATION_POLICY.md` - quando usar FULL vs outros modos
- `core/docs/TOKEN_ECONOMY.md` - calculo de custo
- `feature-init.md` - alternativa lean (PAR/MINI) para 80% das features
- `retro.md` (TODO) - retro pos-incidente
- `core/protocols/HANDOFF_PROTOCOL.md` - handoff entre gems durante a call
- `team-call-notes-template.md` - template de ata
