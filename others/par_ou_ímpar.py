from random import randint

n = int(input('Número de jogadores: '))
jogadas = []

print()
for i in range(n):
    jogadas.append(randint(0, 10))
    print(f'Jogador {i + 1}: {jogadas[i]}')
print()

soma = sum(jogadas)
if soma % 2 == 0:
    print(f'{soma} = Par')
else:
    print(f'{soma} = Ímpar')
