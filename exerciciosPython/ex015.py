
#? Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
#? e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPercorridos = float(input('Digite a quantidade de Km percorridos: '))
qntDias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))

print('O valor a pagar é de R${:.2f}'.format((kmPercorridos * 0.15) + (qntDias * 60)))
