"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Qual é o seu salario? R$ '))
aumento = 15
novo = salario + (salario * aumento / 100)
valorAumento = novo - salario

print('Com o aumento de {}%, o seu salario vai passar de R$ {} para R$ {:.2f} '.format(aumento, salario, novo))
print('Valor do aumento foi de R$ {:.2f} '.format(valorAumento))
