"""
Faça um programa que leia algo pelo teclado e mostra na tela o seu
tipo primitivo e todas as informações possíveis sobre ela.
"""

n1 = input('Digite um valor: ')
print('O tipo primitivo deste valor é: ', type(n1))
print('É número? ', n1.isnumeric())
print('É letra? ', n1.isalpha())
print('É alfanumérico? ', n1.isalnum())  # Possui letras e números
print('Somente letras maiúsculas? ', n1.isupper())
print('Somente letras minusculas? ', n1.islower())
print('Somente espaços? ', n1.isspace())
print('Está capitalizada', n1.istitle())  # nem maiusculo nem minusculo
