# Faça um Programa que peça 2 números inteiros e um número real.
#  Calcule e mostre:
#    o produto do dobro do primeiro com metade do segundo .
#    a soma do triplo do primeiro com o terceiro.
#    o terceiro elevado ao cubo.


a = int(input('Informe um número inteiro: '))
b = int(input('Informe um número inteiro: '))
c = float(input('Informe um número real: '))


primeira = (a * 2) * (b / 2)
segunda = (a * 3) + c
terceira = (c ** 3)


print('O resultado da primeira é:{}, da segunda é:{} e da terceira é:{}'
      .format(primeira, segunda, terceira))
