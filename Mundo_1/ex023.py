print('======== DESAFIO 023 ========')

num = int(input('Digite um número entre 0 e 9999: '))

if num >= 1000 and num <= 9999:
    n = str(num)
    print(f'Unidade: {n[3]} \nDezena: {n[2]} \nCentena: {n[1]} \nMilhar: {n[0]}')
elif num >= 100 and num <= 999:
    n = str(num)
    print(f'Unidade: {n[2]} \nDezena: {n[1]} \nCentena: {n[0]}')
elif num >= 10 and num <= 99:
    n = str(num)
    print(f'Unidade: {n[1]} \nDezena: {n[0]}')
elif num < 10 and num >= 0:
    n = str(num)
    print(f'Unidade: {n[0]} \nEste número possui apenas unidade(s)!')
else:
    print('Número inválido! Por favor digite um número entre 0 e 9999.')





