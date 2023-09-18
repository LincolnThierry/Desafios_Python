# Como trabalhar com cores no terminal
nome = 'Lincoln'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
        'amarelo':'\033[33m',
         'pretoevermelho':'\033[7;31;40m'}

print('Olá! Muito prazer em te conhecer,{}{}{}!!'.format(cores['pretoevermelho'], nome, cores['pretoevermelho']))