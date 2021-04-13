print(f'\033[1:34m{" DESAFIO 046 " :=^40}\033[m')
print('CONTAGEM REGRESSIVA...')
from time import sleep
for i in range(10, -1, -1):
    print(f'\033[1:33m{i}')
    sleep(0.5)
print('\033[1:31mBUM, BUM, POOWW!!!!')
