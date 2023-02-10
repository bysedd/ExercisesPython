"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide
a entrada e permita repetir a operação.
"""

while True:
    a = input("Digite a população do país A: ")
    b = input("Digite a população do país B: ")
    crescimento_a = float(
        input("Digite a taxa de crescimento do país A: ")) / 100
    crescimento_b = float(
        input("Digite a taxa de crescimento do país B: ")) / 100
    anos = 0

    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
    else:
        continue

    if a < b:
        while a <= b:
            a += a * crescimento_a
            b += b * crescimento_b
            anos += 1
    else:
        while a >= b:
            a += a * crescimento_a
            b += b * crescimento_b
            anos += 1

    print(
        f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.\n"
    )
