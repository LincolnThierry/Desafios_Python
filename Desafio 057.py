sexo = str(input(print('Informe seu sexo: [M/F] ')).upper())[0]
while sexo not in 'MmFf':
    sexo = str(input(print('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper())[0]
print('Sexo {} registrado com sucesso'.format(sexo))