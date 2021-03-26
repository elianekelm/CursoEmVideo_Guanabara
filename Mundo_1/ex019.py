print('======== DESAFIO 019 ========')

import random

alunos = []
while len(alunos) < 4:
    nome_aluno = input('Nome do Aluno: ')
    alunos.append(nome_aluno)

# random.choice() faz uma escolha dentro da lista
print(f'O aluno escolhido para apagar o quadro foi: {random.choice(alunos).upper()}')

