# Leitura de três segmentos de retas

r1 = int(input(print('Digite o numero para o comprimento do segmento de reta')).strip())
r2 = int(input(print('Digite o numero para o comprimento do segmento de reta')).strip())
r3 = int(input(print('Digite o numero para o comprimento do segmento de reta')).strip())

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')