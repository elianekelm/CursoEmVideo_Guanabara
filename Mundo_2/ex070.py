print("*" * 36)
print(f'{"LOJA DECENTRALAND".center(36)}')
print("*" * 36)
totalCompra = qtProdCaro = precoMenor = cont = 0
nomeProdMenor = ' '
listaCaro = []
while True:
    nomePrd = str(input("Nome do Produto: ")).strip()
    preco = float(input("Preço: R$ "))
    cont += 1
    totalCompra += preco
    if preco > 1000:
        qtProdCaro += 1
        listaCaro.append(nomePrd)
    if cont == 1 or preco < precoMenor:
        precoMenor = preco
        nomeProdMenor = nomePrd
    opcao = ' '
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        break
print(f'{" FIM DO PROGRAMA ":-^36}')
print(f"Total da compra: R$ {totalCompra:.2f}")
print(f"{qtProdCaro} produto(s) custando mais de R$ 1000.00", listaCaro)
print(f"Produto mais barato: {nomeProdMenor} (R$ {precoMenor:.2f}) ")
