# Faça um programa que receba dois números inteiros e gere os números
#  inteiros que estão no intervalo compreendido por eles

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = [0]
if a < b:
    while a < b:
        print(a)
        c.append(a)
        a = a + 1
    exit()
else:
    while a > b:
        print(b)
        c.append(b)
        b = b + 1
