
#? Crie um programa que leia o nome completo de uma pessoa e mostre:
#? – O nome com todas as letras maiúsculas e minúsculas.
#? – Quantas letras ao todo (sem considerar espaços).
#? – Quantas letras tem o primeiro nome.
nome = str(input('Escreva seu nome completo: ')).strip()
print('Nome em Maiúsculo: {}'.format(nome.upper()))
print('Nome em Minúsculo: {}'.format(nome.lower()))
listNome = nome.split()
print('Esse nome possui {} letras.'.format(len(''.join(listNome)))) #* Podia ser len(nome) - nome.count(' ')
print('O primeiro nome possui {} letras'.format(len(listNome[0])))
