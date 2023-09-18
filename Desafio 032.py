#Leitor de numeros que identifica qual é o maior numero e qual é o menor numero

a = int(input(print('Insira o primeiro número para ser analisado sua ordem de valor')).title().strip())
b = int(input(print('Insira o segundo número para ser analisado segundo a ordem de valores digitados')).title().strip())
c = int(input(print('Digite o terceiro número para ser analisado junto aos três numeros digitados')).title().strip())
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))