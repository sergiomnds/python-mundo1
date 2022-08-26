
#? Desenvolva um programa que pergunte a distância de uma viagem em Km.
#? Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia =int(input('Qual a distância da viagem (em Km) ? '))
if distancia > 200:
    taxa = 0.45
else:
    taxa = 0.5
passagem = distancia * taxa
print('O preço da passagem será de R${:.2f}'.format(passagem))
