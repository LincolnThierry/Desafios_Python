# Crie uma frase qualquer e verifique se ela é um palindromo
# Desconsidere os espaços

frase = str(input(print('Digite sua frase: ')).strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)