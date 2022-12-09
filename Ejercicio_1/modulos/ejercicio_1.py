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

def es_valido(sudoku, fila, columna, valor):
    for i in range(9):
        if sudoku[fila][i] == valor:
            return False
        if sudoku[i][columna] == valor:
            return False
    fila = fila // 3
    columna = columna // 3
    for i in range(3):
        for j in range(3):
            if sudoku[fila * 3 + i][columna * 3 + j] == valor:
                return False
    return True


def resolver_sudoku(sudoku):
    for fila in range(9):
        for columna in range(9):
            if sudoku[fila][columna] == 0:
                for valor in range(1, 10):
                    if es_valido(sudoku, fila, columna, valor):
                        sudoku[fila][columna] = valor
                        if resolver_sudoku(sudoku) :
                            return sudoku
                        else: 
                            sudoku[fila][columna] = 0
                return  False
    return sudoku



def imprimir_sudoku(sudoku):
    for fila in range(9):
        for columna in range(9): 
            print(sudoku[fila][columna], end=" ")
        print()
        
        
def ejercicio_1():
    imprimir_sudoku(resolver_sudoku(sudoku))


