
#? Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: '))
listaNome = nome.split()

priNome = listaNome[0]
ultNome =listaNome[len(listaNome)-1]

print(priNome, ultNome)
