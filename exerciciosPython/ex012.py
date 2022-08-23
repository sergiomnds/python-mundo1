
#? Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
novo_preco = preco - (preco * 0.05)
print('O produto de custo R${:.2f}, fica por {:.2f} com 5% de desconto.'.format(preco, novo_preco))
