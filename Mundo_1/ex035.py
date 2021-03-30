print('\033[33m-*-' * 5, 'ANALISADOR DE TRIÂNGULOS', '-*-' * 5)

r1 = float(input('\033[0mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mSIM! Esses segmentos PODEM formar um triângulo!')
else:
    print('\033[31mNÃO! Esses segmentos NÃO PODEM formar um triângulo!')

# Cada segmento tem que ser menor que a soma dos outros dois segmentos