print(f'{" DESAFIO 064 " :*^40}')

num = int(input('Digite um número [999 para parar]: '))
soma = 0
contador = 0
while num != 999:
    soma = num + soma
    num = int(input('Digite um número [999 para parar]: '))
    contador += 1
    if num == 999:
        break
print(f'Qtdade números digitados: {contador}')
print(f'Soma entre eles: {soma}')
