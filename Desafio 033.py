# Calculo de um Salário com aumento

s = float(input(print('Qual é o Salário do Funcionário')).strip())

if s <= 1250:
    novo = s + (s * 15/100)
else:
    s > 1250
    novo = s + (s * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar agora R${:.2f}'.format(s, novo))

