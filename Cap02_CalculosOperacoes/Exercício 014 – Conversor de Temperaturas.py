"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

celsius = float(input("Digite um temperatura em Celsius: "))
fahrenheit = ((9 * celsius) / 5) + 32

print('A temperatura {}°C em Fahrenheit é: {}°F'.format(celsius, fahrenheit))
