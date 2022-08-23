
# ? Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número inteiro: '))
print('{}'.format('-'*15))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, n*i))
print('{}'.format('-'*15))