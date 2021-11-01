# Faça um Programa que pergunte quanto você ganha por hora e o
#  número de horas trabalhadas no mês. Calcule e mostre o total
#  do seu salário no referido mês.

valor_hora = float(input('Quanto ganha por hora: '))
qntd_hora = float(input('Quantas horas por mês: '))

salario = valor_hora * qntd_hora


print('O seu salário no mês é: R${}'.format(salario))
