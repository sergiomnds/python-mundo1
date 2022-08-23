
#? Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite o nome para verificar: ')).upper().strip()
valido = 'SILVA' in nome
if(valido):
    print('O nome possui Silva!')
else:
    print('O nome NÃO possui Silva!')