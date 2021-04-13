print(f'\033[1:33m{" DESAFIO 050 " :*^40}\033[m')
soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}º número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você digitou {cont} número(s) PAR(ES). \nA soma deles é: \033[1:34m{soma}')


