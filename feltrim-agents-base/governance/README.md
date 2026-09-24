# Governance - Feltrim Agents Company

> Politicas oficiais da empresa Feltrim Agents Company. Tudo aqui e
> aplicavel a `core/` e a todos os packs. Mudancas exigem aprovacao do
> decisor humano (Rafael Feltrim).

## Documentos

- **`COMPANY_CHARTER.md`** - quem e a empresa, missao, valores, decisor humano, cultura "Unity, Tradition, Pride, Equity".
- **`AGENT_HIERARCHY.md`** - organograma, niveis, cadeia de escalada, quem pode delegar para quem.
- **`RITUALS_GUARDRAILS.md`** - regra explicita: rituais sao simbolicos, nao metricas. XP nao promove agente.
- **`PROMOTION_POLICY.md`** - politica oficial de promocao entre niveis (quem decide, quando, como audita).
- **`CERTIFICATION_POLICY.md`** - politica de emissao, manutencao e revogacao de certificacoes internas.
- **`SECURITY_AND_PRIVACY.md`** - lista de palavras-bandeira, procedimento de incidente, IP de terceiros.

## Relacao com core/

- `governance/` define a politica.
- `core/docs/` traz a operacionalizacao (matrizes, criterios concretos,
  catalogos).
- `core/protocols/` traz os contratos tecnicos.
- `packs/<pack>/` herda a politica via `core/`.

Se houver conflito entre `governance/` e `core/docs/`, `governance/`
prevalece.

Se houver conflito entre `governance/` e contrato com cliente, contrato com
cliente prevalece (se for mais rigoroso).

## Quem pode editar

Apenas via PR com:

- Aprovacao Rafael Feltrim (decisor humano).
- Sofia CIAO assinando como revisora.

## Atualizacao recente

(Inicializado em PR6 do plano `feltrim agents base rebrand`, 2026-05-16.)
