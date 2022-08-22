import emoji #*Teve que ser instalado manualmente, pelo site do PyPI
#! import alguma coisa -> Import GERAL
import random
from math import floor, sqrt


num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz))) 
#* math.ceil -> Arredonda para cima!
#* math.floor -> Arredonda para baixo!

num2 = random.randint(1,10)
print(num2)
#* random.random() -> Nº aleatório float
#* random.randin() -> Nº aleatório int

print(emoji.emojize('Olha a fazendinha passando: :baby_chick: :pig: :horse:'))