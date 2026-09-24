# ADRs - Architectural Decision Records (genericos)

Decisoes arquiteturais universais do Feltrim Agents Framework: aplicaveis a
qualquer projeto/empresa que use o boilerplate.

ADRs especificos de empresa/cliente (integracoes proprietarias, regras
operacionais internas, automacoes especificas) ficam no pack
correspondente em `packs/<pack>/adr/`, nunca em `core/`. Ver
`DECISIONS_PENDING.md` item 3 e `governance/SECURITY_AND_PRIVACY.md`.

## ADRs ja consolidados (genericos)

Aguardando primeira leva. Sugestoes de partida (a serem escritas em PRs
futuros):

- ADR-CORE-001: Memoria transacional persistente para agentes deve ser
  versionavel e separada de navegacao pessoal (Obsidian/Notion = navegacao,
  Git/Supabase = fonte de verdade).
- ADR-CORE-002: Workers de fila assincrona devem receber comando via stdin,
  nunca via args de shell (anti command-injection).
- ADR-CORE-003: Escrita de arquivos de output usa flag atomic create (`wx`
  em Node, `O_EXCL` em geral) para evitar overwrite silencioso.
- ADR-CORE-004: Conversas sociais/rituais entre agentes nao sao fonte oficial
  de decisao tecnica; toda decisao auditavel migra para ADR/backlog/runbook.

## Formato sugerido

```
# ADR-CORE-NNN: <Titulo curto>

**Status:** proposed | accepted | superseded | deprecated
**Data:** YYYY-MM-DD
**Autor(es):** <agente(s) responsavel(eis)>
**Decisor humano:** Rafael Feltrim

## Contexto

<situacao que motivou a decisao>

## Decisao

<o que foi decidido>

## Alternativas consideradas

- <alternativa 1>: <por que rejeitada>
- <alternativa 2>: <por que rejeitada>

## Consequencias

- <impacto positivo>
- <impacto negativo / debito tecnico criado>

## Revisao

- Data de revisao prevista: YYYY-MM-DD
- Trigger de revisao: <evento que obriga revisitar>
```
