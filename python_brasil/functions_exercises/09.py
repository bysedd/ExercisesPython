# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


def reverse_number(number: int) -> int:
    if str(number)[0] == '-':
        return int('-' + str(number)[1:][::-1])
    return int(str(number)[::-1])


while True:
    try:
        number = int(input('Informe um número (0 para sair): '))
        if number == 0:
            break
    except ValueError:
        print('\033[31mValor inválido, tente novamente.\033[m')
    else:
        print(f'O reverso de {number} é {reverse_number(number)}.')
