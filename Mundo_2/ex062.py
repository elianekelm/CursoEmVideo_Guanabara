print('\033[1m=' * 40)
print(f'    SUPER PROGRESSÃO ARITMÉTICA')
print('\033[1m=' * 40)

a1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = a1  #variável 'termo' recebe o primeiro termo (a1)
cont = 1
total = 0
mais = 10 # inicia em 10 porque já foram exibidos 10 termos
while mais != 0: #quando o usuário digitar 0 o loop torna-se falso e encerra
    total += mais #total já começa valendo 10 + a quantidade que o usuário digitar
    while cont <= total:
        print(f'\033[7:37m{termo}', end=' → ')
        termo += razao
        cont += 1
    print('PAUSA \033[m')
    mais = int(input('Quantos termos a mais você quer mostrar: '))
print(f'PA finalizada com \033[1:34m{total} termos\033[m mostrados')
