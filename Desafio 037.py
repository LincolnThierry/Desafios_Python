# Escreva um programa que leia um número inteiro e converta para a base de conversão que o usuário escolher

### A Estrutura com aspas triplas me deixou confuso não sei o uso delas, além da parte em que ele faz a variavel opção
## A opção servirá como um armazenador de digitos
# Tente sempre simplificar, não deixe o código grande
# o uso do else geralmente esta associado a uma opção não contida na estrutura em tese que leva aparecer erros ou opção invalida dependendo da estrutura de criação do programa tudo basta a ser coordenado assim pensnado em todos os casos

num = int(input(print('Digite um número inteiro: ')).strip())
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igaul a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mOpção Inválida\033[m. \033[4;32mTente novamente.\033[m')
