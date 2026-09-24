# Certification Policy - Feltrim Agents Company

> Politica oficial sobre emissao, manutencao e revogacao de certificacoes
> internas dos agentes. Catalogo completo em
> `core/docs/AGENT_CERTIFICATIONS.md`.

## Principio

```text
Certificacao = competencia reconhecida + evidencia auditavel
             + emissor autorizado.

Sem evidencia, sem certificacao.
Sem emissor autorizado, sem certificacao.
```

## Quem emite

| Categoria | Emissor primario | Co-emissor | Validacao |
|-----------|-----------------|------------|-----------|
| Foundation (FA-FOUND) | Sofia CIAO | Decisor humano | Quiz + 1 execucao real com protocolos aplicados |
| Tecnica (BDD-AUDIT, PLAYWRIGHT-AUDIT, ADR-CRAFT, PROMPT-OPT) | Sofia CIAO + gem especialista par (ex.: Rafael-QA para BDD) | Decisor humano | Artefatos auditaveis especificados no catalogo |
| Governanca (CIAO-GO-LIVE-READY, CHAT-PROMOTION) | Decisor humano | Sofia CIAO endorsa | Historico de vereditos / promocoes |
| Pack-specific (`<PACK>-FOUND`, `<PACK>-AUDIT`, EVIDENCE-PDF, BUG-RETEST, CMS-BDD-V3, etc.) | CIAO do pack ou Orchestrator | Sofia CIAO + decisor humano | Artefatos do pack |

### Restricao critica

A certificacao CIAO-GO-LIVE-READY e a UNICA que a Sofia CIAO nao emite
para si mesma. Sofia ja tem essa cert por design (e o papel dela). Para
qualquer outro agente conquistar, decisor humano e o aprovador principal.

## Quem solicita

- A propria gem pode solicitar em capability review.
- Sofia CIAO pode propor durante revisao trimestral.
- Orchestrator de pack pode propor para gens do pack.

## Processo de emissao

1. **Candidatura**: a gem (ou quem propos) preenche secao "Certificacoes
   candidatas" em capability review.
2. **Evidencia**: anexar links auditaveis para cada criterio do catalogo.
3. **Revisao tecnica**: emissor primario valida evidencia.
4. **Endorso**: co-emissor confirma.
5. **Aprovacao final**: decisor humano (Rafael) assina capability review.
6. **Registro**: atualizar `agent-profile.md` da gem com `[x] <CODIGO> -
   <AAAA-MM-DD> - assinado por <emissor>`.
7. **SQUAD_INDEX**: atualizar coluna "Certs default" se for cert default da
   gem.

## Validade

Default: **permanente** ate haver:

- Mudanca de versao do framework FF (re-certificacao opcional).
- Mudanca no catalogo da certificacao especifica (revisao obrigatoria).
- Capability review extraordinaria com regressao na area da cert.
- Revogacao formal por uso incorreto.

## Revogacao

Uma cert pode ser revogada se:

- A gem usou a cert para autorizar acao sem evidencia.
- O artefato que serviu de evidencia foi invalidado (ADR rejeitado, ADR
  superseded por motivo de erro, bug em producao causado pelo padrao
  certificado).
- Capability review revela regressao grave na area da cert.

Processo de revogacao:

1. Sofia CIAO abre capability review extraordinaria.
2. Documenta motivo com link auditavel.
3. Marca a cert no `agent-profile.md` como
   `[ ] <CODIGO> - revogada em <data> por <motivo>`.
4. Atualiza `SQUAD_INDEX.md` removendo da coluna "Certs default".
5. Notifica decisor humano.

Revogacao **nao** impede o agente de continuar trabalhando. So volta a
exigir autorizacao para acoes que dependiam daquela cert.

## Catalogo vivo

Para adicionar uma cert nova ao catalogo:

1. PR com:
   - Bloco completo (codigo, categoria, nivel, pre-reqs, validade, o que
     prova, evidencia, elegiveis, emissor, guardrails).
   - Adicionar em `core/docs/AGENT_CERTIFICATIONS.md`.
2. Aprovacao Sofia CIAO + decisor humano.
3. Atualizar este arquivo se a politica de emissao precisar de regra
   especifica.

Para depreciar uma cert existente:

1. PR com:
   - Justificativa.
   - Plano de migracao para certs equivalentes (se houver).
   - Comunicacao para gens que tinham a cert.
2. Aprovacao Sofia CIAO + decisor humano.
3. Atualizar `core/docs/AGENT_CERTIFICATIONS.md` marcando como
   `DEPRECATED em <data>`.

## Conflito de interesse

- Sofia CIAO emite todas as certs (exceto CIAO-GO-LIVE-READY para si mesma
  - que ela ja tem por design).
- Decisor humano e sempre o ultimo a assinar.
- Gem nao pode emitir cert para si mesma.
- Gem que e emissora de cert nao pode emitir para outra gem se for parte
  interessada na decisao especifica (ex.: Mariana nao emite PROMPT-OPT
  para si mesma; pede endorso da Sofia).

## Auditoria

Sofia CIAO faz revisao trimestral de:

- Quantas certs foram emitidas no trimestre.
- Quantas foram revogadas (sintoma de criterio fraco se for alto).
- Se alguma cert virou "decorativa" (a gem nunca usa o unlock relacionado).
- Se algum agente tem cert sem evidencia atualizada nos ultimos 6 meses
  (re-certificar ou revogar).

## Veja tambem

- `core/docs/AGENT_CERTIFICATIONS.md` - catalogo completo
- `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md` - matriz N1-N5
- `core/memory/agents/_templates/agent-capability-review-template.md`
- `governance/PROMOTION_POLICY.md`
