print('======== DESAFIO 027 ========')

nome = str(input('Digite seu nome completo: ')).strip().split()
# split() gera uma lista com toda a cadeia - cada palavra recebe uma indexação
print(f'Prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0].title()}')
print(f'Seu último nome é {nome[-1].title()}')
