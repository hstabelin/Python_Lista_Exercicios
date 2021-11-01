# Faça um programa que pergunte o preço de três produtos e informe
#  qual produto você deve comprar, sabendo que a decisão é sempre
#  pelo mais barato.

carne = float(input('Informe o valor da carne: '))
leite = float(input('Informe o valor da leite: '))
pao = float(input('Informe o valor da pão: '))
produtos = [carne, leite, pao]


if leite > carne:
    print('leite')
elif pao > leite:
    print('pão')
else:
    print('carne')
