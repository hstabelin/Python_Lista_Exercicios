# Faça um Programa que peça a temperatura em graus Celsius, transforme
# e mostre em graus Fahrenheit.

c = float(input('Informe a temperatura em C°: '))


f = ((c * 9) / 5) + 32


print('A temperatura em Farenheit é: F°{}'.format(round(f, 2)))
