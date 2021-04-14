print('\033[1m=' * 40)
print(f'    10 PRIMEIROS TERMOS DE UMA PA')
print('\033[1m=' * 40)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for i in range(1, 11):
    print(f'\033[7:37m{termo}', end=' → ')
    termo += razao
print('END \033[m')
