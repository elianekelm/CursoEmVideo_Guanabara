print('-*-' * 5, 'DESAFIO 030', '-*-' * 5)

num = int(input('\033[36mDigite um número inteiro: '))

if num % 2 == 0:
    print(f'\033[0mO número {num} é \033[1:34mPAR!')
else:
    print(f'\033[0mO número {num} é \033[1:34mÍMPAR!')