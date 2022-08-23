
#? Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Digite quanto dinheiro você tem na carteira: R$'))
dolar = 0.19 #* Cada 1 real está valendo 0.19 dólares na cotação atual.
valor_dolar = real / 5.16

#! Há uma diferença pequena no valor.
print('Com {:.2f} reais é possível comprar {:.2f} dólares.'.format(real, real*dolar))
print('Com {:.2f} reais é possível comprar {:.2f} dólares.'.format(real, valor_dolar))
