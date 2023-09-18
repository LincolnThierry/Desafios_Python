# Palavra contém no Inicio a Palavra 'SANTO'

# I forget of put the function .strip() in w variable
# The function 'find' doesn't was used. For this Example was used the 'Slicing' [:5], to find and give the result at binary
# The main strategy was delimited the character of string with slicing
# The correct way of do this Challenge are Slicing and putting the symbol of equal (==)

w = str(input(print('Enter a name of city')).strip())

print(w[:5].upper() == 'SANTO')
