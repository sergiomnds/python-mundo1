
#? Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário do funcionário: R$'))
novo_salario = salario + (salario * 0.15)
print('O salário de R${:.2f}, fica {:.2f} com o aumento de 15%.'.format(salario, novo_salario))
