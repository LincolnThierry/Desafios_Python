#Sorteio de Ordem de Apresentação

import random

a = str(input(print('Digite o nome do aluno')))
b = str(input(print('Digite o nome do aluno')))
c = str(input(print('Digite o nome do aluno')))
d = str(input(print('Digite o nome do aluno')))
alunos = [a,b,c,d]
x = random.sample(alunos,4)
print('A Ordem de Alunos sorteadas será')
print(x)
