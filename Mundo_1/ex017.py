print('======== DESAFIO 017 ========')

from math import hypot
cat_oposto = float(input('Cateto Oposto: '))
cat_adj = float(input('Cateto Adjacente: '))

print(f'Hipotenusa = {hypot(cat_oposto, cat_adj):.2f}')


