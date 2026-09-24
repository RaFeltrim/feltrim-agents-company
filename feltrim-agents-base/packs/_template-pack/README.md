# Template Pack

Esqueleto para criar packs novos do Feltrim Agents Framework.

## Estrutura

```
_template-pack/
|-- README.md      (este arquivo - sobrescrever no seu pack)
|-- agents/        (gens especificas do pack: gem_<pack>_<funcao>.md)
|-- brains/        (brains operacionais: <slug>/brain.md)
|-- docs/          (operating contract, capability matrix, CHANGELOG)
`-- skills/        (skills locais do pack, ou referencia para skills no repo do projeto)
```

## Como instanciar

```bash
PACK=<seu-pack>
cp -r packs/_template-pack packs/$PACK
```

Depois siga o passo a passo em `examples/example-pack-init.md`.

## Checklist minimo de um pack novo

- [ ] `README.md` reescrito com visao do pack, atencao/flag words, estrutura
- [ ] Pelo menos 1 gem em `agents/` (ou referenciar gens core sem criar novas)
- [ ] Brain inicial em `brains/<slug>/brain.md` se houver gem propria
- [ ] `docs/OPERATING_CONTRACT.md` com regras nao-negociaveis do pack
- [ ] `docs/CAPABILITY_MATRIX.md` com responsabilidades por gem
- [ ] `docs/CHANGELOG.md` para versionar mudancas
- [ ] `skills/README.md` indicando se as skills vivem aqui ou no repo do projeto
- [ ] Auditoria contra `governance/SECURITY_AND_PRIVACY.md` (zero flag words da
      sua instalacao em arquivos do pack que devem ser publicos)

## Veja tambem

- `examples/example-pack-init.md` - passo a passo completo
- `core/agents/_template/gem-skeleton.md` - skeleton de gem
- `core/agents/_template/INDEX_TEMPLATE.md` - template de roster
- `core/memory/agents/_templates/agent-brain-template.md` - template de brain
- `governance/SECURITY_AND_PRIVACY.md` - palavras-bandeira e antes de
  commitar
