# Altere o programa anterior para mostrar no final a soma dos números

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = [0]
if a < b:
    while a < b:
        print(a)
        c.append(a)
        a = a + 1
    print('O resultado da soma é:', sum(c))
    exit()
else:
    while a > b:
        print(b)
        c.append(b)
        b = b + 1
    print('O resultado da soma é:', sum(c))
