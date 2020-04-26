"""
Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI
para configurar cores para os seus programas em Python. Veja como utilizar
o código \033[m com todas as suas principais possibilidades.
"""
print('\033[31m 1 - Olá mundo')
print('\033[1;31;43m 2 - Olá mundo\033[m')
print('\033[4;30;45m 3 - Olá mundo\033[m')
print('\033[36m 4 - Olá mundo\033[m')
print('\033[7;33;44m 5 - Olá mundo\033[m')

a = 3
b = 5
print('Os valores são \033[31m{}\033[m e \033[32m{}\033[m!!!'.format(a, b))

nome = 'mico'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'pretoBranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['verde'], nome, cores['limpa']))
