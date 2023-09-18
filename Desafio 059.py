from time import sleep as slp
valor_1 = int(input(print('1ª valor:')))
valor_2 = int(input(print('2ª valor: ')))
operador = 0
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
# Se existe um valor limitante de funções facilita o uso do while, caso seja um número indeterminado use o False ou True
while operador != 5:
    operador = int(input('>>>>>>>>>>Qual é a sua opção:'))
    if operador == 1:
        print('soma: {}'.format(valor_1 + valor_2))
        slp(1)
    elif operador == 2:
        print('multiplicação {}'.format(valor_1 * valor_2))
        slp(1)
    elif operador == 3:
        if valor_1 > valor_2:
            maior = valor_1
            slp(1)
        else:
            maior = valor_2
        print('O Maior valor é: {} dentre os valores [{},{}] '.format(maior, valor_1, valor_2))
        slp(1)
    elif operador == 4:
        print('Informe os números novamente:')
        valor_1 = int(input(print('1ª valor:')))
        valor_2 = int(input(print('2ª valor:')))
        slp(1)
    elif operador == 5:
        print('Finalizando...')
        slp(1)
    else:
        print('Opção inválida, Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')