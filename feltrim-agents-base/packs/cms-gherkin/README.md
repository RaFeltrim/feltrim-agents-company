# Pack: CMS Gherkin

> Pack para projetos de CMS/Treinamento envolvendo BDD/Gherkin. Cobre o
> fluxo: leitura de User Story (US) -> analise -> conversao em features
> Gherkin -> registro de problemas e padroes aprovados -> export Xray.

## Origem

Migrado do pacote `<treinamento-cms-gherkin-source>/PACOTE-TREINAMENTO-CMS-GHERKIN/CMS-Gherkin`,
versao de 2026-03-20. Mantido praticamente 1:1, apenas reorganizado em
subdiretorios consistentes com o boilerplate Feltrim Agents Base.

## Estrutura

```
packs/cms-gherkin/
|-- README.md                       (este arquivo)
|-- prompts/                        (4 prompts canonicos por modelo LLM)
|   |-- PROMPT_CLAUDE_OPUS_4_6.md
|   |-- PROMPT_GEMINI_3_1_PRO.md
|   |-- PROMPT_GPT_5_4.md
|   `-- PROMPT_GPT_5_4_ECONOMICO.md
|-- ferramentas/                    (scripts Python operacionais)
|   |-- gerar_artefatos.py          (gera artefatos BDD a partir das USs)
|   `-- registrar_problema.py       (atualiza MEMORIA-OPERACIONAL)
|-- fontes-estruturadas/            (modelos JSON de fonte estruturada)
|   |-- MODELO-FONTE-ESTRUTURADA.json
|   `-- PROJETO-EXEMPLO.json
|-- memoria-operacional/            (problemas e solucoes acumulados)
|   `-- PROBLEMAS-E-SOLUCOES.md
|-- padrao-a-seguir/                (exemplo de padrao aprovado)
|   `-- EXEMPLO-PADRAO-APROVADO.md
|-- docs/                           (guias operacionais)
|   |-- CONDUTA-E-FELTRIMS-FRAMEWORK.md
|   |-- GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md
|   |-- GUIA-DE-USO-OPERACIONAL-NOVA-PASTA-DE-PROJETO.md
|   |-- MODO-ECONOMICO-DE-TOKENS.md
|   |-- README-INICIO-RAPIDO.md
|   `-- SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md
`-- exemplos/                       (artefatos PROJETO-EXEMPLO genericos)
    |-- analises/                   (analise detalhada de US exemplo)
    |-- processados-bdd/            (features geradas exemplo)
    |-- uss-avaliar/                (US exemplo .docx + .xlsx)
    `-- xray-export/                (export Xray exemplo)
```

## Filosofia do pack

Conforme `docs/CONDUTA-E-FELTRIMS-FRAMEWORK.md`, o pack opera dentro do
framework Feltrim:

- Operacao deve favorecer ciclo curto e auditavel.
- Cada conversao US -> Gherkin deve produzir evidencia salva em
  `memoria-operacional` quando aparecer problema novo ou solucao nova.
- `padrao-a-seguir/EXEMPLO-PADRAO-APROVADO.md` define o padrao aprovado
  vigente: novas features devem buscar paridade com o exemplo.

## Modos de operacao

| Modelo LLM | Prompt | Uso recomendado |
|------------|--------|-----------------|
| Claude Opus 4.6 | `prompts/PROMPT_CLAUDE_OPUS_4_6.md` | US complexa, fluxo com varias entradas |
| Gemini 3.1 Pro | `prompts/PROMPT_GEMINI_3_1_PRO.md` | US com tabela/anexo (.docx, .xlsx) |
| GPT-5.4 padrao | `prompts/PROMPT_GPT_5_4.md` | US generica |
| GPT-5.4 economico | `prompts/PROMPT_GPT_5_4_ECONOMICO.md` | Lote / batch / cenarios simples |

> **Nota sobre nomes de modelo:** os identificadores `GPT-5.4`,
> `Claude Opus 4.6` e `Gemini 3.1 Pro` representam a notacao interna
> usada quando este pack foi criado para distinguir geracoes / linhas
> de modelo (ex.: `Codex no VS Code` linha 4.x). Substitua pelos nomes
> reais disponiveis na sua conta no momento da execucao (ex.: `Codex`,
> `Claude Sonnet 4.5`, `Gemini 2.5 Pro`). O comportamento esperado dos
> prompts independe da versao especifica e deve funcionar com qualquer
> geracao equivalente.

Detalhes de economia de token em `docs/MODO-ECONOMICO-DE-TOKENS.md`.

## Ferramentas

- `ferramentas/gerar_artefatos.py` - Le US -> aplica template -> gera
  feature Gherkin + caderno de analises.
- `ferramentas/registrar_problema.py` - Anexa novo problema/solucao em
  `memoria-operacional/PROBLEMAS-E-SOLUCOES.md`.

> Estes scripts assumem a estrutura espelhada deste pack copiada para um
> repositorio de projeto. Adaptar paths antes de rodar.

## Onboarding rapido

1. Ler `docs/README-INICIO-RAPIDO.md`.
2. Ler `docs/CONDUTA-E-FELTRIMS-FRAMEWORK.md` para entender filosofia.
3. Escolher prompt em `prompts/` conforme modelo disponivel.
4. Carregar `padrao-a-seguir/EXEMPLO-PADRAO-APROVADO.md` como exemplo de
   nivel de qualidade esperado.
5. Rodar `ferramentas/gerar_artefatos.py` apos pre-processar fontes
   estruturadas conforme `fontes-estruturadas/MODELO-FONTE-ESTRUTURADA.json`.

## Decisor humano

O fluxo CMS Gherkin atualmente nao tem decisor humano oficial definido
neste boilerplate (depende do projeto cliente). Quando ativado em um
projeto, o decisor humano do projeto e dono final dos artefatos gerados.

## Veja tambem

- `core/agents/gem_rafael_qa.md` - QA/SDET core que pode operar este pack.
- `core/agents/gem_marlon_po.md` - PO core para validar critericos de
  aceite das US.
- `core/docs/ONBOARDING.md` - onboarding generico do framework.
- `governance/SECURITY_AND_PRIVACY.md` - pack contem dados de PROJETO-EXEMPLO;
  ao instanciar para cliente real, manter dados do cliente fora deste pack
  e dentro do repositorio do projeto cliente.
