"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
"""

cidade = str(input('Em que cidade você nasceu? ')).strip()  # strip elimina os espaços
print(cidade[:5].upper() == 'SANTO')  # upper converter a cidade (input) para maiusculo
