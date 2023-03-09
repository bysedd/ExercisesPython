def confirm(c: str):
    while not (c.__contains__('y') or c.__contains__('n')):
        c = input('\033[1:31mIncorrect option\033[m\n'
                  'Do you want to continue(y/n)? ').lower()[0]


try:
    age = int(input('Enter an age: '))
    countPart, countMajor, countMinor = 0, 0, 0

    if 0 < age < 110:
        if 0 < age < 18:
            countMinor += 1
        else:
            countMajor += 1
        countPart += 1
        c = input('Do you want to continue(y/n)? ').lower()[0]
        confirm(c)

        while c.__contains__('y'):
            age = int(input('\nEnter another age: '))
            if 0 < age < 110:
                countPart += 1
                if 0 < age < 18:
                    countMinor += 1
                else:
                    countMajor += 1
                c = input('Do you want to continue(y/n)? ')[0].lower()
                confirm(c)
            else:
                print('\033[0:31mInvalid age\033[m')
        print(f'\nPeople: {countPart}')
        print(f'Major age: {countMajor}')
        print(f'Minors age: {countMinor}')
    else:
        print('\033[0:31mInvalid age\033[m')
except ValueError:
    print("\033[0:31mEnter what was ordered...\033[m")
