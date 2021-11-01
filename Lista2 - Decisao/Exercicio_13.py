# Faça um Programa que leia um número e exiba o dia correspondente
#  da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor
#  deve aparecer valor inválido

a = {1: 'Domingo', 2: 'Segunda', 3: 'Terça',
     4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sabado'}


b = int(input('Informe um número de 1 a 7: '))

if b in a:
    print(a.get(b))
else:
    print('Valor inválido')
