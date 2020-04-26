import math
from math import floor  # Importação para realizar o último calculo

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A Raiz de {} é: {}'.format(num, raiz))

print('=' * 50)
print('A Raiz de {} é: {:.0f}'.format(num, raiz))
print('A Raiz de {} é: {}'.format(num, math.ceil(raiz)))  # ceil é arredondamento para cima.
print('A Raiz de {} é: {}'.format(num, floor(raiz)))  # ceil é arredondamento para baixo.
