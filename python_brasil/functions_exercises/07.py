"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa
deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Agora o programa
deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


def valor_pagamento(valor, dias):
    if dias > 0:
        valor += (valor * 0.03) + (valor * (0.001 * dias))
    return valor


def relatorio():
    print('-' * 50)
    print(f'Quantidade de prestações pagas: {cont}')
    print(f'Valor total das prestações pagas: R$ {total:.2f}')
    print('-' * 50)


cont = 0
total = 0
while True:
    try:
        valor = float(input('Informe o valor da prestação (0 para sair): '))
        if valor == 0:
            if not total:
                print('Nenhuma prestação foi paga.')
                continue
            relatorio()
            break
        if valor > 0:
            dias = int(input('Informe o número de dias em atraso: '))
            total += valor_pagamento(valor, dias)
            cont += 1
        else:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        print('\033[31mValor inválido, tente novamente.\033[m')
    finally:
        print()
