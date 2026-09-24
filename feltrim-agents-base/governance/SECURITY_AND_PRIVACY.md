# Security and Privacy - Feltrim Agents Company

> Politica oficial sobre seguranca de dados, segredos, IP de cliente e
> privacidade nos repositorios e packs.

## Principio

```text
Nada que pertenca a cliente ou conte como segredo vai para Git.
Nada que pertenca a outro autor entra como autoral.
Toda exposicao acidental e tratada como incidente critico.
```

## Lista de palavras-bandeira (NUNCA em `core/` nem `governance/`)

Cada empresa/instalacao do Feltrim Agents Framework DEVE manter sua propria
lista de palavras-bandeira em arquivo privado (NAO commitar nesta lista
publica). Este arquivo so traz os **padroes** que aplicam ao boilerplate
publico.

### Categorias que devem virar palavras-bandeira na sua instalacao

Liste em arquivo privado os termos especificos da sua operacao para cada
categoria abaixo. Mantenha o arquivo fora de `core/`, `governance/`,
`examples/` e da raiz do repo.

**Clientes da empresa / projetos cliente:**

- Nomes proprios de cliente (ex.: `<CLIENTE-A>`, `<CLIENTE-B>`).
- Codinome/sigla de sistema cliente (ex.: `<SISTEMA-CLIENTE>`).
- Nomes de pessoas internas ao cliente.
- Codigos internos de processo/regra do cliente.

**Operacao interna da empresa (vai em `packs/<empresa>-internal/`):**

- Nomes proprios de marketplaces / fornecedores usados.
- Prefixos SKU especificos de catalogo.
- Regras operacionais internas (codinomes de rotinas, status, fluxos).
- Identificadores de canais, contas, instancias internas.

**Tecnologias cliente / proprietary:**

- Nomes de sistemas legados internos ao cliente.
- Nomes de aplicacoes internas ainda nao publicas do cliente.
- Componentes/extensoes customizadas que sao IP do cliente ou da empresa.

**Dados pessoais / segredos (universal):**

- Qualquer CPF / CNPJ real.
- Numeros de telefone reais.
- E-mails de cliente / fornecedor / colaborador.
- API keys, tokens, passwords.
- URLs com credenciais (`https://user:pass@host`).

## Verificacao automatica (pre-commit sugerido)

Comando recomendado antes de cada commit em `core/` ou `governance/`,
usando a lista da SUA instalacao (substituir `<flag1|flag2|...>`):

```bash
rg -i "(<flag1|flag2|flag3|...|sua lista privada>)" core/ governance/ examples/ README.md
```

Resultado esperado: **zero matches** (exceto se for o proprio header de
sanitizacao explicando que foi removido).

Para `packs/<cliente>/` o resultado pode ter matches - e o pack dele.
Para `packs/<publicos>/` o resultado deve ser **zero**.

## Onde cada coisa pode aparecer

| Categoria | `core/` | `governance/` | `packs/<cliente>/` (privado) | `packs/cms-gherkin/` | `packs/us-avaliator/` | `packs/<empresa>-internal/` (privado) |
|-----------|---------|---------------|------------------------------|----------------------|-----------------------|----------------------------------------|
| Nome de cliente / sigla | NUNCA | NUNCA | OK | NUNCA | so se sanitizado | NUNCA |
| Sistemas legados de cliente | NUNCA | NUNCA | OK | NUNCA | NUNCA | NUNCA |
| Marketplaces / fornecedores | NUNCA | NUNCA | NUNCA | NUNCA | NUNCA | OK |
| Codigos SKU / regras internas | NUNCA | NUNCA | NUNCA | NUNCA | NUNCA | OK |
| API keys / segredos | NUNCA | NUNCA | NUNCA | NUNCA | NUNCA | NUNCA (vai em `.env` local) |

## Arquivos NUNCA commitar

Bloqueados pelo `.gitignore` (verificar antes de cada commit):

- `.env`, `.env.local`, `.env.*.local`
- `*.pem`, `*.key`, `*.p12`
- `credentials.json`
- `secrets/`
- `evidence/`, `prints/`, `massas/` (dados de cliente em packs)
- `*-CONFIDENCIAL.*`, `*-PRIVATE.*`
- Test outputs (`test_out.txt`, etc.)
- Arquivos `FLAG_WORDS_PRIVATE.md` (lista privada da empresa adotante).

## Procedimento de incidente

Se um segredo ou dado de cliente for commitado por engano:

### Severidade 1 - segredo ativo exposto (API key, password, token)

1. **Imediato:** rotacionar o segredo no provedor (Anthropic, OpenAI, etc.).
2. **Imediato:** revogar a API key exposta.
3. **Em < 1h:** remover do historico do Git (`git filter-repo` ou
   `git filter-branch`), force push se ja foi enviado para remoto.
4. **Em < 1h:** notificar Sofia CIAO + decisor humano.
5. **Em < 24h:** abrir capability review para a gem que commitou.
6. **Em < 7 dias:** atualizar `.gitignore` se houver gap.

### Severidade 2 - dado de cliente exposto (PII, IP)

1. **Imediato:** identificar o cliente afetado.
2. **Em < 1h:** notificar decisor humano (que decide se notifica cliente).
3. **Em < 4h:** remover do repo (do branch principal + historico se for
   publico).
4. **Em < 24h:** auditoria de outras exposicoes semelhantes.
5. **Em < 7 dias:** atualizar palavras-bandeira na lista privada.

### Severidade 3 - referencia a cliente em core/governance (sem dado)

1. **Em < 24h:** abrir PR de sanitizacao.
2. **Em < 7 dias:** revisao de outras referencias.

## IP de terceiros

Material de autoria de terceiros (catalogos externos, prompts copiados,
bibliotecas adaptadas) NUNCA entra em `core/`, `packs/`, ou `governance/`
sem:

- Auditoria de origem da autoria.
- Autorizacao de uso (licenca aberta ou contrato).
- Atribuicao explicita ao autor original.

## Conformidade

- LGPD: se houver dado pessoal de qualquer pessoa identificavel, tratar
  como dado sensivel mesmo que seja "publico".
- GDPR: aplicavel se houver dado de cidadao europeu - tratar com mesmo
  rigor.
- Contratos com cliente: prevalecem sobre esta politica se forem mais
  rigorosos.

## Consumo de token como risco operacional

> Token nao e so dinheiro - e risco operacional. Convocar squad
> completa para uma feature pequena pode 5x-10x o custo sem agregar
> qualidade. Em volume mensal, isso vira blocker de orcamento.

Diretrizes:

- Toda sessao deve usar o **menor modo de ativacao** que resolve a
  tarefa (`core/docs/AGENT_ACTIVATION_POLICY.md`).
- Code review automatico em init de feature: **proibido** por consumir
  token sem necessidade.
- Convocar Sofia CIAO em tarefa tatica: **proibido** por consumir
  modelo premium sem decisao em jogo.
- Convocar agentes "por garantia" ou "pra ouvir opiniao": **proibido**
  por gerar ruido sem decisao.
- Monitorar custo mensal por modelo e por modo. Se houver desvio > 50%
  da media, abrir capability review.
- Quando suspeitar de loop de convocacao redundante (mesma squad
  resolvendo o mesmo tipo de tarefa 3+ vezes), transformar em ritual
  com escopo definido ou gem dedicada (reduz custo recorrente).

Severidade do incidente de token:

| Severidade | Trigger | Acao |
|------------|---------|------|
| **Sev T1** | Sessao unica > 500k tokens em modo PAR/MINI | Pause imediato, revisao da convocacao |
| **Sev T2** | Custo mensal > 2x media historica | Revisao em retro + ajuste de defaults |
| **Sev T3** | Repeticao de anti-pattern (code review automatico, Sofia em tatico) | Atualizar gem que causou + capability review |

Ver `core/docs/TOKEN_ECONOMY.md` para a lista completa de anti-patterns
e diretrizes de modelo por modo de ativacao.

## Auditoria

Sofia CIAO faz revisao mensal de:

- Resultado do grep de palavras-bandeira em core/governance.
- Verificacao de `.gitignore` cobrindo tudo necessario.
- Incidentes registrados no mes.

Resultado vira retro no proximo hackathon ou em capability review da gem
que causou (se houve incidente).

## Atualizacao desta politica

Mudancas via PR com:

- Aprovacao do decisor humano da empresa adotante.
- Aprovacao Sofia CIAO.
- Atualizar `.gitignore` em conjunto se necessario.
- Atualizar lista privada de palavras-bandeira (em geral so adiciona,
  nao remove).

## Veja tambem

- `.gitignore`
- `LICENSE`
- `core/docs/AGENT_CERTIFICATIONS.md` (cert CHAT-PROMOTION reduz risco de
  exposicao em chat)
- `core/docs/AGENT_ACTIVATION_POLICY.md` (modos de ativacao)
- `core/docs/TOKEN_ECONOMY.md` (anti-patterns de consumo)
