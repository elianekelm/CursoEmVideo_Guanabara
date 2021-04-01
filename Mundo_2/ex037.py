print('\033[36m# - ' * 5, 'DESAFIO 037', '- # ' * 5)

num = int(input('\033[mDigite um número inteiro: '))
print('Escolha uma das bases para Conversão: ')
print('1 - converter para BINÁRIO \n2 - converter para OCTAL \n3 - converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} em BINÁRIO é igual: {bin(num)[2:]}')  # 0b = binário
elif opcao == 2:
    print(f'{num} em OCTAL é igual: {oct(num)[2:]}')  # 0o = octal
elif opcao == 3:
    print(f'{num} em HEXADECIMAL é igual: {hex(num)[2:]}')  # 0x = hexadecimal
else:
    print('Operação Inválida! Você deve escolher entre 1/2/3')



