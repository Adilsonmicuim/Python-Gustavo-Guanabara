"""
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. Tente adivinhas...')
print('-=-' * 20)
jogador = int(input('Que número pensei? '))

print('PROCESSANDO...')
sleep(1)  # segundos
if jogador == computador:
    print('Acertou!')
else:
    print('Errou, computador escolheu {}!'.format(computador))
