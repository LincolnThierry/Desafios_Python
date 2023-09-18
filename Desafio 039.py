#Leitura de nascimento e informar a idade de um jovem

nascimento = int(input(print('Digite a data do ano de nascimento: ')).strip())
ano = int(input(print('Digite o ano atual')).strip())
idade = ano - nascimento
tempo = idade - 18

if idade == 18:
    print('\033[34mÉ hora de comparecer a Junta Militar mais proxima de sua região! Para o alistar ao Serviço Militar!!!\033[m')
elif idade < 18:
    print('\033[34mAinda irá se alistar ao serviço militar\n O prazo para o alistamento chegará daquia a \033[m\033[4;32m{} anos \033[m'.format(tempo))
elif idade > 18:
    print('\033[32mO Tempo para o alistamento militar já passou!!\033[m\n Já se passou \033[4;31m{} anos\033[m do Prazo para se alistar'.format(tempo))
