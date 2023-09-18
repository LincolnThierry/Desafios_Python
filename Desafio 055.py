# ANALISADOR DE PESO
# Dois Laços?
# Em peso o Valor Digitado será armazenado em uma outra variavel chamada armazenador que ira separar cada valor em ordenalos por ordem crescente
# Delimitar Qual é O Maior é necessário fazer o Laço correr entre todos os elementos e comparar atrave´s da subtração, Masw como eu posso fazer o laço correr e subtrair pelo elemento sucessor
# Entre os Intervalos os elementos precisão ser subtraidos
# Ultima tentativa é tentar dois for
from time import sleep
maior = 0
menor = 0
print('{:=^40}'.format('Ponderador de Massa Corporea', end=''))
for p in range(1, 6):
    peso = float(input(print('Peso da {}ª pessoa: '.format(p))))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    print('---Analisando Peso---')
sleep(1)
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))



