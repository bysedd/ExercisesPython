n = int(input('\033[0:34m!\033[m'))
f = 1

if n < 0:
    print('\033[0:31mFatorial não existe\033[m')
else:
    print()
    for c in range(f, n + 1):
        f *= c
    print(f'Result = \033[0:32m{f}\033[m')
    print(f'Contains \033[0:34m{len(str(f))}\033[m number(s)')
