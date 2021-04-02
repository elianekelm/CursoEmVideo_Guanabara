print('\033[35m+=+ ' * 5, 'DESAFIO 039', '+=+ ' * 5)

from datetime import date
anoAtual = date.today().year
anoNasceu = int(input('\033[mEm que ano você nasceu? '))
idade = anoAtual - anoNasceu
print(f'Você completa {idade} anos nesse ano.')

if idade > 18:
    print(f'Seu ALISTAMENTO MILITAR foi em {anoNasceu + 18} (há {anoAtual - (anoNasceu + 18)} anos)')
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade < 18:
    print(f'Seu ALISTAMENTO MILITAR será em {anoNasceu + 18}')
    print(f'Ainda faltam {(anoNasceu + 18) - anoAtual} anos!')

