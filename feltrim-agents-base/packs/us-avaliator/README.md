# Pack: US Avaliator

> Pack experimental que consolida o trabalho de avaliacao da proposta
> executiva "Substituicao de Copilot Pro por stack de IA dedicado" e os
> 14 relatorios consolidados produzidos por agentes do Feltrim Agents
> Framework como exercicio de revisao multi-perspectiva.

## Origem

Pacote derivado de `<gherkin-manager-source>/Gherkin-Manager_Fase1_Pacote/`
(versao Marco/2026), especificamente:

- `Proposta_Final_Substituicao_Copilot.md` (proposta executiva original).
- `Relatorios_Agentes/relatorio_*.md` (14 revisoes feitas pelos agentes
  Feltrim, organizadas por papel).

## Sanitizacao aplicada

Para tornar o material seguro para repositorio publico/portfolio, foi
aplicada a seguinte redaction:

| Item original | Substituicao |
|---------------|--------------|
| Valores em moeda local (R$ X/mes, R$ X/ano) | `<custo-redigido>`, `<custo-mensal-redigido>` |
| `Joao` (lider de negocio) | `<lider>` |
| `30 QAs`, `~30 licencas` | `<N QAs>`, `<N licencas>` |
| Estimativa `15 US/QA/dia x 30 QAs x 30 dias = 13.500/mes` | `<estimativa-redigida>` |
| Paths absolutos `c:/Users/Rafael Feltrim/Documents/us-avaliator` | `<us-avaliator-repo>` |
| Consumo eletrico em kWh | `<consumo-redigido>` |
| `Rafael Feltrim` em contexto de equipe ("revisao de proposta de Rafael Feltrim") | `<autor>` |
| `Rafael Feltrim` em credito/autoria (header, footer, "Owner tecnico") | mantido como autoral |

## Estrutura

```
packs/us-avaliator/
|-- README.md                                     (este arquivo)
|-- docs/
|   |-- Proposta_Substituicao_Copilot.md          (proposta sanitizada)
|   `-- CHANGELOG.md                              (historico do pack)
`-- agent-reports/                                (14 revisoes sanitizadas)
    |-- relatorio_aline_arch.md
    |-- relatorio_beatriz_tl.md
    |-- relatorio_camila_devops.md
    |-- relatorio_claudia_pm.md
    |-- relatorio_cleber_mobile.md
    |-- relatorio_emerson_de.md
    |-- relatorio_fabio_frontend.md
    |-- relatorio_joao_backend.md
    |-- relatorio_laura_uiux.md
    |-- relatorio_mariana_prompt.md
    |-- relatorio_marlon_po.md
    |-- relatorio_pedro_dados.md
    |-- relatorio_rafael_qa.md
    `-- relatorio_sofia_ciao.md
```

## O que NAO foi migrado (e por que)

| Arquivo de origem | Motivo da exclusao |
|-------------------|---------------------|
| `01_Documentos_Oficiais/05_Laudo_Final_Qualidade_V4.md` | Contem nomes de 3 clientes (flag words `governance/SECURITY_AND_PRIVACY.md`). Decidir profundidade de sanitizacao requer envolver decisor humano. |
| `01_Documentos_Oficiais/06_Ata_Governanca_Qualidade.md` | Mesmo motivo - referencia a clientes especificos. |
| `01_Documentos_Oficiais/04_Relatorio_Auditoria_360.md` | Mesmo motivo. |
| `01_Documentos_Oficiais/07_Evidencia_Padronizacao_Massiva.md` | Mesmo motivo. |
| `blueprint_v3_documentacao/*` | Ja migrado para `core/protocols/` em PR1; nao duplicar aqui. |
| `Passagem-Us-avaliator.mp4` | Binario; conteudo nao indexavel e potencial vazamento de tela. |

Ver `docs/CHANGELOG.md` para o registro completo da decisao.

Tracking adicional em `<repo-root>/DECISIONS_PENDING.md` -> item "us-avaliator
pack - profundidade de sanitizacao".

## Como usar este pack

Este pack tem valor primariamente didatico e demonstrativo:

1. Mostrar como **uma unica proposta** pode ser auditada por **multiplos
   agentes** especializados em paralelo (Aline arch, Beatriz TL, Camila
   devops, etc).
2. Servir de **caso de uso** para o ritual `team-call` (ver
   `core/memory/team-rituals/team-call.md`).
3. Demonstrar a tecnica de **revisao multi-perspectiva** mencionada em
   `core/docs/manifesto/FELTRIMS_FRAMEWORK_MANIFESTO.md`.

## Decisor humano

Rafael Feltrim. Autoria da proposta original e da convocacao dos agentes
para revisao. Toda decisao sobre execucao ou nao da proposta original
e da empresa/lider para quem ela foi enderecada.

## Veja tambem

- `core/agents/` - 15 agentes que produziram as revisoes.
- `core/memory/team-rituals/team-call.md` - ritual de revisao multi-perspectiva.
- `governance/SECURITY_AND_PRIVACY.md` - politica que motivou a sanitizacao.
- `DECISIONS_PENDING.md` - item us-avaliator profundidade de sanitizacao.
