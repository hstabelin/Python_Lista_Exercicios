n1 = float(input('Informar a nota1: '))
n2 = float(input('Informar a nota2: '))

nmedia = (n1 + n2) / 2


if nmedia == 10:
    print('Aprovado com Distinção')
elif nmedia >= 7:
    print('Aprovado')
else:
    print('Reprovado')
