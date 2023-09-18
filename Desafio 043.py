# Calculadora de IMC // Classificação
nome = str(input(print('Qual é o seu nome?')).strip())
peso = float(input(print('Qual é seu peso? (Kg) ')).strip())
altura = float(input(print('Qual é sua altura: (m) ')).strip())
IMC = (peso / altura ** 2)
print('O seu IMC {} é de {:.1f}'.format(nome, IMC))
if IMC < 18.5:
    print('Classificação: Abaixo do Peso')
elif 18.5 <= IMC < 25:
    print('Classificação: Peso Ideal')
elif 25 <= IMC < 30:
    print('Classificação: Sobrepeso')
elif IMC >= 40:
    print('Classificação: Obesidade Mórbida')
