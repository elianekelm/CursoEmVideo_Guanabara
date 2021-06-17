print(f'\033[1:34m{" TABUADA ":*^30}\033[m')

while True:
    num = int(input('Tabuada do número: '))
    print('-' * 30)
    if num < 0:
        print('Sem resposta para valores negativos.')
        break
    for i in range(1, 11):
        print(f'{num} * {i} = {i*num}')
    print('-' * 30)
print('END. Volte sempre!')
