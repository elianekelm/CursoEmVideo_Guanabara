print(f'{" DESAFIO 056 " :*^40}')

listaMaiorIdade = []
somaIdade = 0
nomeMaisVelho = 0
idadeMaisVelho = 0
qtMulheres = 0
for i in range(1, 5):
    print(f'\033[1:34m----- {i}ª PESSOA -----\033[m')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    somaIdade += idade  # variável que soma as idades
    listaMaiorIdade.append(idade)  # armazena as idades em uma lista
    sexo = str(input('Sexo [M/F]: ')).strip()
    if i == 1 and sexo in 'Mm':
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > idadeMaisVelho: # Faz uma nova verificação
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        qtMulheres += 1
print(f'O homem mais velho ({nomeMaisVelho}) tem {idadeMaisVelho} anos')
print(f'Média das idades do grupo: {somaIdade/4}')
print(f'Total de mulher(es) com menos de 20 anos: {qtMulheres}')
