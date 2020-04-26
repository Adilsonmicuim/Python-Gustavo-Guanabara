"""
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

padrao = 1250
percentoA = 10
percentoB = 15

salario = float(input('Digite o salario: '))

if salario <= padrao:
    novo = salario + (salario*percentoB/100)
else:
    novo = salario + (salario*percentoA/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))