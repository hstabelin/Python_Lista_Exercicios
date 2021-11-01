# Tendo como dado de entrada a altura (h) de uma pessoa, construa um
# algoritmo que calcule seu peso ideal

h = float(input('Informe a sua altura em cms: '))

homem = (72.7 * (h / 100)) - 58
mulher = (62.1 * (h/100)) - 44.7


print('O seu peso ideal se for homem é: {:0.2f}kg e se for mulher é: {:0.2f}kg'
      .format(homem, mulher))
