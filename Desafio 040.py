# Calculadora de Média Escolar
# olhar resolução do 039
# Como colocar o sinal de entre
Nota_1 = float(input(print('Digite a média: ')).strip())
Nota_2 = float(input(print('Digite a média ')).strip())
Média = (Nota_1 + Nota_2) / 2
print('Média de: {:.2f}'.format(Média))
if Média < 5.0:
    print('\033[1;31mREPROVADO\033[m')
elif Média <= 5.0 <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
elif Média >= 7.0:
    print('\033[1;32mAPROVADO\033[m')
else:
    print('\033[31;40mDígito Invalido. O Valor Inserido Não é um Número Inteiro. Tente Novamente\033[m')
