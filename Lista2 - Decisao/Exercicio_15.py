# Faça um Programa que peça os 3 lados de um triângulo. O programa
#  deverá informar se os valores podem ser um triângulo. Indique, caso
# os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno

l1 = float(input('Informe o lado 1: '))
l2 = float(input('Informe o lado 2: '))
l3 = float(input('Informe o lado 3: '))


a = [l1, l2, l3]
b = [l2, l3]
c = [l1, l2, l3]


if l1 > sum(b):
    print('Não é um triangulo')
elif l1 == l2 and l2 == l3:
    print('É um triangulo Equilátero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('É um triangulo Isosceles')
else:
    print('É um triangulo Escaleno')
