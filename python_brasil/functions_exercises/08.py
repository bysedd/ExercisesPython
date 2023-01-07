# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.


def count_digits(number: int) -> int:
    return len(str(number).replace('-', '').replace('+', ''))


while True:
    try:
        number = int(input('Informe um número (0 para sair): '))
        if number == 0:
            break
    except ValueError:
        print('\033[31mValor inválido, tente novamente.\033[m')
    else:
        print(f'O número {number} tem {count_digits(number)} digitos.')
