# Faça um programa que leia uma frase pelo teclado e mostre:

# Analyse of STR
# At function find has how to slicing strings Ex:: w.find('o',0,13)
# rfind

p = str(input(print('Type a phrase')).strip().upper())
print('Analysing the count of a repeated in your phrase...')
print('The number of times the character A appear is: {}'.format(p.count('A')))
print('The first position the character A appear was: {}'.format(p.find('A')+1))
print('The last position the character A appeared was: {}'.format(p.rfind('A')+1))
