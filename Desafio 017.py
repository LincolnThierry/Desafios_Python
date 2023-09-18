#Calculadora de Seno, Cosseno e Tangente
from math import hypot
from math import cos
from math import sin

x = int(input(print('Digite um Número para o Lado Horizontal de um Triangulo (Cateto Adjacente (X)):')))
y = int(input(print('Digite um Número para o Lado Vertical de um Triangulo (Cateto Oposto(y)):')))
ß = int(input(print('Digite um Número para ser o Ângulo do Circulo Trigonometrico')))
print('O Cateto Oposto (y), vale: {}, possui como Seno o valor: {:.2f} \n O Cateto Adjacente (x), vale {}, possui como Cosseno o valor : {:.2f} \n  O Triângulo de lados {} e {} (respectivamente x e y) Tem como Hipotenusa o valor de: {:.2f}'.format(x,sin(ß),y,cos(ß),x,y,hypot(x,y)))
