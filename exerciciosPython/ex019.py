
#? Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#? Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

aluno1 = str(input('Escreva o nome do primeiro aluno: '))
aluno2 = str(input('Escreva o nome do segundo aluno: '))
aluno3 = str(input('Escreva o nome do terceiro aluno: '))
aluno4 = str(input('Escreva o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4] #! Tem a lista para poder usar o choice
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
