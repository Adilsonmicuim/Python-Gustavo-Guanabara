"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

import math

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno de {} é {:.3f}'.format(angulo, seno))
print('O Cosseno de {} é {:.3f}'.format(angulo, cosseno))
print('A tangente de {} é {:.3f}'.format(angulo, tangente))
