print('======== DESAFIO 020 ========')

from random import shuffle

alunos = []
x = 1
while x < 5:
    nome_aluno = input(f'Nome do {x}º Aluno: ')
    alunos.append(nome_aluno)
    x += 1

# shuffle() embaralha os elementos de uma lista
shuffle(alunos)
print(f'Ordem sorteada: {alunos}')