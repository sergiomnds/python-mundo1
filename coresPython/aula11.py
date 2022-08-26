print('\033[7;33;44mTESTE\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))

nome = 'Sérgio'
print('Olá! Prazer em te conhecer {}{}{}!'.format('\033[4;36m',nome,'\033[m'))

cores= {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'peb': '\033[7;30m'}
print('Uma {}coisa{}, outra {}coisa{}.'.format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))