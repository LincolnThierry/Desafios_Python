# Fatorial de um numero qualquer
print('{:=^40}'.format('Fatorial'))
origem_n = int(input(print('Digite um número para calcular seu Fatorial: ')))
c = origem_n
f = 1
print('Calculando {}! = '.format(origem_n), end='')
while c > 0 :
    print('{}'  . format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))


