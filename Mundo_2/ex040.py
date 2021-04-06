print('\033[33m+=+ ' * 5, 'DESAFIO 040', '+=+ ' * 5)

nota1 = float(input('\033[mDigite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

media = (nota1 + nota2) / 2
print(f'Média Final: {media}')

if media < 5:
    print(f'\033[1:31mSituação: REPROVADO\033[m')
elif media >= 5 and media < 7:
    print('\033[1:33mSituação: EM RECUPERAÇÃO \033[m')
elif media >= 7:
    print('\033[1:34mSituação: APROVADO\033[m')

