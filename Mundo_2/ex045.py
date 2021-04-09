print(f'\033[1:33m{" DESAFIO 045 " :=^40}\033[m')

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opções: ')
print('[0] PEDRA \n[1] PAPEL \n[2] TESOURA')
jogador = int(input('Qual você escolhe? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('\033[1:34m-=' * 14)
print(f'\033[1:33mComputador escolheu {itens[computador]}')
print(f'Jogador escolheu {itens[jogador]}')
print('\033[1:34m-=' * 14)

if computador == 0:   #pedra
    if jogador == 0: #pedra (EMPATE)
        print('\033[1:31mEMPATE')
    elif jogador == 1: #pedra x papel (GANHA PEDRA)
        print('\033[1:31mJOGADOR VENCE')
    elif jogador == 2: #pedra x tesoura (GANHA TESOURA)
        print('\033[1:31mCOMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #papel
    if jogador == 0: #pedra
        print('\033[1:31mCOMPUTADOR VENCE')
    elif jogador == 1: #papel
        print('\033[1:31mEMPATE')
    elif jogador == 2: #tesoura
        print('\033[1:31mJOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #tesoura
    if jogador == 0: #PEDRA
        print('\033[1:31mJOGADOR VENCE')
    elif jogador == 1: #PAPEL
        print('\033[1:31mCOMPUTADOR VENCE')
    elif jogador == 2: #TESOURA
        print('\033[1:31mEMPATE')
    else:
        print('JOGADA INVÁLIDA!')
