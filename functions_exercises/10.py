"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente."""


def roll_dice() -> int:
    from random import randint
    return randint(1, 6) + randint(1, 6)


def play_craps(simulate: int=0) -> dict[str: int]:
    match = {'games': 0, 'win': 0, 'loss': 0}
    display = simulate == 0

    def jogar() -> None:
        if display:
            print('-' * 50)
            point = roll_dice()
            print(f'Você tirou {point}')

            if point in (7, 11):
                print('Você tirou um natural e ganhou!')
                match['win'] += 1
            elif point in (2, 3, 12):
                print('Você tirou um craps e perdeu!')
                match['loss'] += 1
            else:
                print('Você tirou um ponto.')
                point = roll_dice()
                print(f'Você tirou {point}')

                if point == 7:
                    print('Você tirou um 7 e perdeu!')
                    match['loss'] += 1
                else:
                    print('Você tirou o ponto novamente e ganhou!')
                    match['win'] += 1
            match['games'] += 1
        else:
            point = roll_dice()
            if point in (7, 11):
                match['win'] += 1
            elif point in (2, 3, 12):
                match['loss'] += 1
            else:
                point = roll_dice()
                if point == 7:
                    match['loss'] += 1
                else:
                    match['win'] += 1
            match['games'] += 1
    if not simulate:
        while True:
            jogar()
            continuar = None
            while continuar not in ('S', 'N'):
                continuar = input('Deseja jogar novamente (S/N)? ').upper()
            if continuar == 'N':
                break
    else:
        for _ in range(simulate):
            jogar()                
    return match


def resultado(result: dict) -> None:
    print('-' * 50)
    print(f'Você jogou {result["games"]} vezes.')
    print(f'Você ganhou {result["win"]} vezes.')
    print(f'Você perdeu {result["loss"]} vezes.')
    print(f'Você teve {round(result["win"] / result["games"] * 100)}% de aproveitamento.')
    print('-' * 50)


if __name__ == '__main__':
    resultado(play_craps())
