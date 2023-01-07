"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
sendo a quantia de imposto sobre venda expressa em porcentagem e custo, o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""


def soma_imposto(taxa_imposto, custo):
    print(f"item: R${custo:,.2f}, imposto: {round(taxa_imposto, 2)}%")
    custo += custo * (taxa_imposto * 0.01)
    print("imposto aplicado!")
    print(f"item: R${custo:,.2f}")


soma_imposto(5, 1956)
print()
soma_imposto(10, 3671)
print()
soma_imposto(2.5, 401)
