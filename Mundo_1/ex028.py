#print('======== DESAFIO 028 ========')

from random import randint
from time import sleep

print('\033[1:33m-=-' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[1:33m-=-' * 20)
print('\033[0mPROCESSANDO...')
sleep(2)
print('Você pode tentar 3 vezes!')

computador = randint(0, 5)  # Faz o computador "pensar"
a = 2
x = 0
while x <= 2:
    jogador = int(input('\033[1:0mEm que número eu pensei? '))
    print(f'\033[35mVocê tem {a} tentativas')

    if jogador == computador:
        print('\033[1:34mPARABÉNS! Você conseguiu me vencer! \nEND')
        break
    else:
        print(f'\033[0mGANHEI! eu pensei em outro número e não no {jogador}')
        if a == 0:
            print(f'\033[31mGAME OVER. Eu tinha pensado no número {computador}!')
    x += 1
    a -= 1

