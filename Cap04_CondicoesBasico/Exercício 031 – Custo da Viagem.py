"""
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
parta viagens mais longas.
"""

precoA = 0.50
precoB = 0.45

km = float(input('Digite a distância da viagem em km: '))

custoA = km * precoA
custoB = km * precoB

valorPassagem = custoA if km <= 200 else custoB
print('O custo da sua viagem será R$ {}'.format(valorPassagem))

# if km <= 200:
#     print('Custo da passagem é {}'.format(custoA))
# else:
#     print('Custo da passagem é {}'.format(custoB))

print('Boa viagem MIGUXO!')