#Progressão Aritmética v2.0
# Primeiro Termo e Razão aritmetica
# Como formatar cada linha de acordo com sua ordem de precedente
print('{:=^10}'.format('CALCULADORA DE PROGRESSÃO ARITMETICA (PA)', end =","))
cont = 0
a1 = int(input(print('Primeiro termo : ')))
R = int(input(print('Razão Aritmética: ')))
for c in range(1,11):
    PA = a1 + (c - 1) * R
    cont += 1
    print('\033[1m {}º Termo da Progressão Aritmetica é: {}\033[m'.format(cont, PA))
