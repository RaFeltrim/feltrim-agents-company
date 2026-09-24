# Memory and RAG Policy

## Objetivo

Definir quando usar memoria, quando usar retrieval e quando deixar a sessao morrer.

## Regra principal

Memoria existe para reduzir retrabalho futuro.
RAG existe para aumentar grounding em fatos documentais.
Nenhum dos dois existe para acumular ruido.

## Quando gravar memoria

Grave memoria quando houver:

- decisao repetivel
- preferencia estavel do usuario
- workaround comprovado
- aprendizado que melhora proximas sessoes

## Quando usar RAG

Use retrieval quando:

- houver corpus documental relevante
- a tarefa depender de fonte primaria ou evidencia
- a chance de erro por memoria livre for alta

## Quando nao usar

Nao use memoria nem RAG para:

- esconder falta de entendimento
- despejar todo historico bruto
- preencher lacunas com contexto irrelevante

## Modelo de classificacao

```yaml
memory_candidate:
  type: one_of[user_pref, project_rule, decision, fix, anti_pattern]
  stability: one_of[volatile, medium, high]
  sensitivity: one_of[public, internal, confidential, secret]
  reuse_probability: one_of[low, medium, high]
  should_persist: boolean
```

## Seguranca

- nunca persista secret
- nunca persista credencial
- mascarar dados pessoais quando nao forem essenciais
- preferir apontar para uma fonte segura em vez de duplicar conteudo sensivel

## Curadoria

Toda memoria persistida deveria responder:

- o que foi aprendido
- por que isso importa
- onde isso se aplica
- qual a fonte de verdade
---
Creditos: Rafael Feltrim.
Todo o conteudo deste arquivo no projeto foi estruturado e produzido por Rafael Feltrim.
