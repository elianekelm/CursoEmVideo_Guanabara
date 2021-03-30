print('\033[33m-*-' * 5, 'DESAFIO 034', '-*-' * 5)

salario = float(input('\033[0mDigite o valor do salário atual: R$ '))
aumento = 0.10
if salario <= 1250:
    aumento = 0.15

print(f'Você terá um aumento de \033[1:31m{aumento * 100}%\033[0m (+{salario * aumento:.2f})')
print(f'Novo salário \033[1:34mR$ {(salario * aumento) + salario:.2f}\033[0m')
