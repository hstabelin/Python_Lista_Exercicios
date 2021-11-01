# Faça um Programa para uma loja de tintas. O programa deverá pedir
#  o tamanho em metros quadrados da área a ser pintada. Considere que
#  a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que
#  a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
#  galões de 3,6 litros, que custam R$ 25,00.

import math


area = float(input('Informa a área a ser pintada: '))


area_tinta = math.ceil(area / 3)
preco_lata = 80
preco_galao = 25
quantidade_lata = 18
quantidade_galao = 3.6

# se o cliente quiser somente lata
oferta1 = math.ceil(area_tinta / quantidade_lata)
valor_oferta1 = oferta1 * preco_lata

# se o cliente quiser somente galão
oferta2 = math.ceil(area_tinta / quantidade_galao)
valor_oferta2 = oferta2 * preco_galao

# Um mix dos valores
oferta3 = (area_tinta * 1.10) // quantidade_lata
qntd_gala = math.ceil((area_tinta % quantidade_lata) / quantidade_galao)
valor_oferta3 = (oferta3 * preco_lata) + (qntd_gala * preco_galao)

print('Opção 1: Nessa opção serão {} latas e o custo é de: R${}'
      .format(oferta1, valor_oferta1))
print('Opção 2: Nessa opção serão {} galões e o custo é de: R${}'
      .format(oferta2, valor_oferta2))
print('Opção 3: Nessa opção serão {} latas, {} galões e o custo é de : R${}'
      .format(oferta3, qntd_gala, valor_oferta3))
