# Multimodal Extension

## Objetivo

Padronizar a extensao opcional da v3 para visao, audio e outros inputs nao textuais.

## Quando ativar

Ative a camada multimodal quando o problema depender de:

- screenshot
- design reference
- OCR
- imagem de produto
- audio
- video curto

## Regras

### 1. Nao trocar evidencia visual por palpite textual

Se a imagem for primaria, ela precisa ser tratada como fonte primaria.

### 2. Preservar rastreabilidade

Toda interpretacao multimodal deve apontar para o arquivo ou frame analisado.

### 3. Separar descricao de inferencia

- `descricao`: o que aparece
- `inferencia`: o que isso pode significar

## Envelope sugerido

```yaml
multimodal_artifact:
  type: one_of[image, screenshot, audio, video]
  source: string
  purpose: string
  observations: []
  inferences: []
  confidence: 0.0-1.0
```

## Agentes mais naturais para esta extensao

- `Laura` para UI e design
- `Fabio` para implementacao de interface
- `Rafael` para evidencias e regressao visual
- `Mariana` para OCR, parsing e pipelines multimodais
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
