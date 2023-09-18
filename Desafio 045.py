# Crie um Programa Que faça o computador jogar jokenpô com você.
# Esta Dando Erro Nos Resultados
from random import randint
from time import sleep
print('{:=^40}'.format('JO-KEN-PÔ!'))
# Sorteio Dos Elementos
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Para Jogar Basta Digitar o número correspondido ao elemento desejado!')
jogador = int(input(print(''' Faça a sua Escolha 

🪨   Pedra  \033[1;34m [ 0 ] \033[m
🤚🏻   Papel   \033[1;32m[ 1 ] \033[m
✂️   Tesoura \033[1;33m[ 2 ] \033[m                ''')))

print('     JO')
sleep(1)
print('     KEN')
sleep(1)
print('     PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # Computador Jogou Pedra
        if jogador == 0:
                print('🪨 x 🪨 = 🪨')
                print('\n\n\033[1;33mEMPATE\033[m')
        elif jogador == 1:
                print('   🪨 x 🤚🏻 = 🤚🏻\n\n\n\033[1;32m   Você Venceu!!\033[m')
        elif jogador == 2:
                print('   🪨 x ✂️ = 🪨\n\n\n\033[1;31m   Você Perdeu!!\033[m')
        else:
                print('\033[4;31mJOGADA INVALIDA\033[m')

elif computador == 1: # Computador Jogou Papel
        if jogador == 0:
                print('   🤚🏻 x 🪨 = 🤚🏻\n\n\n\033[1;31m   Você Perdeu!\033[m')
        elif jogador == 1:
                print('   🤚🏻 x 🤚🏻 = 🤚🏻\n\n\033[1;33mEMPATE\033[m')
        elif jogador == 2:
                print('   🤚🏻 x ✂️ = ✂️\n\n\n\033[1;32m  Você Venceu!!\033[m')
        else:
                print('\033[4;31mJOGADA INVALIDA\033[m')

elif computador == 2: # Computador Jogou Tesoura
        if jogador == 0:
                print('   ✂️ x 🪨 = 🪨\n\n\n\033[1;32m  Você Venceu!!\033[m')
        elif jogador == 1:
                print('   ✂️ x 🤚🏻 = ✂️\n\n\n\033[1;31m  Você Perdeu!\033[m')
        elif jogador == 2:
                print('   ✂️ x ✂️ = ✂️\n\n\033[1;33mEMPATE\033[m')
        else:
                print('\033[4;31mJOGADA INVALIDA\033[m')
