from math import radians, sin, cos, tan

#? Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
angulo = float(input('Digite o valor de um ângulo: '))
angulo = radians(angulo) #*transformar em radiano para calcular.

print('O ângulo de {:.1f} graus possui SENO igual a {:.2f},'
    '\nO COSSENO vale {:.2f},'
    '\nE a tangente vale {:.2f}.'.format(angulo, sin(angulo), cos(angulo), tan(angulo)))
