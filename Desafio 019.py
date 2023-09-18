#Sorteio de Alunos

import random

a = str(input(print('Digite o nome do aluno')))
b = str(input(print('Digite o nome do aluno')))
c = str(input(print('Digite o nome do aluno')))
d = str(input(print('Digite o nome do aluno')))
alunos = [a,b,c,d]
x = random.choice(alunos)
print("O aluno sorteado foi: {}".format(x))
