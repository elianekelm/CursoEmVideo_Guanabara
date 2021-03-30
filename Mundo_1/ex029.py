print('-*-' * 5, 'DESAFIO 029', '-*-' * 5)

from time import sleep
velocidade = float(input('\033[0mVelocidade do carro (km/h): '))
sleep(1)

if velocidade > 80:
    print(f'\033[1:31mMULTADO! - ultrapassar velocidade permitida (80 km/h).')
    print(f'\033[31mValor a pagar \033[1:33mR$ {(velocidade - 80) * 7:.2f}.')

print('\033[0:33mTenha um bom dia! Dirija com segurança!')