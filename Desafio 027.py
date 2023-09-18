# Programa que pede para o Usuário adivinhar qual número o computador estava pensando

import random

n = str(input(print('Olá como você se chama?')).strip())
a = print('Como vai {}?,Espero que bem, Que tal testar seus dotes com adivinhação? Você não tem escolha =D'.format(n).title())
print('Estou Pensando em um numero entre 0 e 5'.title())
b = int(input(print('Em que numero estou pensando?')))
r = random.randint(0, 5)
if b == r:
    print('Você adivinhou parabéns!! Isso mesmo o numero que eu estava pensando era:{}'.format(b).title())
else:
    print('Você errou o número que eu estava pensando era:{}\nO computador venceu'.format(r))




