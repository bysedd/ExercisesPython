try:
    num = int(input('Digite um valor para ver sua tabuada? '))
    fim = int(input('Até qual número você gostaria de multiplicar? '))
    print()
    for c in range(1, fim + 1):
        resultado = num * c
        print(f'\033[1;36m{num} x {c}\033[m = \033[1;32m{resultado}\033[m')
except ValueError:
    print('\033[1:31mDigite apenas números inteiros!\033[m')
