
#? Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 1.8) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF.'.format(celsius, fahrenheit))
