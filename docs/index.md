# Notas Musicais

Notas musicais é um CLI para ajudar na formaçao de escalas e acordes
Temos dois comandos disponiveis: `escala` e `acorde`

# Como usar?

## Escalas

Voce pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run notas-musicais escala
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
poetry run notas-musicais escala F#
```
Resultando em:

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘

```

## Alteração na tonalidade da escala

Voce pode alterar a tonalidade da escala tambem! Esse é o segundo parametro da linha de comando. Por exemplo a escala de `C#`` maior:

```bash
poetry run notas-musicais escala C# menor
```

Resultando em:

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ C# │ D# │ E   │ F# │ G# │ A  │ B   │
└────┴────┴─────┴────┴────┴────┴─────┘

```

## Acordes

Uso basico
```bash
poetry run notas-musicais acorde C+
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variacoes na cifra

```bash
poetry run notas-musicais acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V  ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até o momento voce pode usar acordes maiores, menores, diminutos e aumentados

## Mais informaçoes sobre o CLI

Para descobrir outras opcoes, voce pode usar a flag `--help``
