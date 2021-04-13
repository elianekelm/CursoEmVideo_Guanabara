print(f'\033[1:35m{" DESAFIO 048 " :*^40}\033[m')

soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num  # Acumulador --> vai acumulando os valores
        cont += 1    #Contador --> conta dentro do loop

print(f'A soma dos {cont} valores ímpares múltiplos de 3 (até 500) é \033[1:31m{soma}')