from notas_musicais.acordes import triade
from notas_musicais.escalas import escala

def _triade_na_escala(nota, notas_da_escala):
    """
    Saber se as notas de um acorde estao na escala.

    Examples:
        >>> _triade_na_escala('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'
        >>> _triade_na_escala('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
        >>> _triade_na_escala('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'B°'
    """
    tonica, terca, quinta = triade(nota, 'maior')
    match terca in notas_da_escala, quinta in notas_da_escala:
        case True, True:
            return tonica
        case False, True:
            return f'{tonica}m'
        case False, False:
            return f'{tonica}°'
        
def _converte_graus(cifra, grau):
    """
    Converte o grau relativo a cifra.

    Parameters:
        cifra: Uma cifra de um acorde
        grau: Grau em forma maior

    Examples:
        >>> _converte_graus('C', 'I')
        'I'
        >>> _converte_graus('Cm', 'I')
        'I'
        >>> _converte_graus('C°', 'I')
        'I°'
    """
    if 'm' in cifra:
        return grau.lower()
    elif '°' in cifra:
        return f'{grau.lower()}°'
    
    return grau

def campo_harmonico(tonica: str, tonalidade: str) -> dict[str, list[str]]:

    """
    Gera uma campo harmonico com base em uma tonica e uma tonalidade.

    Parameters:
        tonica: Primeiro grau do campo harmonico    
        tonalidade: Tonalidade para o campo. Ex: maior, menor, etc...
    
    Returns:
        Um campo harmonico

    Examples:
        >>> campo_harmonico('c', 'maior')
        {'acordes': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°']
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII°']}
       
        >>> campo_harmonico('c', 'menor')
        {'acordes': ['Cm', 'D°', 'D#', 'Fm', 'Gm', 'G#', 'A#']
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    notas, _graus = escala(tonica, tonalidade).values()
    acordes = [_triade_na_escala(nota, notas) for nota in notas]
    graus = [_converte_graus(acorde, grau) for acorde, grau in zip(acordes, _graus)
            ]

    return {'acordes': acordes, 'graus': graus}