print('\033[34m# - ' * 5, 'DESAFIO 036', '- # ' * 5)

vl_casa = float(input('\033[mValor do imóvel: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))

margem_financ = salario * 0.3
parcela = vl_casa / (anos * 12)
if parcela > salario * 0.3:
    print('\033[1:31mEMPRÉSTIMO NEGADO!\033[m')
    print(f'Para pagar esse imóvel de R$ {vl_casa:.2f} em {anos} anos o valor da parcela mensal será  R$ {parcela:.2f}')
    print(f'Limite máximo da parcela que o cliente consegue pagar \033[4mR$ {margem_financ:.2f}\033[m (30% da renda)')
else:
    print('\033[1:34mEMPRÉSTIMO CONCEDIDO!\033[m')
    print(f'Valor da parcela mensal R$ {parcela:.2f} ({parcela * 100 / salario:.2f}% da renda)')
