#Calculo de Área de uma parede e a quantidade de tinta necessária para pintar

la=int(input(print('Qual é a Largura de sua parede')))
al=int(input(print('Qual é a Altura de sua parede')))
print('A sua parede possui {}m², para pinta-la serão necessários: {} litros de tinta'.format(la*al,((la*al))/2))