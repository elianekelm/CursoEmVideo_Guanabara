print(f'\033[1:35m{" DESAFIO 065 " :+^40}')

sair = False
contador = soma = 0
lista = []
while sair != True:
    num = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    contador += 1
    soma = soma + num
    lista.append(num)
    if opcao == 'S':
        continue
    else:
        sair = True
print(f'\033[1:33mQtdade de números digitados: {contador}')
print(f'Média {soma/contador:.2f}')
print(f'Maior valor: {max(lista)}')
print(f'Menor valor: {min(lista)}')
