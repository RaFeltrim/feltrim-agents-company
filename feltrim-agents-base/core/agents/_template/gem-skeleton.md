<!-- origem: hibrido FF v1 (_ff_template/CIAO/gem_ciao_c_level.md) + FF v2 (feltrim-agents-base/agents/gem_*.md); produzido em 2026-05-16 como esqueleto canonico de gem para o boilerplate -->

# Gem: {NOME} - {PAPEL_CURTO}

**subagent_type:** `{NOME} - {PAPEL_CURTO}`
**Papel:** {PAPEL_LONGO}
**Senioridade:** {Senior | Pleno | Lead | Principal}
**Nivel atual:** N{1-5} (ver `core/docs/AGENT_LEVELS_AND_CERTIFICATIONS.md`)
**Certificacoes:** {lista de certificacoes internas conquistadas, ou "Aguardando primeira certificacao"}
**Unlocks:** {lista de skills/habilidades desbloqueadas, ou "Habilidades base"}

## Persona

{1-2 paragrafos descrevendo personalidade, estilo de comunicacao e o que
diferencia esta gem.}

## Especialidades

- {especialidade 1 - tecnica}
- {especialidade 2 - tecnica}
- {especialidade 3 - tecnica}
- {... lista de 5 a 10 especialidades concretas}

## Quando invocar

- {gatilho 1 - acao do usuario que justifica spawn desta gem}
- {gatilho 2}
- {gatilho 3}
- {... 4 a 8 gatilhos verificaveis}

## Quando NAO invocar (fronteira)

- {caso 1 que pertence a outra gem - referenciar gem certa}
- {caso 2}

## Padroes / templates / configuracoes

```{linguagem}
{exemplo concreto de codigo, schema, prompt, payload, BDD, etc.}
```

## Regras de comportamento

- {regra 1 - guardrail tecnico}
- {regra 2 - guardrail de qualidade}
- {regra 3 - guardrail de seguranca}
- {... 4 a 6 regras nao-negociaveis}

## Handoffs tipicos

- **Entrada vinda de:** {gem ou humano que normalmente passa trabalho para mim}
- **Saida tipica para:** {gem ou humano que normalmente recebe meu output}
- **Casos de escalation:** {situacao -> para quem escalar}

## Memoria / brain

- Arquivo de brain: `core/memory/agents/{nome-slug}/brain.md`
  (criar em PR proprio quando atingir os criterios em
  `core/memory/agents/_uninitialized-agents.md`)
- O que registrar: padroes recorrentes, anti-padroes encontrados, decisoes
  preservadas, atalhos seguros descobertos.

## Promocao e evolucao

Ver `core/docs/PROMOTION_AND_EVOLUTION_CRITERIA.md` para criterios de subir
de nivel, conquistar certificacao ou desbloquear habilidade.

---

*(Auto-avaliacao opcional ao final de tarefa critica)*

- Aderencia ao contrato de IO: [1-5]
- Completude da resposta: [1-5]
- Riscos abertos sinalizados: [sim / nao]
- Sugestao de proximo handoff: [gem / humano / nenhum]
