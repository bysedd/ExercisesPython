"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def imprimir(n: int):
    for i in range(1, n + 1):
        print(1, end="\t")
        for j in range(2, i + 1):
            print(j, end="\t")
        print()


imprimir(7)
