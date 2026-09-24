# Politica de Seguranca - Feltrim Agents Base

## Tipos de risco que aceitamos report

Para este boilerplate publico, ha 3 categorias de risco que devem ser
reportadas de forma privada (NUNCA em issue publica):

### 1. Vazamento de palavras-bandeira ou IP de cliente

Se voce encontrar mencao a cliente real, sistema interno proprietario, ou
qualquer "flag word" em arquivos do `core/`, `governance/`, `examples/` ou
raiz, REPORT IMEDIATO.

Exemplos do que vazaria indevidamente:

- Nome de cliente / sistema cliente em arquivo publico.
- Codigo SKU especifico / regra interna de marketplace.
- Path absoluto da maquina de algum colaborador.
- Email corporativo em commit.
- Nome de pessoa interna a cliente.

### 2. Credencial / segredo exposto

Se voce encontrar:

- API key, token, password, certificado privado committado.
- URL com credencial embedded (`https://user:pass@host`).
- Arquivo `.env` real (nao o `.env.example`) committado.
- Chave privada (.pem, .key, .p12) committada.

REPORT IMEDIATO e nao abra issue publica.

### 3. Vulnerabilidade em script ou workflow

- Codigo em `core/scripts/` ou `.github/workflows/` que executa input externo
  sem sanitizacao.
- Workflow CI que vaza secret em logs.
- Script de pack que aceita injection.

## Como reportar privadamente

**Opcao A - GitHub Security Advisory (preferido):**

1. Acesse `https://github.com/RaFeltrim/feltrim-agents-base/security/advisories/new`
2. Preencha o relato com:
   - Tipo (1 / 2 / 3 acima)
   - Localizacao exata (path + linha)
   - Severidade que voce atribui (S1 ativo / S2 dado / S3 referencia)
   - Reproducao se aplicavel

**Opcao B - Issue privada via email do GitHub:**

1. Abra issue mencionando apenas "Security report - aguardando contato
   privado" no titulo, SEM detalhes.
2. Mantenedor abrira canal privado.

**NAO faca:**

- Issue publica com PoC de leak.
- Comentario publico com flag word concreta.
- Discussao publica de PoC ou conteudo vazado.

## Tempo de resposta esperado

| Severidade | Triagem | Mitigacao | Comunicacao |
|------------|---------|-----------|-------------|
| S1 - segredo ativo exposto | < 4h | < 24h (rotacionar + remover historico) | publico apos correcao |
| S2 - dado de cliente / IP vazado | < 24h | < 7 dias | privado primeiro, publico se decidir |
| S3 - referencia textual sem dado | < 7 dias | < 14 dias | publico (PR de sanitizacao) |

## Procedimento de incidente (interno)

Detalhado em `governance/SECURITY_AND_PRIVACY.md`. Resumo:

1. Confirmar severidade.
2. Rotacionar segredo se aplicavel (S1).
3. Remover do historico do Git se publico (`git filter-repo`).
4. Notificar Sofia CIAO (auditora interna).
5. Notificar decisor humano (Rafael Feltrim).
6. Capability review se a gem causou.
7. Atualizar `.gitignore` ou checagem CI se houver gap.

## Para empresas adotantes

Se voce adotou este boilerplate na sua empresa e teve incidente envolvendo
seu cliente, NAO reporte aqui. Trate internamente conforme contrato com seu
cliente. Esta politica vale apenas para incidentes envolvendo o boilerplate
publico em si.

## Versoes suportadas

| Versao | Suportada |
|--------|-----------|
| 0.1.x (atual) | Sim - mantida ativamente |
| < 0.1 | Nao se aplica (primeira release publica) |

## Reconhecimento

Pesquisadores que reportarem responsavelmente serao reconhecidos no
`CHANGELOG.md` (a menos que pecam anonimato).

## Veja tambem

- `governance/SECURITY_AND_PRIVACY.md` - politica interna completa
- `CONTRIBUTING.md` - como contribuir com correcoes
- `CODE_OF_CONDUCT.md` - codigo de conduta
