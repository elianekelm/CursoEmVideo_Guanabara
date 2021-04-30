print('\033[1:36m-' * 40)
print(f'{"Sequência de Fibonacci":^40}')
print('-\033[m' * 40)

qt_termos = int(input('Quantos termos você quer mostrar? '))
a1 = 0
a2 = 1
print('~' * 40)
print(f'{a1} ↠ {a2}', end='')
contador = 3 #porque já mostrei o 1ºe 2º termos
while contador <= qt_termos:
    a3 = a1 + a2
    print(f'↠ {a3} ', end='')
    a1 = a2
    a2 = a3
    contador += 1
print('↠ FIM')
