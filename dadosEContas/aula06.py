# n1 = input ('Digite um valor: ')
# print(type(n1));
# ! Saída: <class 'str'>

# n1 = int(input('Digite um valor: '))
# n2 = int(input('Digite outro valor: '))
# s = n1 + n2
# * print('A soma entre ', n1, ' e ', n2, ' é ', s)
# print('A soma entre {} e {} é {}'.format(n1, n2, s)) # ! Forma atual

# n = bool(input('Digite um valor: '))
# ? Caso possua um valor, retorna true e caso esteja vazio, retorna false.
# print(n)

# ! Métodos de testes de Tipos
n = input('Digite algo: ')
# print(n.isnumeric())  # ? retorna true se for numérico e false se não for.
# print(n.isalpha())  # ? retorna true se for apenas letra e false se não for.
# print(n.isalnum())  # ? retorna true se for alphanumérico e false se não for.
print(n.isupper())  # ? retorna true se for todas maiúscula e false se não.
