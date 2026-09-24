# Feltrim Agents - Project Constitution

> Versao generica para uso com Spec Kit em projetos baseados em Feltrim
> Agents Framework.
>
> Esta constituicao **complementa** a `governance/COMPANY_CHARTER.md` -
> ela aplica os principios da empresa ao escopo de um projeto especifico.

## Identidade do projeto

- **Nome do projeto:** `<a-definir>`
- **Cliente / domain:** `<a-definir>`
- **Decisor humano do projeto:** `<a-definir>` (sempre ha um)
- **Sponsor / lider:** `<a-definir>`
- **Inicio:** `<YYYY-MM>`

## Principios (5 invariantes)

### 1. Source of truth respeitada

- Toda decisao funcional deve apontar para uma fonte autoritativa:
  Mainframe, oraculo do dominio, contrato com cliente, regra de
  negocio documentada.
- Quando houver divergencia entre fontes, prevalece a mais autoritativa
  (em geral o oraculo do dominio).
- Agentes NUNCA inventam regra; pedem clarificacao.

### 2. Evidencia obrigatoria para classificacao

- Toda classificacao (PASSED, FAILED, BUG, RISCO ACEITO, etc.) precisa
  de evidencia reproduzivel.
- "Funcionou no meu cara" NUNCA e evidencia.
- Print sem contexto NUNCA e evidencia.

### 3. Separacao chat vs artefato

- Decisao tomada em chat / call / ritual **so vira oficial** quando
  promovida para artefato auditavel (issue, ADR, PR, run, status).
- Promocao segue `core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`.

### 4. Decisor humano final

- Decisor humano e a unica entidade autorizada a aprovar Go/No-Go, abrir
  bug oficial, fechar incidente, aprovar release, dar PASSED final.
- Agentes recomendam, decisor decide.

### 5. Seguranca e IP nao-negociaveis

- Dados de cliente, IP de terceiros, segredos: **NUNCA** em Git.
- Ver `governance/SECURITY_AND_PRIVACY.md` para flag words e
  procedimentos de incidente.

## Stack default (ajustar por projeto)

- Linguagem principal: `<a-definir>`
- Framework: `<a-definir>`
- Banco: `<a-definir>`
- Hospedagem: `<a-definir>`
- CI/CD: `<a-definir>`
- Observabilidade: `<a-definir>`

## Agentes ativos no projeto

Marcar com [x] os agentes core que atuam neste projeto:

- [ ] Aline (Cloud)
- [ ] Ana TDAH (UX)
- [ ] Beatriz (Tech Lead)
- [ ] Camila (DevOps)
- [ ] Claudia (PM)
- [ ] Cleber (Mobile)
- [ ] Emerson (Supabase / Data Eng)
- [ ] Fabio (Frontend)
- [ ] Joao (Backend / RPA)
- [ ] Laura (UI/UX)
- [ ] Mariana (Prompt Eng)
- [ ] Marlon (PO)
- [ ] Pedro (DBA / Analytics)
- [ ] Rafael (QA / SDET)
- [ ] Sofia (CIAO / Executive Audit)

Pack ativo (se houver): `packs/<nome-do-pack>/`

## Rituals ativos

Marcar com [x] os rituais que rodam neste projeto:

- [ ] pre-daily
- [ ] daily
- [ ] team-call
- [ ] retro
- [ ] hackathon
- [ ] capability-review
- [ ] adr-craft

(Ver `core/memory/team-rituals/` para definicao de cada um.)

## Validacao

Esta constituicao deve ser:

- Lida no boot de qualquer agente atuando no projeto.
- Revisada antes de mudanca arquitetural relevante.
- Atualizada quando principios funcionais mudam (raro - principios sao
  estaveis).

## Veja tambem

- `governance/COMPANY_CHARTER.md`
- `governance/SECURITY_AND_PRIVACY.md`
- `core/docs/SQUAD_INDEX.md`
- `core/docs/CHAT_TO_ARTIFACT_GOVERNANCE.md`
- `core/memory/team-rituals/`
