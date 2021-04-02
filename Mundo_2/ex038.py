print('\033[33m-- ' * 5, 'DESAFIO 038', '-- ' * 5)

numeros = []
x = 1
while x <= 3:
    num = int(input(f'\033[mDigite o {x}º número: '))
    numeros.append(num)
    x += 1
if numeros[0] == numeros[1] == numeros[2]:  # Se o índice 0 for igual o índice 1 e o índice 2
    print(f'\033[31mNão há MENOR ou MAIOR! Todos os valores são \033[4mIGUAIS!')
else:
    print(f'O \033[1:34mMENOR\033[m valor é: {min(numeros)}')
    print(f'O \033[1:34mMAIOR\033[m valor é: {max(numeros)}')