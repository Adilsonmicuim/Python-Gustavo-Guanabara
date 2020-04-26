"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preco = float(input('Qual o preço do produto? R$ '))
desconto = 5
novo = preco - (preco * desconto / 100)
valorDesconto = preco - novo

print('O produto custava R$ {}, com desconto de {}% vai custar R$ {:.2f} '.format(preco, desconto, novo))
print('Valor do desconto foi de R$ {:.2f} '.format(valorDesconto))