
# ? Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt

n = int(input('Digite um número inteiro: '))
print('O dobro vale {}, o triplo é igual a {} e a raiz quadrada é igual a {:.2f}'.format(n*2, n*3, sqrt(n))) # * n**(1/2) também dá raiz.
