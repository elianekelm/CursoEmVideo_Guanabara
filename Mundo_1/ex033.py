print('\033[33m-*-' * 5, 'DESAFIO 033', '-*-' * 5, '\033[0m')

numeros = []
x = 1
while x <= 3:
    num = int(input(f'Digite o {x}º número: '))
    numeros.append(num)
    x += 1
if numeros[0] == numeros[1] == numeros[2]:  # Se o índice 0 for igual o índice 1 e o índice 2
    print(f'\033[31mNão há MENOR ou MAIOR! Todos os valores são IGUAIS!')
else:
    print(f'\033[34mO MENOR valor é: {min(numeros)}')
    print(f'O MAIOR valor é: {max(numeros)}')
