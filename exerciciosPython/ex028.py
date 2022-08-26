
#? Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
#? e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#? O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

sorteado = randint(0, 5)
escolhido = int(input('Diga qual número acha que o computador pensou: '))
sleep(3) #! Função que faz o terminal esperar x(3) segundos até aparecer o resultado.
if sorteado == escolhido:
    print('Parabéns! Você adivinhou!')
else:
    print('Que pena! O computador pensou no nº \33[31m{}\33[m.'.format(sorteado))
