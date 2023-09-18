# Numero Sucessor e Antecessor

import random

n=int(input(print('Digite um numero')))

# r = cores.random.choices()
cores = {'azul':'\033[4;34m',
        'vermelho':'\033[4;31m',
         'roxo':'\033[4;35m' }
print('O Número que você digitou foi {}{}{}\n O seu Sucessor é {}{}{}\n O seu Antecessor é {}{}{}'.format(cores['azul'], n,'\033[m', cores['vermelho'],  n+1,'\033[m' ,cores['roxo'], n-1, '\033[m'))