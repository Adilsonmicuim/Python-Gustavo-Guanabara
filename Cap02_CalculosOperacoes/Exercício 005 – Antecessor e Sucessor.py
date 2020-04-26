"""
Faça um programa que leia um número inteiro e mostra
na tela o seu sucessor e seu antecessor
"""

n = int(input("Digite primeiro número: "))
a = n - 1
s = n + 1

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))
print('=' * 50)
# O valor aplicado abaixo não necessitam das variáveis a e s,
# mas não é muito recomendado, caso deseja utilizar as variáreis no decorrer do código.
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n - 1), (n + 1)))
