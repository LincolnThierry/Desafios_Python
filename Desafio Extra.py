# Faixa Etaria de Sete Pessoas
import random
from datetime import date
from random import randint
tot = 0
maior = 0
for c in range(1, 8, + 1):
    i = random.randint(1980,2023)
    data = date.today().year
    idade = data - i
    if idade <= 18:
        tot += 1
    elif idade >= 18:
        maior += 1
print('No total {} pessoas da lista são ainda são \033[1mMenores de idade\033[m'.format(tot))
print('No total {} pessoas da lista já são \033[1mMaiores de idade\033[m'.format(maior))
