print(f'\033[1:36m{" LOJAS ELIANE ":=^42}')

vl_compra = float(input('\033[mValor total da compra: R$ '))
print('FORMAS DE PAGAMENTO')
print('\033[1m[1]\033[m à vista Dinheiro/Cheque')
print('\033[1m[2]\033[m à vista Cartão')
print('\033[1m[3]\033[m 2x no Cartão')
print('\033[1m[4]\033[m 3x ou mais no Cartão')
opcao = int(input('Opção desejada (1/2/3/4): '))
print('==' * 21)
if opcao == 1:
    vl_pgto = vl_compra * 0.9
    print(f'Valor a Pagar \033[1:31mR$ {vl_pgto:.2f}\033[m\nDesconto Obtido R$ {vl_compra - vl_pgto:.2f}')
elif opcao == 2:
    vl_pgto = vl_compra * 0.95
    print(f'Valor a Pagar \033[1:31mR$ {vl_pgto:.2f}\033[m\nDesconto Obtido R$ {vl_compra - vl_pgto:.2f}')
elif opcao == 3:
    vl_pgto = vl_compra
    print(f'Valor a Pagar \033[1:31mR$ {vl_pgto:.2f}\033[m\n2x SEM JUROS de R$ {vl_pgto / 2:.2f}')
elif opcao == 4:
    vl_pgto = vl_compra * 1.2
    qt_parcelas = int(input('Quantidade de parcelas: '))
    if qt_parcelas >= 3:
        print(f'Valor a Pagar \033[1:31mR$ {vl_pgto:.2f}\033[m\nJUROS INCLUSOS R$ {vl_pgto - vl_compra:.2f}')
        print(f'{qt_parcelas}x de R$ {vl_pgto / qt_parcelas:.2f}')
    else:
        print('Opção Inválida! Escolha outra forma de pagamento.')
else:
    print('Opção Inválida! Tente novamente.')



