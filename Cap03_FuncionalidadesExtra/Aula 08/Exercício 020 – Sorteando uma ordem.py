"""
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random

nam1 = str(input('Digite primeiro nome: '))
nam2 = str(input('Digite segundo nome: '))
nam3 = str(input('Digite o terceiro nome: '))
nam4 = str(input('Digite o quarto nome: '))
list = [nam1, nam2, nam3, nam4]
random.shuffle(list)  # shuffle embaralha os nomes

print('A ordem de apresentação será ')
print(list)
