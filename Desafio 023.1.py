#Mostra os Numeros Sepados pela sua correpodência Unidacional Decimal Centenal e Milenar

# Method with int

n = int(input(print('Digite um numero qualquer')))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 100
m = n // 1000 % 1000
print('Analisando o numero {}'.format(n))
print('Unidade:{:}'.format(u))
print('Dezena:{:>2}'.format(d))
print('Centena:{:}'.format(c))
print('Milhar:{:>2}'.format(m))