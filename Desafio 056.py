# Banco de Dados de 4 pessoas
maioridadehomem = 0
médiaidade = 0
somaidade = 0
cont = 0
nomevelho = ''
print('{:=^10}'.format('Classificação de Peso e Idade', end=''))
for m in range(1, 5):
    print('----- {}ª PESSOA -----'.format(m))
    nome = str(input(print('Nome: ')).strip())
    idade = int(input(print('Idade: ')))
    sexo = str(input(print('Sexo [M/F]: ')).strip())
    somaidade += idade
    if m == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        cont += 1
médiaidade += somaidade / 4
print('=-' * 40)
print('\033[1;34mA Média de Idade do Grupo é \033[m: {}'.format(médiaidade))
print('=-' * 50)
print('O Homem mais Velho do Grupo é: {}, que possui {} anos.'.format(nomevelho, maioridadehomem).title())
print('A Quantidade de Mulheres que possuem idade menor do que 20 anos é quantabilizada por {} Mulheres'.format(cont).title())
print('=-' * 50)

