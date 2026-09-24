# Pull Request

## Resumo (1-2 frases)

<!-- O que esta PR faz e por que -->

## Tipo de mudanca

- [ ] `feat` - novo conteudo (gem, protocolo, ritual, pack, doc)
- [ ] `fix` - correcao de bug em script / comportamento errado / link
- [ ] `docs` - mudanca apenas em documentacao
- [ ] `refactor` - reorganizacao sem mudar comportamento
- [ ] `chore` - manutencao (ci, deps, configs)
- [ ] `sec` - sanitizacao, leak fix, atualizacao de politica

## Areas tocadas

- [ ] `core/agents/`
- [ ] `core/protocols/`
- [ ] `core/docs/`
- [ ] `core/memory/`
- [ ] `core/skills/` ou `core/integrations/` ou `core/scripts/`
- [ ] `governance/`
- [ ] `packs/`
- [ ] `examples/`
- [ ] `docs/` raiz
- [ ] `.github/`
- [ ] Arquivos meta-raiz (README, CONTRIBUTING, etc.)

## Issue relacionada

<!-- Closes #<numero>  ou  Refs #<numero> -->

## Checklist de sanitizacao (OBRIGATORIO)

- [ ] Nao introduzi nome de cliente real, sistema interno proprietario,
      prefixo SKU, codigo de regra interno ou nome de pessoa interna ao
      cliente. Se a mudanca cita "<placeholder>", esta explicito.
- [ ] Nao committei `.env` real, credencial, API key, token ou
      certificado privado.
- [ ] Nao committei path absoluto da minha maquina local em arquivos
      publicos (`C:\Users\<nome>\...`, `/Users/<nome>/...`,
      `~/Desktop/...`).
- [ ] Configurei git local com email `<user>@users.noreply.github.com`
      (NAO email corporativo) antes de commitar.
- [ ] Conferi resultado do grep de palavras-bandeira (ver
      `governance/SECURITY_AND_PRIVACY.md`).

## Checklist de governanca (se aplicavel)

- [ ] Mudanca em hierarquia -> atualizei `governance/AGENT_HIERARCHY.md`
      E `governance/COMPANY_CHARTER.md`.
- [ ] Nova gem -> atualizei `core/docs/SQUAD_INDEX.md` com linha da gem.
- [ ] Nova certificacao -> atualizei `core/docs/AGENT_CERTIFICATIONS.md`
      E `governance/CERTIFICATION_POLICY.md` se a politica mudou.
- [ ] Novo unlock -> atualizei `core/docs/AGENT_UNLOCKS.md`.
- [ ] Novo protocolo -> atualizei `core/protocols/README.md` e o boot
      sequence se mudou.
- [ ] Mudanca em politica de seguranca -> atualizei
      `governance/SECURITY_AND_PRIVACY.md` E `SECURITY.md` raiz se
      relevante para reporters externos.

## Checklist de documentacao

- [ ] Mudei o mapa do repo -> atualizei `README.md` raiz.
- [ ] Adicionei novo arquivo -> referenciei a partir do README/index
      apropriado (nada orfao).
- [ ] Mudei algo versionado -> adicionei entrada em `CHANGELOG.md` raiz
      (secao `[Unreleased]`).
- [ ] Nao ha link quebrado em arquivos que toquei.

## Testes locais executados

<!-- Que checagens locais voce rodou antes de abrir o PR? -->

- [ ] Grep de palavras-bandeira da minha instalacao
- [ ] Checagem de links markdown
- [ ] Lint markdown
- [ ] Outro: 

## Revisores sugeridos

Conforme `CONTRIBUTING.md` -> "Onde sua contribuicao se encaixa":

- [ ] Sofia CIAO (auditoria de seguranca / governanca)
- [ ] Mariana (prompts / gens)
- [ ] Beatriz TL (arquitetura / protocolos)
- [ ] Marlon-PO / Claudia-PM (rituais / packs)
- [ ] Camila DevOps (CI / workflows)
- [ ] Laura UI (documentacao visual)

## Notas para revisores

<!-- Algo que voce quer destacar especificamente? Trade-off conhecido?
     Limitacao aceita? -->
