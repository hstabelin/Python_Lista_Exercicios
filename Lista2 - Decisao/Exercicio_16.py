import math


a = float(input('Informe o valor de a: '))


if a == 0:
    print('Não é uma equação do segundo grau')
    exit()

b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))


delta = (b ** 2) - ((4 * a) * c)


if delta < 0:
    print('Equação não tem valores reais')
elif delta == 0:
    x1 = ((b * -1) - (math.sqrt(delta))) / (2 ** a)
    print('A equação possui somente uma raiz, que é:', x1)
else:
    x2 = ((b * -1) + (math.sqrt(delta))) / (2 ** a)
    x3 = ((b * -1) - (math.sqrt(delta))) / (2 ** a)
    print('O resultado da equação é {:.2f} e {:.2f}'.format(x2, x3))
