print(f'\033[1:33m{" JOGO DA ADIVINHAÇÃO ":=^40}')

from random import randint
computador = randint(0, 10)
print('\033[mSou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar? ')
tentativa = 1
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    if jogador == computador:
        print(f'\033[1mParabéns! Acertou na {tentativa}ª tentativa.\033[m')
        acertou = True
    elif computador < jogador:
        print('\033[31mMenos...Tente mais uma vez!\033[m')
        tentativa += 1
    elif computador > jogador:
        print('\033[34mMais...Tente mais uma vez!\033[m')
        tentativa += 1
