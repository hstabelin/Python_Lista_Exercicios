# Faça um programa para uma loja de tintas. O programa deverá pedir
#  o tamanho em metros quadrados da área a ser pintada. Considere que
#  a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#  Informe ao usuário a quantidades de latas de tinta a serem compradas
#  e o preço total.

area = float(input('Informe a área a ser pintada: '))

valor = 80
balde = 18


quantidade = (area/3) / balde
preco = round(quantidade, 0) * valor


print('Serão necessários {:0.0f} baldes e o preço é R${:0.2f}'.format(
    quantidade, preco))
