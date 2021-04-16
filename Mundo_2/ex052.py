print(f'\033[1:35m{" DESAFIO 052 " :⩋^36}\033[m')

totalDiv = 0
num = int(input('Digite um número inteiro: '))
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[1:34m', end=' ')
        totalDiv += 1
    else:
        print('\033[1:31m', end=' ')
    print(i, end=' ')
print(f'\n\033[mO número {num} foi divisível {totalDiv} vezes.')
if totalDiv == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

