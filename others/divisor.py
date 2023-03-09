num = input('Digite um número: ')
choose: str = ''


def maior(n: int):
    for div in range(num - 1, 1, -1):
        if n % div == 0:
            print(f'O maior divisor de {n} é {div} o quociente obtido foi {n // div}')
            break


def menor(n: int):
    for div in range(2, n - 1, 1):
        if n % div == 0:
            print(f'O menor divisor de {n} é {div} o quociente obtido foi {n // div}')
            break


def check_prime(number: int) -> bool:
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            return True
    else:
        return False


if num.isnumeric():
    num = int(num)
    if num > 1:
        print()
        while choose not in ('maior', 'menor', 'ambos'):
            choose = input('Você quer achar o \033[34m"maior"\033[m divisor, '
                           'o \033[34m"menor"\033[m ou \033[34m"ambos"\033[m? ').lower().strip()[:5]
        print()
        if check_prime(num):
            print(f'Esse número é primo, logo, ele só pode ser dividido por 1 e {num}')
        else:
            if choose == 'maior':
                maior(num)
            elif choose == 'menor':
                menor(num)
            else:
                maior(num)
                menor(num)
    else:
        print('\033[31mNúmero precisa ser maior que 1\033[m')
else:
    print('\033[31mDigite um número!\033[m')
