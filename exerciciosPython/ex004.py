n = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(n))

print('Só tem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabético', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
# * Se tem a primeira letra maiúscula
print('Está capitalizada? ', n.istitle())

# ? Usando o format
print('{} só tem espaços? '.format(n), n.isspace())
