# Média Escolar


nome= str(input(print('Digite seu Nome')).strip())
m= str(input(print('Digite a Materia Escolhida')))
s1= int(input(print('{:} Coloque sua Nota do Primeiro Semestre'.format(nome))))
s2= int(input(print('{:} Coloque sua Nota do Segunda Semestre'.format(nome))))
media = (s1+s2)/2
print('\033[4;34m{}\033[m Sua \033[1mMédia\033[m Na Matéria\033[m de \033[1;36;40m{}\033[m'.format(nome,m))
if media >= 6:
    print('Foi De \033[1;32m{}\033[m'.format(media))
    print('Parabéns Você Foi \033[1;32mAprovado!!!\033[m')
else:
    print('Foi de \033[1;31m{}\033[m'.format(media))
    print('Infelizmente Você Foi \033[1;31mReprovado\033[m Na Matéria de \033[1;36;40m{}\033[m Recomendo que você Estude mais!!'.format(m))