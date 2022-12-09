from math import factorial


lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


def numero_permutaciones():
    for i in range(1, len(lista) + 1):
        print('Numero de permutaciones de {} elementos: {}'.format(i, factorial(i)))



