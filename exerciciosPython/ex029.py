
#? Escreva um programa que leia a velocidade de um carro.
#? Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#? A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual era a velocidade do carro (em Km/h)? R: '))
if velocidade > 80:
    kmAcima = velocidade - 80
    multa = kmAcima * 7
    print('O carro foi multado em R${},00 por ultrapassar a velocidade permitida!'.format(multa))
else:
    print('O carro não foi multado.')
    