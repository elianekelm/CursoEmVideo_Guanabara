print('\033[33m-*-' * 5, 'ANALISADOR DE TRIÂNGULOS v.2.0', '-*-' * 5)

r1 = float(input('\033[0mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mEsses segmentos PODEM formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('\033[1:34mEQUILÁTERO\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[1:34mISÓSCELES\033[m')
    else:
        print('\033[1:34mESCALENO\033[m')
else:
    print('\033[31mEsses segmentos NÃO PODEM formar um triângulo!')

# Para formar um triângulo --> Cada segmento tem que ser menor que a soma dos outros dois segmentos