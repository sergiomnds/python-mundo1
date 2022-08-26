
#? Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

#* MAIOR
maior = a
if b > a and b > c:
    maior = b
    
if c > b and c > a:
    maior = c

#* MENOR
menor = a
if b < a and b < c:
    menor = b
    
if c < b and c < a:
    menor = c

print('O maior número é {}'.format(maior))
print('O maior número é {}'.format(menor))