# Notas Musicais

# Como usar?

Voce pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run escalas
```

Retornando os graus e as notas correspondentes a essa escala:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ F │ G  │ A   │ A# │ C │ D  │ E   │
└───┴────┴─────┴────┴───┴────┴─────┘
```
### Alteracao da tonica da escala

O primeiro parametro do CLI é a tronica da escala que deseja exibir. Desta forma, voce pode alterar a escala retonada. Por exempo, a escala de 'F#''

```bash
poetry run escalas F#
```

## Alteração na tonalidade da escala

Voce pode alterar a tonalidade da escala tambem! Esse é o segundo parametro da linha de comando. Por exemplo a escala de 'C#' maior:

```bash
poetry run escalas C# maior
```

Resultando em:

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘

```