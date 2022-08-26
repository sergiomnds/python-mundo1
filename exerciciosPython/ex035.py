
#? Desenvolva um programa que leia o comprimento de três retas
#? e diga ao usuário se elas podem ou não formar um triângulo.
a = int(input('Escreva o valor da 1º reta: '))
b = int(input('Escreva o valor da 2º reta: '))
c = int(input('Escreva o valor da 3º reta: '))

if abs(b - c) < a and a < (b + c) and abs(a - c) < b and b < (a + c) and abs(a-b) < c and c < (a + b):
    print('Elas podem formar um triângulo!')
else:
    print('As retas não formam um triângulo!')