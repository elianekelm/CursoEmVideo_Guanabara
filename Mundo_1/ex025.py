print('======== DESAFIO 025 ========')

adivinha1 = str(input('Qual a capital do Rio Grande do Sul? ')).strip()

if 'Porto Alegre' in adivinha1.title():
    print(f'Você acertou!')
else:
    print('Errado. Tente novamente!')


adivinha2 = str(input('\nO rato roeu a roupa do rei e...? ')).strip()
# strip() elimina todos os espaços em branco porventura digitados

print('Você digitou Rainha? {}'.format('rainha' in adivinha2.lower()))


