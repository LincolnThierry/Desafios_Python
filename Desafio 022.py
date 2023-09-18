# Manipulating Text

name= str(input(print("Digite seu Nome Completo"))).strip()
print('Analisando seu nome...')
split = name.split()
print(name.upper())
print(name.lower())

# count of letters of a name without spacebar

print('O Seu nome tem ao todo : {} '.format((len(name.replace(' ', '')))))

# in the way of teacher was that: print('...'.format(len(nome) - nome.count(' ')))
# append (-) | * - nome.count - * |

print('Seu primeiro nome é :{}'.format(split[0]))

print('Seu primeiro nome tem {} letras'.format(len(split[0])))

# in the way of teacher was: print('...'.format(nome.find(' ')))
# the spacebar between ('_'), set the first place of array