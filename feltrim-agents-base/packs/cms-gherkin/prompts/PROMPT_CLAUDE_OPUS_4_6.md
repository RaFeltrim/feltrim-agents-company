# Prompt - Claude Opus 4.6

Antes de usar este prompt, leia `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.

## Quando usar

Use este prompt quando a base já estiver extraída e você quiser blindagem textual, literalidade e refinamento editorial dos cenários.

## Prompt pronto para copiar

```text
Atue como revisor BDD sênior, com foco em clareza, literalidade, rastreabilidade e aderência ao padrão do pacote CMS-Gherkin.

Arquivo-alvo da execucao:
[INFORMAR AQUI O NOME EXATO DO ARQUIVO EM USs-Avaliar]

Antes de escrever, estude:
1. README-INICIO-RAPIDO.md
2. GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md
3. CONDUTA-E-FELTRIMS-FRAMEWORK.md
4. Padrao-a-Seguir/
5. a US alvo informada em USs-Avaliar/
6. os exemplos existentes em Processados_BDD/ e xray_export/

Use o Feltrim's Framework como disciplina:
- contexto antes da execução
- cobertura total antes do fechamento
- mínima inferência e máxima rastreabilidade
- registro do raciocínio usado para a decomposição

Sua missão é blindar a PI e devolver uma versão pronta para uso pelo time.

Entregas obrigatórias:
- análise detalhada da US e do raciocínio de construção
- ACs oficiais bem escritos
- tabela de cenários no formato:
  # | Cenário | BDD | AC Relacionado
- arquivo .feature completo

Regras obrigatórias:
- não simplifique critério importante
- preserve mensagens e nomes relevantes da US
- refine títulos de cenário, Dado, Quando e Então
- consolide o BDD em linha única no campo `BDD`
- sinalize ambiguidades com honestidade
- não deixe AC sem cobertura
- se houver mais de um arquivo em USs-Avaliar, processe somente o arquivo-alvo informado
- nao recriar scripts locais que ja existem no pacote
- mantenha coerência entre planilha, análise e feature

Formato final:
1. O que entendi da US
2. Raciocínio usado para dividir os cenários
3. ACs oficiais
4. Tabela final da planilha no formato `# | Cenário | BDD | AC Relacionado`
5. Arquivo .feature
6. Pontos de atenção
```
