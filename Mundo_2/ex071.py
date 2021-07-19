print("*" * 36)
print(f'{"BANCO RARI".center(36)}')
print("*" * 36)
vl_saque = int(input("Que valor você deseja sacar? R$ "))
total = vl_saque
vlCed = 100
qtCed = 0
while True:
    if total >= vlCed:
        total -= vlCed
        qtCed += 1
    else:
        if qtCed > 0:
            print(f"Total de {qtCed} cédula(s) de R$ {vlCed}")
        if vlCed == 100:
            vlCed = 50
        elif vlCed == 50:
            vlCed = 20
        elif vlCed == 20:
            vlCed = 10
        elif vlCed == 10:
            vlCed = 5
        elif vlCed == 5:
            vlCed = 1
        qtCed = 0
        if total == 0:
            break
print("Volte sempre! Tenha um bom dia!")
