"""
Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(), transformações
com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
"""

frase = str('Curso em video python')

print('Tamanho da frase é:', len(frase))
print(frase.count('o'))  # soma a quantidade de "o" na frase
print(frase.count('o', 0, 15))  # de zero a quinze
print(frase.find('deo'))  # mostra a posição onde inicia
print(frase[9:15])
print(frase[0:15])
print(frase[9::15])
print(frase[9:15:2])  # saltando de dois em dois
print(frase[:5])
print(frase[5:])
print('Curso' in frase)
print(frase.find('Android'))  # Aparecerá valor negativo
print(frase.upper())  # O que for maiúsculo mantém e os minusculos passam ser maiúsculo
print(frase.lower())  # É o inverso de upper
print(frase.capitalize())  # Deixa o primeiro caracter maiúsculo e o restante minusculo
print(frase.title())  # analisa quantas palavras tem na frase e deixa a primeira letra maiúscula
print('----------------------------------')
print(frase.split())  # Vai criar uma divisão onde tem espaço
print('----------------------------------')
print('-'.join(frase))
print('----------------------------------')
print(frase.replace('python', 'Android'))  # Substituiria a palavra python por Android, de modo não efetivo.
