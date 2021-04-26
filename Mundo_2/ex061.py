print('\033[1m=' * 40)
print(f'    10 PRIMEIROS TERMOS DE UMA PA')
print('\033[1m=' * 40)

pri_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = pri_termo
cont = 1
while cont <= 10:
    print(f'\033[7:37m{termo}', end=' → ')
    termo = termo + razao
    cont += 1
print('END \033[m')
