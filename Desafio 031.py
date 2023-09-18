#Faça um Prgrama que mostre um ano Bissexto

a = int(input(print('Insira aqui o ano e veja se ele é bissexto')).title().strip())
b = a % 4
if b == 0:
    print('O ano {} é Bissexto'.format(a).title())
else:
    print('O ano {} não é Bissexto'.format(a).title())
