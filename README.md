# Notas Musicais
[![Documentation Status](https://readthedocs.org/projects/notas-musicaisv/badge/?version=latest)](https://notas-musicaisv.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/unclesummer/notas-musicais/graph/badge.svg?token=3WT83G8A9N)](https://codecov.io/gh/unclesummer/notas-musicais)
![CI](https://github.com/unclesummer/notas-musicais/actions/workflows/pipeline.yaml/badge.svg)

## Instalaçao

Para instalacao do cli do projeto recomendamos que use o `pipx` para fazer a instalacao:

```bash
pipx install notas-musicais
```

Embora isso seja somente uma recomendacao! Voce tambem pode instalar o projeto com o gerenciador de sua preferencia:

```bash
pip install notas-musicais
```

## Como usar?

### Escalas

Voce pode chamar as escalas via linha de comando. Por exemplo:

```bash
notas-musicais escala
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
notas-musicais escala F#
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
notas-musicais escala C# menor
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
notas-musicais acorde C+

┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variacoes na cifra

```bash
notas-musicais acorde C+

┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V  ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até o momento voce pode usar acordes maiores, menores, diminutos e aumentados

## Campo harmonico

Voce pode chamar os campos harmonicos via o subcomando `campo-harmonico`. Por exemplo:

```bash
notas-musicais campo-harmonico

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrao os parametros utilizados sao a tonica de `C` e o campo harmonico `maior`

### Alteracoes nos campos harmonicos

Voce pode alterar os parametros da tonica e da tonalidade.

```bash
notas-musicais campo-harmonico [TONICA] [TONALIDADE]
```
#### Alteracao na tonica do campo harmonico

```bash
notas-musicais campo-harmonico E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Alteracao da tonalidade do campo

Um exemplo utilizando o campo harmonico de `E` na tonalidade `menor`:

```bash
notas-musicais campo-harmonico E menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informaçoes sobre o CLI

Para descobrir outras opcoes, voce pode usar a flag `--help``

```bash
notas-musicais --help

╭─ Commands ─────────────────────────────────────────────────────────────────────╮
│ acorde                                                                         │
│ campo-harmonico                                                                │
│ escala                                                                         │
╰────────────────────────────────────────────────────────────────────────────────╯
```

### Mais informacoes sobre os subcomandos

As informacoes sobre os subcomandos podem ser acessadas usando a flag `--help` apos o nome do parametro. Um exemplo usando `help` nos campos harmonicos:

```bash
notas-musicais campo-harmonico --help

 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE]            
                                                                                  
╭─ Arguments ────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tonica do campo harmonico [default: C]         │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmonico [default: maior] │
╰────────────────────────────────────────────────────────────────────────────────╯
```