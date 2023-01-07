"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    a. Se o usuário informar o valor de A igual a zero,
    a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, encerrando o programa;
    b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
    c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;
"""

from math import sqrt

try:
    a = int(input('a = '))

    if a == 0:
        raise ValueError

    b = int(input('b = '))
    c = int(input('c = '))

    delta = pow(b, 2) - 4 * a * c

    print(f'\n∆ = {delta}\n')

    if delta < 0:
        print('S = { } (não existe solução real)')
    else:
        x = ((b * -1) + sqrt(delta)) / (2 * a)
        y = ((b * -1) - sqrt(delta)) / (2 * a)

        if delta == 0:
            print(f'S = { {round(x, 3)} }')
        else:
            print(f'S = { {round(x, 3), round(y, 3)} }')

except ValueError:
    print('A equação não é de segundo grau!')
