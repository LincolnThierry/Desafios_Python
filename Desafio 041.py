# Indicador de Categoria por Faixa Etaria
# Classificação de Atletas

from datetime import date
atual = date.today().year
Nascimento = int(input(print('Digite o ano de nascimento: ')).strip())
data = atual - Nascimento
print('O Atleta possui {} anos. A sua catégoria de acordo com sua faixa etária se enquadra ao:  '.format(data))
if data <= 9:
    print('Classificação: MIRIM')
elif data <= 14:
    print('Classificação: INFANTIL')
elif data <= 20:
    print('Classificação: JUNIOR')
elif data <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
