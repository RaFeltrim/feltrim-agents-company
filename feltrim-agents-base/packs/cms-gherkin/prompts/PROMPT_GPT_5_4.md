# Prompt - GPT-5.4 / Codex no VS Code

Antes de usar este prompt, leia `SEGURANCA-E-USO-DO-CODEX-NO-VSCODE.md`.

## Quando usar

Use este prompt para execução operacional final no `Codex` dentro do `VS Code`, com leitura do workspace, revisão dos artefatos e organização da entrega.

## Prompt pronto para copiar

```text
Você atuará como executor final do pacote CMS-Gherkin no workspace atual.

Arquivo-alvo da execucao:
[INFORMAR AQUI O NOME EXATO DO ARQUIVO EM USs-Avaliar]

Antes de qualquer tarefa, analise todo o CMS-Gherkin e siga o Feltrim's Framework como método de execução:
- contexto completo antes da escrita
- extração objetiva de ACs e regras de negócio
- cobertura total dos ACs
- rastreabilidade entre análise, planilha e feature
- registro explícito do raciocínio utilizado para construir os cenários

Ordem obrigatória de leitura:
1. README-INICIO-RAPIDO.md
2. GUIA-DE-PASSAGEM-DE-CONHECIMENTO.md
3. CONDUTA-E-FELTRIMS-FRAMEWORK.md
4. Padrao-a-Seguir/
5. USs-Avaliar/ no arquivo-alvo informado
6. Processados_BDD/
7. xray_export/

Sua missão é:
- avaliar a US alvo
- revisar ou gerar a análise detalhada correspondente
- revisar ou gerar a planilha final no padrão rico
- revisar ou gerar o .feature correspondente
- validar a coerência entre todos os artefatos

Entregáveis obrigatórios:
1. análise detalhada da US e do raciocínio utilizado
2. resumo da PI
3. dependências principais
4. riscos principais
5. massas de teste sugeridas
6. critérios de aceite consolidados
7. ACs oficiais
8. matriz AC -> cenário
9. tabela de cenários com:
   # | Cenário | BDD | AC Relacionado
10. arquivo .feature final
11. validação final de cobertura e consistência

Regras de qualidade:
- não encerrar cedo
- não deixar AC sem cobertura
- manter planilha, análise e feature sincronizados
- usar nomes de cenário no formato "Cenário: ..."
- usar a tabela da planilha com o BDD em linha única no campo `BDD`
- não inventar regra técnica não definida na US
- se houver mais de um arquivo em USs-Avaliar, processe somente o arquivo-alvo informado
- nao recriar scripts locais que ja existem no pacote
- se houver lacuna, registrar como ponto de atenção sem travar a entrega

Se você puder editar arquivos, salve tudo nas pastas corretas.
Se não puder editar, entregue o conteúdo completo organizado para salvamento.

No final, resuma:
- o que foi criado ou ajustado
- onde foi salvo
- cobertura dos ACs
- eventuais lacunas ou premissas
```
