NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tonica e uma tonalidade
    
    Parameters:
        tonica: Nota que será a tonica da escala
        tonalidade: Tonalidade da escala

    Returns:
        um dicionario com as notas da escala e os graus

    Raises:
        ValueError: Caso a tonica nao seja uma nota valida
        KeyError: Caso a escala nao foi implementada

    Examples:
        >>> escala('C', 'maior')   
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError (f'Essa nota nao existe, tente uma dessas {NOTAS}')
    except KeyError:
        raise KeyError(
            f'Essa escala nao existe ou nao foi implementada. Tente uma dessas {list(ESCALAS.keys())}'
            )

    temp = []
    
    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
