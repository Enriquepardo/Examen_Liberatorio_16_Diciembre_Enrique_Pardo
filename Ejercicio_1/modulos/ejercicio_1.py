from random import choice


sudoku = [
        [5, 0, 0, 0, 4, 0, 0, 0, 9],
        [0, 2, 0, 0, 1, 0, 6, 8, 0],
        [0, 0, 9, 8, 7, 0, 1, 0, 0],
        [0, 0, 6, 7, 0, 0, 2, 0, 0],
        [0, 9, 0, 3, 5, 4, 0, 6, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 0, 0, 6, 0, 0, 0, 2],
        [0, 1, 4, 0, 3, 0, 0, 5, 7],
        [0, 0, 5, 0, 8, 7, 0, 0, 0]
]


def numero_fila(numero,fila,sudoku):        #  comprobar si el numero esta en la fila
    return numero in sudoku[fila] 

def numero_columna(numero,columna,sudoku):      #  comprobar si el numero esta en la columna
    return numero in [sudoku[i][columna] for i in range(9)]

def numero_caja(numero,fila,columna,sudoku):        #  comprobar si el numero esta en la caja
    caja_fila, caja_columna = caja_por_posicion(fila,columna)
    numeros_caja = ( 
                    fila[caja_fila*3:caja_fila*3 + 3]            # recorrer la caja
                    for fila in sudoku [caja_columna*3:caja_columna*3 + 3]
    )
    return numero in numeros_caja
    

def reducir(n):
    n /= 3
    if n == 0 or n != int(n):
        n += 1
    return int(n)

def caja_por_posicion(fila,columna):
    fila += 1
    columna += 1
    return reduce(fila) -1, reduce(columna) -1


def unpack(iterable):
    for item in iterable:
        yield from item

def numeros_posibles(sudoku, fila, columna):
    for numero in range(1, 10):
        if not numero_fila(numero,fila,sudoku) and not numero_columna(numero,columna,sudoku) and not numero_caja(numero,fila,columna,sudoku):
            yield numero


s = \
        """\
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        """

def resolver_sudoku():
    while True:
                numeros_posibles = {(fila, columna): None for fila in range(9) for columna in range(9)
                }
                
                # Obtener una lista de números posibles para cada una de 
                # las posiciones vacías.
                for fila in range(9):
                    for columna in range(9):
                        numeros = sudoku[fila][columna]
                        if numeros == 0:
                            opciones = list(
                                numeros_posibles(sudoku, fila, columna)
                            )
                            if opciones:
                                numeros_posibles[(fila, columna)] = opciones 
                
                # Remover valores vacíos y ordenar por la cantidad de 
                # posibilidades.
                possible_numbers = sorted(
                    (
                        (x, y)
                        for (x, y) in numeros_posibles.items()
                        if y is not None
                    ),
                    key=lambda kv: len(kv[1])
                )
                
                if possible_numbers: 
                    (fila, columna), numeros = numeros_posibles[0]
                    
                    sudoku[fila][columna] = choice(numeros)
                else:
                    break
                if 0 not in unpack(sudoku):
                    print(s.format(*(unpack(sudoku))))
                break
