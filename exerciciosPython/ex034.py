
#? Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#? Para salários superiores a R$1250,00, calcule um aumento de 10%.
#? Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250:
    taxa = 0.1
    aumento = salario * taxa
    salario = salario + aumento
else:
    taxa = 0.15
    aumento = salario * taxa
    salario = salario + aumento

print('O salário recebeu um aumento de {:.0f}%, ficando no total de R${:.2f}'.format(taxa*100, salario))
