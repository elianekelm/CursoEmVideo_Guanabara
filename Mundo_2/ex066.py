print(f'\033[1:34m{" DESAFIO 066 ":*^40}\033[m')

lista = []
while True:
    num = int(input("Digite um número [ou '999' para SAIR]: "))
    if num == 999:
        break
    lista.append(num)
print(f"Quantidade de valores digitados: {len(lista)}")
print(f'Soma total: {sum(lista)}')
