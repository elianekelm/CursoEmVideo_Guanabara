print('-*-' * 5, 'DESAFIO 031', '-*-' * 5)

print(f'\033[1:31mPROMOÇÃO DO MÊS: \n\033[0:33mR$ 0.50 por km - viagens de até 200Km \nR$ 0.45 por km - viagens mais longas\033[0m')
distancia = float(input('Qual a distância da sua viagem: '))

preco = 0.45
if distancia <= 200:
    preco = 0.50
print(f'Preço da passagem \033[1:34mR$ {distancia * preco:.2f} \033[0m\nVocê aproveitou o desconto de R$ {preco} por km')