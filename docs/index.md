# Notas Musicais

Notas musicais é um CLI para ajudar na formaçao de escalas e acordes e campos harmonicos.
Toda a aplicacao é baseada em um comando chadado `notas-musicais`. Esse comando tem um subcomando relacionado a cada acao que a aplicacao pode realizar. Como `escalas`, `acordes` e `campo-harmonico`.

{% include "templates/cards.html" %}

{% include "templates/instalacao.md" %}

## Como usar?

### Escalas

Voce pode chamar as escalas via linha de comando. Por exemplo:

```bash
{{ commands.run }} escala
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
{{ commands.run }} escala F#
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
{{ commands.run }} escala C# menor
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
{{ commands.run }} acorde C+

┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variacoes na cifra

```bash
{{ commands.run }} acorde C+

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
{{ commands.run }} campo-harmonico

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
{{ commands.run }} campo-harmonico [TONICA] [TONALIDADE]
```
#### Alteracao na tonica do campo harmonico

```bash
{{ commands.run }} campo-harmonico E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Alteracao da tonalidade do campo

Um exemplo utilizando o campo harmonico de `E` na tonalidade `menor`:

```bash
{{ commands.run }} campo-harmonico E menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informaçoes sobre o CLI

Para descobrir outras opcoes, voce pode usar a flag `--help``

```bash
{{ commands.run }} --help

╭─ Commands ─────────────────────────────────────────────────────────────────────╮
│ acorde                                                                         │
│ campo-harmonico                                                                │
│ escala                                                                         │
╰────────────────────────────────────────────────────────────────────────────────╯
```

### Mais informacoes sobre os subcomandos

As informacoes sobre os subcomandos podem ser acessadas usando a flag `--help` apos o nome do parametro. Um exemplo usando `help` nos campos harmonicos:

```bash
{{ commands.run }} campo-harmonico --help

 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE]            
                                                                                  
╭─ Arguments ────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tonica do campo harmonico [default: C]         │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmonico [default: maior] │
╰────────────────────────────────────────────────────────────────────────────────╯
```
