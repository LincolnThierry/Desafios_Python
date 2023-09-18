# Faixa Etaria de Sete Pessoas
from datetime import date
totmenor = 0
totmaior = 0
for c in range(1, 8):
    i = int(input(print('Em que ano que a {}ª pessoa nasceu: '.format(c))))
    data = date.today().year
    idade = data - i
    if idade <= 18:
        totmenor += 1
    elif idade >= 18:
        totmaior += 1
print('No total {} pessoas da lista ainda são \033[1mMenores de idade\033[m'.format(totmenor))
print('No total {} pessoas da lista já são \033[1mMaiores de idade\033[m'.format(totmaior))
