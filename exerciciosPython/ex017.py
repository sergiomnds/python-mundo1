from math import sqrt, hypot
#? Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#? Calcule e mostre o comprimento da hipotenusa.
c1 = float(input('Informe o valor do cateto oposto: '))
c2 = float(input('Informe o valor do cateto adjacente: '))
h = sqrt(c1**2 + c2**2)
hi = hypot(c1, c2) #* Usando o math.hypot
print('A hipotenusa é igual a: {:.1f}'.format(h))
print('A hipotenusa é igual a: {:.1f}'.format(hi))
