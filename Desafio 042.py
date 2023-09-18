#Formação de Triângulos e a designação de seus tipos
## Com Condição Aninhada/ Analisando Triângulos
r1 = float(input(print('Primeiro segmento:')).strip())
r2 = float(input(print('Segundo segmento: ')).strip())
r3 = float(input(print('Terceiro segmento: ')).strip())

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os segmentos acima Podem formar um triângulo ')
    if r1 == r2 == r3:
        print('\033[4;34mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[4;34mESCALENO!\033[m')
    else:
        print('\033[4;34mISÓCELES\033[m')
else:
    print('\033[1;31;40mOs segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO\033[m')