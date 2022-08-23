
#? Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

n = float(input('Digite um número real: '))
print('A parte inteira de {} é {}'.format(n, trunc(n))) #! Sem usar módulos: int(n) já funcionaria
