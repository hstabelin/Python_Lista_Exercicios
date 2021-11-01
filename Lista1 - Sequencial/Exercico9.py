# Faça um Programa que peça a temperatura em graus Fahrenheit,
#  transforme e mostre a temperatura em graus Celsius.

f = float(input('Informa a temperatura em F°: '))


c = 5 * ((f-32)/9)


print('A temperatura em Celsius é: C°{}'.format(round(c, 2)))
