"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere U$$ 1,00 = R$ 4,22  -  Data 05/12/2019
"""

real = float(input('Quanto de dinheiro você tem na carteira? '))
dolar = real / 3.27

print('Com R$ {} reais você pode comprar UU$ {:.2f} '.format(real, dolar))
