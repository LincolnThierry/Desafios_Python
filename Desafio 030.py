#Preço da Passagem



k = int(input(print('Qual é a distância da sua viagem em Km?')).title().strip())
p = 0.50 * k
if k > 200:
    pm = 0.45 * k
    print('O preço total da sua passagem é: R${:.2f}'.format(pm))
else:
    print('O preço total da sua passagem é: R${:.2f}'.format(p))
