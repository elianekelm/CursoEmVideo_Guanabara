print(f'\033[1:33m{" DESAFIO 054 " :+^40}\033[m')

from datetime import date
anoAtual = date.today().year
listaMenor = []
listaMaior = []
totmaior = 0
totmenor = 0
for i in range(1, 8):
    anoNasc = int(input(f'Em que ano a {i}ª pessoa nasceu: '))
    idade = anoAtual - anoNasc
    if idade <= 18:
        totmenor += 1
        listaMenor.append(idade)
    elif idade > 18:
        totmaior += 1
        listaMaior.append(idade)
print(f'Menores de idade: {totmenor} pessoas; \033[1:31mIdades: {listaMenor}\033[m')
print(f'Maiores de idade: {totmaior} pessoas; \033[1:31mIdades: {listaMaior}\033[m')

