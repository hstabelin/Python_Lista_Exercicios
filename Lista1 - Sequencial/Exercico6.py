# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math


pi = math.pi
raio = float(input('Informe o raio'))


resultado = pi * (raio ** 2)
print('A área do círculo é {}'.format(resultado))
