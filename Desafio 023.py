#Mostra os Numeros Sepados pela sua correpodência Unidacional Decimal Centenal e Milenar

# Method with str, just work with four digits
n = str(input(print('Digite um numero qualquer')))
nr = n.replace('',' ')
ns = nr.split()
print('Unidade:{:}\nDezena:{:>2}\nCentena:{:}\nMilhar:{:>2}\n'.format(ns[0],ns[1],ns[2],ns[3]))
