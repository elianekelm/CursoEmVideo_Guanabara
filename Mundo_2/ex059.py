print(f'{" MENU DE OPÇÕES ":=^40}')

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
sair = False
while not sair:
    print('\033[1m=' * 40)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? \033[m'))
    if opcao == 1:
        print(f'\033[1:36mO resultado de {num1} + {num2} = {num1 + num2}\033[m')
    elif opcao == 2:
        print(f'\033[1:34mO resultado de {num1} * {num2} = {num1 * num2}\033[m')
    elif opcao == 3:
        if num1 == num2:
            print('\033[1:35mOs números são iguais!\033[m')
        else:
            print(f'\033[1:35mEntre {num1} e {num2} o maior valor é {max(num1, num2)}\033[m')
    elif opcao == 4:
        num1 = int(input('\033[mPrimeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\033[1:31mBye!\033[m')
        break
    else:
        print('\033[1:31mOpção Inválida! Tente novamente\033[m')
