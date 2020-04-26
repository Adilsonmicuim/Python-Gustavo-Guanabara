"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = str(input('Nome completo: ')).strip()  # strip elimina os espaços
print('Seu nome tem silva {}'.format('silva' in nome.lower()))
