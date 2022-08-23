# nome =input('Qual o seu nome? ')
# print('Prazer em te conhecer, {:=^20}!'.format(nome))

# *{:20} -> Escreve o nome com 20 caracteres
# *{:<20} -> Escreve o nome com 20 caracteres e alinha a esquerda
# *{:>20} -> Escreve o nome com 20 caracteres e alinha a direita
# *{:^20} -> Escreve o nome com 20 caracteres e centraliza
# *{:=^20} -> Centraliza o nome e coloca os iguais antes e depois.

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
# print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
de = n1 // n2
p = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end='>>>')
# * {:.3f} -> Limita até 3 pontos flutuantes
# * end=' ' e end='>>>' -> Para não ter quebra de linha nos prints
# * \n -> Quebra de linha dentro do print
print('A divisão exata é {} e a potência é {}'.format(de, p))
