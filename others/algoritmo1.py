data_nascimento = input('Data de nascimento: ')

if data_nascimento.__contains__('/'):
    s = data_nascimento.split('/')
    date_em_texto = f'{s[0]}-{s[1]}-{s[2]}'
    print(date_em_texto)

elif data_nascimento.__contains__('-'):
    s = data_nascimento.split('-')
    date_em_texto = f'{s[0]}/{s[1]}/{s[2]}'
    print(date_em_texto)
