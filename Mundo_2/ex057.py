print(f'{" VALIDAÇÃO DE DADOS ":+^40}')

sexo = str(input("Digite seu sexo [F/M]: ")).strip().upper()[0] #Pega só a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo \033[1:34m{sexo}\033[m registrado com sucesso.')
