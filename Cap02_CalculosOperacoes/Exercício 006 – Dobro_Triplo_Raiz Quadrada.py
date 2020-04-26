"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3
raiz = n ** (1 / 2)

print('O dobro de {} é {}'.format(n, dobro))
print(triplo)
print('{:.2f}'.format(raiz))
