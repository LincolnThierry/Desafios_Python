# Programa que pede para o Usuário adivinhar qual número o computador estava pensando
# Depois mostre a incidencia de numeros digitados em um grafico *****
from random import randint
from time import sleep
palpites = 0
print('{:🔢^40}'.format('GuessNumber.IO'))
n = str(input(print('\nInsira seu apelido: ')).strip())
print('Como vai {} 🪄\nVamos ver se você tem dotes com a adivinhação 🔮'.format(n))
print('🔮' * 12 )
print('  ___ Gerando Número ___')
print('🔮' * 12 )
print('\033[1;32m           Um\033[m')
sleep(1)
print('\033[1;33m           Dois\033[m')
sleep(1)
print('\033[1;34m           Três\033[m')
sleep(1)
# Importação de um dado girando ficaria legal
computador = randint(0, 10)
jogador = int(input(print('Número Gerado com sucesso!\nDigite o seu palpite, lembrando só valerá Números de 0 a 10:')))
acertou = False
while not acertou:
    jogador = int(input(print('Digite um numero entre [0 a 10]:')))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print('\033[1;36mAcertou com {} tentativas. Parabéns \033[m '.format(palpites))



