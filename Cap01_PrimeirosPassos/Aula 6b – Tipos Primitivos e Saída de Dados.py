# Métodos de testes de tipo
# O input (entrada de dados) sem definir será sempre string

n1 = input('Digite um valor: ')
print(type(n1))
print('É número? ', n1.isnumeric())
print('É letra? ', n1.isalpha())
print('É alfanumérico? ', n1.isalnum())
print('Somente letras maiúsculas? ', n1.isupper())
