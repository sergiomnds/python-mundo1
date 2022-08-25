
#? Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
#? em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()

qntAparece = frase.upper().count('A')
aparecePrimeiro = frase.upper().find('A')
apareceUltimo = frase.upper().rfind('A')

print('''\nA letra A aparece {} vezes na frase {},
Aparece pela primeira vez na posição {},
Aparece pela última vez na posição {}.\n'''.format(qntAparece, frase, aparecePrimeiro + 1, apareceUltimo + 1))