"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))

media = (n1 + n2) / 2

print("A média da nota 1 {} e nota 2 {} é: {} ".format(n1, n2, media))
print("A média da nota 1 {:.3f} e nota 2 {:.3f} é: {:.3f} ".format(n1, n2, media))
