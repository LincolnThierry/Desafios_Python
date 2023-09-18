#Condições Aninhadas
#Olhar as outras possibilitades ver as outras possibilidades

home = float(input(print('Valor da casa: R$')).strip())
salary = float(input(print('Salário do comprador: R$')).strip())
years = int(input(print('Quantos anos de financiamento?')).strip())
provision = home / (years * 12)
minimo = salary * 30 /100
print('Para pagar uma casa de R${:.2f} em anos {}'.format(home,years))
print('\033[1;34;49mA prestação será de R${:.2f}\033[m'.format(provision))
if provision <= minimo:
    print('\033[1;32m Empréstimo pode ser CONCEDIDO!\033[m\n')
else:
    print('\033[4;31m \033[m\n\033[1;31;40m ---Emprestimo NEGADO---\033[m')