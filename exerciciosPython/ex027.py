
#? Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: '))
listaNome = nome.split()

priNome = listaNome[0]
ultNome =listaNome[len(listaNome)-1]

print('\33[4;33m', priNome, '\33[m', '\33[4;31m', ultNome, '\33[m')
