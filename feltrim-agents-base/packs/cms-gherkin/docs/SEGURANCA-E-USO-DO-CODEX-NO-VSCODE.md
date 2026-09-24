# Segurança e Uso do Codex no VS Code

## 1. Posicionamento seguro e honesto

Este material foi preparado para uso com o `Codex` no `VS Code`, de forma responsável e sem promessas absolutas.

O que pode ser afirmado com segurança:

- o uso da extensão oficial do Codex em contexto local/IDE não equivale a publicar o repositório
- a documentação oficial da OpenAI diferencia permissões locais e permissões em nuvem para o Codex
- não há indicação, na documentação oficial, de que o uso normal da extensão oficial do Codex no VS Code exponha automaticamente o conteúdo do repositório de forma pública

O que não deve ser prometido:

- "risco zero" em qualquer contexto
- que todo plano de uso trata dados da mesma forma
- que qualquer configuração local é automaticamente segura sem revisão de permissões e políticas

## 2. O que a documentação oficial da OpenAI informa

### Uso local vs. uso em nuvem

Na documentação oficial sobre Codex, a OpenAI diferencia:

- `Codex Local permissions`
- `Codex Cloud permissions`

Isso importa porque o uso via CLI/IDE local é tratado como um modo próprio de operação, distinto de delegação em nuvem.

### Conteúdo usado para treinamento

A documentação oficial informa que, para produtos empresariais da OpenAI, como `Business`, `Enterprise` e `Edu`, o conteúdo do cliente não é usado para melhorar modelos por padrão.

Para uso individual, a documentação orienta revisar os controles de dados da conta.

## 3. Como este pacote trata essa informação

Neste pacote, a orientação correta é:

- usar a extensão oficial do Codex
- preferir uso local com permissões controladas
- revisar configurações de dados e retenção da conta utilizada
- evitar segredos, credenciais reais e dados pessoais desnecessários no workspace
- manter o pacote saneado antes de compartilhamento

## 4. Frase segura para usar em apresentação ou handoff

Você pode usar esta formulação:

```text
O uso da extensão oficial do Codex no VS Code, em contexto local e com permissões controladas, não implica exposição pública automática do repositório. Ainda assim, a segurança operacional depende do plano contratado, das configurações de dados e da conduta de uso adotada pelo time.
```

## 5. Conduta recomendada para o time

- usar somente a extensão oficial homologada internamente
- revisar as permissões concedidas ao Codex no workspace
- evitar subir segredos ou dados sensíveis para a área de trabalho
- preferir pacotes saneados para demonstração, treinamento e passagem de conhecimento
- revisar as políticas do plano contratado antes de uso recorrente com material corporativo

## 6. Referências oficiais consultadas

Consulta realizada em `2026-03-16`.

- OpenAI Help Center - What is Codex:
  `https://help.openai.com/en/articles/11145903-what-is-codex`
- OpenAI Help Center - Codex Enterprise Admin Guide:
  `https://help.openai.com/en/articles/11145780-codex-enterprise-admin-guide`
- OpenAI Help Center - How your data is used to improve model performance:
  `https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance`

## 7. Conclusão

Para este pacote, a mensagem correta é simples:

`Codex no VS Code pode ser usado com segurança operacional quando a extensão oficial é utilizada em contexto controlado, com permissões revisadas, pacote saneado e observância da política de dados do plano contratado.`
