#Desafio 044
# Gerenciador de Pagamento

print('{:=^40}'.format('Lojas Amarit'))
p = float(input(print('Preço das compras: R$')))
dinheiro_cheque = p - (p * 10/100)
vista = p - (p * 5/100)
forma_de_pagamento = int(input(print('''
\033[1;32mForma de Pagamento:\033[m

Dinheiro/Cheque [ 1 ]
Cartão [ 2 ]
''')))
if forma_de_pagamento == 1:
    print('Pagamento Dinheiro/Cheque : R${}'.format(dinheiro_cheque))
elif forma_de_pagamento == 2:
    cartão = int(input(print('''\033[1;34mForma de Pagamento no Cartão:\033[m
    
À vista [ 1 ]
Parcelado em 2x [ 2 ]
Parcelado em 3x ou mais [ 3 ]''')))
    if cartão == 1:
        print('Pagamento À vista: R${:.2f}'.format(vista))
    elif cartão == 2:
        print('\n\nPagamento parcelado em duas vezes no cartão em parcelas de: R${:.2f} '.format(p/2))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.\n\n\n\033[4mSem cobrança de Juros\033[m'.format(p, p))
    elif cartão == 3:
        t = int(input(print('''\033[1;34mDigite a Quantidade de Vezes Parceladas:\033[m
        
\033[1;33m[ 3 ]\033[m
\033[1;33m[ 4 ]\033[m
\033[1:33m[ 5 ] \033[m
  . 
  .
  .
\033[1;39m[ 12 ]\033[m''')))
        parcelamento = (p + (p * 20/100))
        pt = parcelamento / t
        print('\033[4mSua Compra de R${} será cobrada uma tarifa de juros.\nO valor cobrado COM JUROS vai ser: R${:.2f}\n\nNo total o parcelamento de {}x no cartão será de :R${:.2f}\033[m'.format(p, parcelamento, t, pt))



