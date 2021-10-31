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
