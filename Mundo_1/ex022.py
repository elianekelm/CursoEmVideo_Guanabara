print('======== DESAFIO 022 ========')

# strip() já vai remover todos os espaços em branco inúteis ...
# ... que foram colocados no início ou final
nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')

separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')
