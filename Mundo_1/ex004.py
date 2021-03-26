print('======= DESAFIO 004 =======')

tipo_primitivo = input('Digite alguma coisa: ')
print(f'O tipo primitivo desse valor é {type(tipo_primitivo)}')
print(f'Só tem espaços: {tipo_primitivo.isspace()}')
print(f'É um número: {tipo_primitivo.isnumeric()}')
print(f'É alfabético: {tipo_primitivo.isalpha()}')
print(f'É alfanumérico: {tipo_primitivo.isalnum()}')
print(f'Está em maiúsculo: {tipo_primitivo.isupper()}')
print(f'Está em minúsculo: {tipo_primitivo.islower()}')
print(f'Está capitalizada: {tipo_primitivo.istitle()}')


