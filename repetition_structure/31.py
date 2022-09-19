"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número
desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para
indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o
cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao
ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 8.00
Dinheiro: R$ 20.00
Troco: R$ 12.00
...
"""

while True:
    print(f'{"=" * 25}\n'
          f'{"Lojas Tabajara":^25}\n'
          f'{"=" * 25}')
    print('ℹ️ Digite 0 para parar\n')

    produtos: list = []
    price: float = 1
    cont: int = 1

    while price != 0:
        price = float(input(f'Produto {cont}: R$ '))
        produtos.append(price)
        cont += 1

    total = sum(produtos)
    print(f'\nTotal: R$ {total:.2f}')

    dinheiro: float = float(input('Dinheiro: R$ '))

    troco = dinheiro - total
    while troco < 0:
        print(f'\nEstá faltando R$ {abs(troco):.2f}')
        dinheiro: float = float(input('Adicionar dinheiro: R$ '))
        troco += dinheiro

    print(f'\nTroco: R$ {troco:.2f}')

    resp = input('\nDeseja fazer uma nova compra (s/n)? ')[0].lower()
    while 's' != resp != 'n':
        resp = input('Deseja fazer uma nova compra (s/n)? ')[0].lower()

    if resp == 's':
        print()
    else:
        break

print(f'\nObrigado pela preferência!')

input()
