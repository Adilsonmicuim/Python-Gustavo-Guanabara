"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
import math

num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {} '.format(num, math.trunc(num)))

print('-----------------------------------------------------------------------------------')
from math import trunc

print('O valor digitado foi {} e sua porção inteira é {} '.format(num, trunc(num)))

print('-----------------------------------------------------------------------------------')
# Poderia fazer desta maneira sem necessidade de importar módulos
print('O valor digitado foi {} e sua porção inteira é {} '.format(num, int(num)))
