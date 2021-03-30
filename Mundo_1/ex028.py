#print('======== DESAFIO 028 ========')

from random import randint
computador = randint(0,5)  #Faz o computador "pensar"

print('\033[1:33m-=-' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[1:33m-=-' * 20)
print('Você pode tentar 3 vezes!')

a = 2
x = 0
while x <= 2:
    jogador = int(input('\033[0mEm que número eu pensei? '))
    print(f'\033[35mVocê tem {a} tentativas')

    if jogador == computador:
        print('\033[1:33mPARABÉNS! Você conseguiu me vencer! \nEND')
        break
    else:
        print(f'\033[1:33mGANHEI! eu pensei no número {computador} e não no {jogador}')

    x += 1
    a -= 1

