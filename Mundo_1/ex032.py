print('-*-' * 5, 'DESAFIO 032', '-*-' * 5)

from datetime import date
ano = int(input('Qual ano você quer verificar? (Digite 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[34mO ano {ano} é BISSEXTO!')
else:
    print((f'\033[31mO ano {ano} NÃO é BISSEXTO!'))