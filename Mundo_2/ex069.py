qt_M = qt_F = qtMaiorIdade = qtMenor20Fem = 0
while True:
    print("\033[1:33m=" * 24)
    print(" CADASTRE UMA PESSOA ")
    print("=" * 24)
    nome = str(input("\033[mNome: ")).strip()
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if sexo == "M":
            qt_M += 1
        else:
            qt_F += 1
    if idade >= 18:
        qtMaiorIdade += 1
    elif idade <= 20 and sexo == "F":
        qtMenor20Fem += 1
    print("-" * 24)
    opcao = str(input("Quer continuar: [S/N] ")).strip().upper()[0]
    if opcao == "N":
        break
print("=" * 24)
print(f"Total de pessoas com mais de 18 anos: {qtMaiorIdade}")
print(f"Total de homens cadastrados: {qt_M}")
print(f"Temos {qtMenor20Fem} mulher(es) com menos de 20 anos.")
