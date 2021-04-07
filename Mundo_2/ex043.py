print('\033[36m=-=' * 7, 'DESAFIO 043', '=-=' * 7)

peso = float(input('\033[mDigite seu peso (Kg): '))
altura = float(input('Digite sua altura(m): '))

imc = peso / (altura ** 2)
print(f'\033[1:34mSeu IMC: {imc:.1f}\033[m\nClassificação: ', end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('\033[1:31mOBESIDADE')
else:
    print('\033[1:31mOBESIDADE MÓRBIDA! Procure ajuda médica urgentemente!\033[m')

