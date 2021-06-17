print('=-=' * 12)
print('\033[1:36m Vamos jogar PAR ou ÍMPAR!!!\033[m')
print('=-=' * 12)
from random import randint
qt_venceu = 0
while True:
    num = int(input('Digite um valor: '))
    computador = randint(0, 10)
    res = num + computador
    condicao = ' '
    print('-' * 36)
    while condicao not in 'PI':
        condicao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {num} e o cumputador {computador}')
    print(f'Total: {res} --> deu PAR' if res % 2 == 0 else f'Total: {res} --> deu ÍMPAR')
    if res % 2 == 0:
        if condicao == "P":
            print("Você VENCEU!")
            qt_venceu += 1
        else:
            print("Você PERDEU!")
            break
    else:
        if condicao == "I":
            print("Você VENCEU!")
            qt_venceu += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
    print('-' * 36)
print('=-=' * 12)
print(f"\033[1:31mGAME OVER! Você venceu {qt_venceu} vez(es).")
