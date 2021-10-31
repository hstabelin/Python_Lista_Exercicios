area = float(input('Informe a área a ser pintada: '))

valor = 80
balde = 18


quantidade = (area/3) / balde
preco = round(quantidade, 0) * valor


print('Serão necessários {:0.0f} baldes e o preço é R${:0.2f}'.format(
    quantidade, preco))
