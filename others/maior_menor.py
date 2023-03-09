from functools import reduce


def casas_decimais(lista: list):
    cd: int = len(str(lista[0]).split('.')[1])
    for valor in lista:
        if len(str(valor).split('.')[1]) > cd:
            cd: int = len(str(valor).split('.')[1])
    return cd


try:
    n = input('Quantos valores irá digitar? ')
    if n == '0':
        print('OK, não irei digitar nenhum valor.')
        exit(1)
    while not n.isnumeric():
        print('\033[31mDigite um número válido!\033[m')
        n = input('\nQuantos valores irá digitar? ')
    n = int(n)

    if n > 0:
        print()
        valores = []
        for i in range(1, n + 1):
            v = float(input(f'Digite o {i}º valor: '))
            valores.append(v)
        print(f'\nValores digitados: {len(valores)}')
        print(f'Maior valor: {max(valores)}')
        print(f'Menor valor: {min(valores)}')
        print(f'Soma de todos os valores: {sum(valores):.{casas_decimais(valores)}f}')
        print(f'Multiplicação de todos os valores: {reduce(lambda x, y: x * y, valores)}')
    else:
        raise ValueError
except ValueError:
    print('\033[31mValor inválido!\033[m')
