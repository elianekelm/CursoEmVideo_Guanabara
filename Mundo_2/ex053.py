print(f'{" DESAFIO 053 " :=^40}')

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split() #Separa as palavras da frase
junto = ''.join(palavras) #Vai juntar as palavras e uni-las sem o espaço
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('\033[1:34mEssa frase é um PALÍNDROMO!')
else:
    print('\033[1:31mEssa frase NÃO É UM PALÍNDROMO!')
    print('\033[1:33mExemplos de palíndromo:')
    print('→ Apos a sopa\n→ A sacada da casa\n→ A torre da derrota\n→ O lobo ama o bolo\n→ Anotaram a data da maratona')
