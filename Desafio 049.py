# Tabuada 📊
a = '|'
print('{:=^40}'.format('TABUADA'))
num = int(input(print('Digite um número para ver sua tabuada: ')))
for c in range (1, 11):
    print('{} {:2}  x {:2} = {} {:>24}'.format(a, num, c, num*c, a))



