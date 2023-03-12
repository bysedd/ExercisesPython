"""
Recriando a Música dos PATINHOS
https://www.computersciencemaster.com.br/exercicios-recriando-musica-patinhos/

Se você está precisando de um exercício sobre laços de repetição, aqui vai um! Você lembra daquela música irritante
da Xuxa que contava a história dos patinhos que foram brincar e sumiram? Essa música era uma febre entre as crianças
e hoje está aqui para te ensinar programação.

Você pode perceber que ela possui uma sequência lógica bem definida de quantos patinhos vão passear se perdem e
depois retornam. A música repete os parágrafos várias vezes e permite que você automatize essa construção por meio de
linguagem de programação.

Lembre-se que esse exercício sobre laços de repetição não passa de uma brincadeira e você pode usar para praticar
suas habilidades de programação 🙂

Relembre essa música inspiradora:
Xuxa, a rainha dos baixinhos, criou uma música que tem o seguinte formato:

n patinhos foram passear
Além das montanhas
Para brincar
A mamãe gritou: Quá, quá, quá, quá
Mas só n-1 patinhos voltaram de lá.

Que se repete até nenhum patinho voltar de lá.
Ao final, todos os patinhos voltam:

A mamãe patinha foi procurar
Além das montanhas
Na beira do mar
A mamãe gritou: Quá, quá, quá, quá
E os n patinhos voltaram de lá.

Agora meu amigo, é a sua vez. Você precisa automatizar a impressão dessa música no terminal usando for e while. Mas
lembre-se não adianta nada você colocar ela inteira dentro de um print (assim você não aprende nada).

Procure os pontos que se repetem e crie uma estrutura capaz de mostrar esses pontos automaticamente.
"""

from time import sleep


def main(_patinhos: int = 5):
    if _patinhos < 1:
        raise ValueError('O número de patinhos deve ser maior que 0.')
    # Dicionário com os plurais dos patinhos
    patinhos: dict[int, str] = {
        1: 'patinho',
        tuple(range(2, _patinhos + 1)): 'patinhos',
    }
    # Texto da música
    texto: str = 'Além das montanhas para brincar\n' \
                 'A mamãe gritou: "Quá, quá, quá, quá"'
    # Texto final
    final: str = 'A mamãe patinha foi procurar\n' \
                 'Além das montanhas, na beira do mar\n' \
                 'A mamãe gritou: "Quá, quá, quá, quá!"'
    if _patinhos == 1:
        # Primeira parte
        print(f'{_patinhos} {patinhos[1]} foi passear')
        print(texto)
        print(f'Mas nenhum {patinhos[1]} voltou de lá.\n')
        sleep(1)
        # Segunda parte
        print(final)
        print(f'E um {patinhos[1]} voltou de lá.')
    else:
        # Primeira parte
        for i in range(_patinhos, 0, -1):
            if i != 1:
                print(f'{i} {patinhos[1]}s foram passear')
                print(texto)
                print(f'Mas só {i - 1} {patinhos[1]} voltaram de lá.\n')
            else:
                print(f'{i} {patinhos[1]} foi passear')
                print(texto)
                print(f'Mas nenhum {patinhos[1]} voltou de lá.\n')
            sleep(1)
        # Segunda parte
        print(final)
        print(f'E os {_patinhos} {patinhos[1]}s voltaram de lá.')


if __name__ == '__main__':
    try:
        main(_patinhos=10)
    except (ValueError, KeyboardInterrupt) as e:
        print(e)
