"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

KmRodado = float(input('Quantidade de km rodado: '))
numDias = int(input('Número de dias alugado: '))
ValorDiaria = 60
ValorKm = 0.15

ValorPagar = (KmRodado * ValorKm) + (numDias * ValorDiaria)

print('Custo total = R$ {:.2f} '.format(ValorPagar))