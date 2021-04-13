print(f'\033[1:34m{" DESAFIO 049 " :*^40}\033[m')

num = int(input('Você deseja a tabuada de qual número: '))
for i in range(1, 11):
    print(f'{num} * {i} = {num * i}')

