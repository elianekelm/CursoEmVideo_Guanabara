print('======== DESAFIO 015 ========')

qt_km = float(input('Quantidade de Km percorridos: '))
qt_dias = int(input('Quantidade de dias: '))

vlPagar = (qt_km * 0.15) + (qt_dias * 60)
print(f'Valor a pagar pelo aluguel do carro: R$ {vlPagar:.2f}')
