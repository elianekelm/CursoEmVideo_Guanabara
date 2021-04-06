print('\033[32m+=+ ' * 5, 'DESAFIO 041', '+=+ ' * 5)

from datetime import date
anoNasc = int(input('\033[mAno de Nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: \033[1:34mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[1:34mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[1:34mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[1:34mSÊNIOR\033[m')
else:
    print('Classificação: \033[1:34mMASTER\033[m')

