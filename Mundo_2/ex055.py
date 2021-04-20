print(f'\033[1:36m{" DESAFIO 055 " :+^40}\033[m')

listaPeso = []
for i in range(1, 6):
    listaPeso.append(float(input(f'Peso da {i}ª pessoa: ')))
print(f'Maior peso: {max(listaPeso)} kg')
print(f'Menor peso: {min(listaPeso)} kg')
print(f'A diferença entre eles é de {max(listaPeso) - min(listaPeso)} kg')
