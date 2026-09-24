# Changelog - Pack US Avaliator

## 1.0.1 - 2026-05-16 - Sanitizacao residual (Sofia 48h audit)

### Corrigido

Sanitizacao adicional apos audit Sofia CIAO detectar residuos. Mudancas
foram aplicadas na mesma data da release inicial para manter coerencia
com a declaracao publica de pack sanitizado:

- 3 ocorrencias de `30 QAs` / `~30 assinaturas` (Proposta linha 16,
  relatorio Sofia linha 10, relatorio Pedro linha 10) -> trocadas por
  `<N QAs>` / `<N licencas>` conforme `<estimativa-redigida>` ja
  documentada no CHANGELOG 1.0.0.
- 8 ocorrencias de placeholder parcial `<custo-redigido>-N/mês` ou
  `<custo-redigido>-N` -> padronizadas para `<custo-redigido>` puro
  (formato originalmente declarado).
- 4 ocorrencias de placeholder inconsistente `<beta-N QAs>` /
  `<concorrentes-N QAs>` -> padronizadas para `<N QAs subset>`.
- "Rafael Feltrim - QA Pleno" -> "Rafael Feltrim - QA Engineer" no
  cabecalho da Proposta e "Rafael Feltrim - QA Pleno - Studio de QA -
  Marco 2026" -> "Rafael Feltrim - Marco 2026" no rodape, removendo
  rank profissional especifico do empregador atual.
- 6 mencoes de "PC dedicado" / "PC ocioso" / "PC parado" -> trocadas
  por "servidor on-premises dedicado" / "infraestrutura local existente"
  para nao caracterizar setup informal.
- Mencao a hardware especifico do servidor ("RX 550 do PC", "CPU do
  i7 3770") -> generalizada para "GPU do servidor on-premises atual" /
  "CPU dedicada".

### Decisao mantida

- Autoria "Rafael Feltrim" em credits, "De:" da Proposta e rodapes
  permanece (preservacao de IP autoral conforme
  `governance/SECURITY_AND_PRIVACY.md`).
- Linhas 14 e 26-27 do README e linha 14 deste CHANGELOG **citam o
  valor original como evidencia de sanitizacao** ("antes -> depois") e
  permanecem como documentacao de auditoria. Nao sao residuos.

## 1.0.0 - 2026-05-16 - Pack consolidado no boilerplate

### Migrado

- **Proposta_Substituicao_Copilot.md** - origem
  `<gherkin-manager-source>/Proposta_Final_Substituicao_Copilot.md`.
  Sanitizada:
  - Todos os valores em moeda local (`R$ X/mes`, `R$ X/ano`, `R$/mes`,
    `R$/ano`) substituidos por `<custo-redigido>`,
    `<custo-mensal-redigido>`, `<custo-anual-redigido>`.
  - Nome `Joao` (lider de negocio) substituido por `<lider>`.
  - `30 QAs` / `~30 licencas` substituidos por `<N QAs>` / `<N licencas>`.
  - Estimativa concreta de chamadas mensais substituida por
    `<estimativa-redigida>`.
  - Paths absolutos `c:/Users/Rafael Feltrim/Documents/us-avaliator/`
    substituidos por `<us-avaliator-repo>`.
  - Mencoes de `Rafael Feltrim` em contexto de equipe substituidas por
    `<autor>`; mantidas em "De:", "Owner tecnico", footer e creditos
    como expressao de autoria.

- **14 relatorios de agentes** em `agent-reports/relatorio_*.md` - origem
  `<gherkin-manager-source>/Relatorios_Agentes/`. Sanitizacao leve:
  - "proposta executiva de Rafael Feltrim" -> "proposta executiva do
    autor".
  - Demais ocorrencias de `Rafael Feltrim` -> `<autor>`.
  - `Joao` -> `<lider>`.
  - Valores em moeda local -> `<custo-redigido>`.

### Decisao registrada (NAO migrado)

Os seguintes documentos do `Gherkin-Manager_Fase1_Pacote` NAO foram
migrados nesta versao porque mencionam pelo menos 3 nomes de clientes
listados como `flag words` em `governance/SECURITY_AND_PRIVACY.md`:

- `01_Documentos_Oficiais/04_Relatorio_Auditoria_360.md`
- `01_Documentos_Oficiais/05_Laudo_Final_Qualidade_V4.md`
- `01_Documentos_Oficiais/06_Ata_Governanca_Qualidade.md`
- `01_Documentos_Oficiais/07_Evidencia_Padronizacao_Massiva.md`

Recomendacao para revisao humana posterior (rastreada em
`<repo-root>/DECISIONS_PENDING.md`):

- **Opcao 1 (defensiva)**: nao migrar; manter apenas como referencia no
  repo de origem.
- **Opcao 2 (sanitizacao por substituicao)**: substituir cada nome de
  cliente por `<cliente-A>`, `<cliente-B>`, `<cliente-C>` mantendo
  rastreabilidade interna.
- **Opcao 3 (rebrand para casos genericos)**: reescrever exemplos como
  Cliente Automotivo / Cliente Bureau de Credito / Cliente Banco
  preservando o aprendizado sem expor IP.

Decisor: Rafael Feltrim.

### Riscos e mitigacoes

| Risco | Impacto | Mitigacao |
|-------|---------|-----------|
| Exposicao de proposta interna com numeros | Medio | Numeros substituidos por placeholders; relacoes preservadas |
| Quebra de contexto sem nomes de equipe | Baixo | Mantido `<lider>` consistente entre proposta e relatorios |
| Confusao sobre autoria | Baixo | Rafael Feltrim mantido em credito/autoria como expressao de IP |
| Vazamento futuro ao adicionar mais arquivos | Alto | `governance/SECURITY_AND_PRIVACY.md` flag words bloqueiam adicao acidental |
