"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter
14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e
uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terão um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o
usuário repita esse cálculo para novos valores de entrada todas às vezes que desejar.
"""

from colorama import Fore, Style


def conversao(hora, minuto):
    from datetime import datetime

    if 0 < hora <= 12:
        return datetime.strptime(f"{hora}:{minuto}", "%I:%M").strftime("%I:%M %p")
    return datetime.strptime(f"{hora}:{minuto}", "%H:%M").strftime("%H:%M %p")


def saida(hora, minuto):
    print(f"{Fore.LIGHTBLUE_EX}{conversao(hora, minuto)}{Style.RESET_ALL}")


print(f"{Fore.LIGHTRED_EX}Digite um número negativo para sair{Style.RESET_ALL}")

while True:
    try:
        h = int(input("\nDigite alguma hora (0-23): "))
        m = int(input("Digite algum minuto (0-59): "))
        if h < 0 or m < 0:
            break
        saida(h, m)
    except ValueError as err:
        print(f"{Fore.RED}{err}{Style.RESET_ALL}")

print(f"\n{Fore.LIGHTYELLOW_EX}Obrigado por usar este script{Style.RESET_ALL}")
