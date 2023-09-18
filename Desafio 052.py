# Número é primo ou não
# Pedi a Raiz Quadrada de I e se ela for equivalente a divisão de i/i ou seja a² == a/a
# Para um numero ser Primo ele precisa ter resto 0 e ser divisivel apenas por dois numeros ele mesmo e 1
# Se existir dois numeros que satisfaçam então print , I
núm = int(input(print('Digite um Número: ')))
tot = 0
for c in range(1,  núm, + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO Número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

