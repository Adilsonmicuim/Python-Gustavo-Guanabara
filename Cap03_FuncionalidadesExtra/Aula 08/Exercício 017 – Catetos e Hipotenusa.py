"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
 de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

import math

co1 = float(input('Digite o cateto oposto: '))
ca1 = float(input('Digite o cateto adjacente: '))
hi1 = (co1 ** 2 + ca1 **2) ** (1/2)
hi2 = math.hypot(co1, ca1)

print('A Hipotenusa vai medir {:.2f}'.format(hi1))
print('A Hipotenusa vai medir {:.2f}'.format(hi2))
