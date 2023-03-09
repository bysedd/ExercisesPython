import sys

sys.set_int_max_str_digits(9 ** 4)

while True:
    try:
        qtd = int(input('How many numbers do you want to calculate (0 to exit): '))
        if qtd == 0:
            raise EnvironmentError

        for i in range(qtd):
            n = int(input(f'\nEnter the {i + 1}º number: '))
            if n < 0:
                raise ValueError

            ultimo = 1
            penultimo = 1
            fibo = [0, 1]

            for count in range(2, n):
                termo = ultimo + penultimo
                penultimo = ultimo
                ultimo = termo
                fibo.append(termo)
            print(f"Fib({n}) = {fibo[n] if n < 2 else fibo[n - 1]}")
        print()
    except ValueError:
        print('\033[31mInvalid value. Try again.\033[m\n')
    except EnvironmentError:
        print('\033[32mEnd of program\033[m')
        break
