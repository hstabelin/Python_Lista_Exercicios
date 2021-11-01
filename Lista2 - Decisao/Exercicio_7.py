# Faça um Programa que leia três números e mostre o maior e o menor deles.

a = float(input('Informar o 1° número: '))
b = float(input('Informar o 2° número: '))
c = float(input('Informar o 3° número: '))
numero = [a, b, c]


print('Maior número', max(numero))
print('Menor número', min(numero))
