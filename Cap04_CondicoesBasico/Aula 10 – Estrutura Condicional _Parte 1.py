"""
Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas
 nos seus programas em Python. Veja como aplicar os comandos if: e else: no Python.
"""

print('-=' * 20)

# nome = str(input("Qual seu nome? "))
# if nome == 'Adilson':
#     print('Que nome lindo você tem ')
# print('Bom dia {}!'.format(nome))

print('-=' * 20)

n1 = float(input('Digite primeiro número: '))
n2 = float(input('Digite segundo número: '))

m = (n1 + n2) / 2

print('A média é {:.2f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, PARABÉNS!')
elif m >= 4.0:
    print('Sua média foi ruim, PRECISA MELHORAR')
else:
    print('Sua média foi MUITO ruim, ESTUDE MAIS!')

print('-=' * 20)

# n1 = float(input('Digite sua primeira nota: '))
# n2 = float(input('Digite a sua segunda note:'))
m1 = (n1 + n2) / 2

print('Sua média foi {}'.format(m1))
if m1 >= 6.00:
    print('Parabéns você está aprovado')
elif 5.99 >= m1 >= 2.99:
    print('Você está na recuperação')
else:
    print('Você está reprovado')
