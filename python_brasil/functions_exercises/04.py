"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def valor(n):
    if n > 0:
        return "P"
    return "N"


print(valor(1))
print(valor(0))
print(valor(-1))
