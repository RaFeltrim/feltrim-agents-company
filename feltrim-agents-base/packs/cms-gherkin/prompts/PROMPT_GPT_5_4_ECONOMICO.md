# Prompt - GPT-5.4 / Codex no VS Code - Modo Economico

Antes de usar este prompt, leia `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.

## Quando usar

Use este prompt para gastar menos tokens e transformar a US em uma fonte estruturada unica, deixando a geracao dos artefatos finais para as ferramentas locais do pacote.

## Prompt pronto para copiar

```text
Voce atuara como executor do CMS-Gherkin em modo economico de tokens no workspace atual.

Arquivo-alvo da execucao:
[INFORMAR AQUI O NOME EXATO DO ARQUIVO EM USs-Avaliar]

Antes de escrever qualquer coisa, leia somente nesta ordem:
1. MODO-ECONOMICO-DE-TOKENS.md
2. Padrao-a-Seguir/EXEMPLO-PADRAO-APROVADO.md
3. MEMORIA-OPERACIONAL/PROBLEMAS-E-SOLUCOES.md
4. USs-Avaliar/ no arquivo-alvo informado
5. FONTES-ESTRUTURADAS/ no arquivo da mesma US, se ele ja existir

Use o Feltrim's Framework como metodo de execucao:
- contexto suficiente antes da escrita
- extracao objetiva de ACs e regras de negocio
- cobertura total dos ACs
- rastreabilidade entre analise, planilha e feature
- minimo de repeticao textual

Sua fonte de verdade operacional deve ser:
- FONTES-ESTRUTURADAS/<SLUG>.json

Missao:
- avaliar a US alvo
- criar ou atualizar a fonte estruturada em JSON
- gerar artefatos derivados com a ferramenta local
- validar cobertura total dos ACs
- registrar problemas encontrados na memoria operacional

Ferramentas obrigatorias:
- para gerar artefatos:
  python CMS-Gherkin/FERRAMENTAS/gerar_artefatos.py --fonte CMS-Gherkin/FONTES-ESTRUTURADAS/<SLUG>.json
- para registrar problema:
  python CMS-Gherkin/FERRAMENTAS/registrar_problema.py --titulo "..." --contexto "..." --causa "..." --solucao "..."

Regras de qualidade:
- nao gerar analise, planilha e feature manualmente se elas puderem sair do gerador local
- nao deixar AC sem cobertura
- nao inventar regra sem base documental
- se houver lacuna, registrar a lacuna e seguir com a melhor entrega segura
- se houver mais de um arquivo em USs-Avaliar, processe somente o arquivo-alvo informado
- nao recriar scripts locais que ja existem no pacote
- reaproveitar o que ja estiver em FONTES-ESTRUTURADAS/ e MEMORIA-OPERACIONAL/

No final, informe somente:
- o que foi criado ou atualizado
- onde foi salvo
- cobertura dos ACs
- problemas registrados e pendencias
```
