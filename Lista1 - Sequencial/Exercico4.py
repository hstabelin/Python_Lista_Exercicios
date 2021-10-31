b1 = float(input('Informar a nota do 1b: '))
b2 = float(input('Informar a nota do 2b: '))
b3 = float(input('Informar a nota do 3b: '))
b4 = float(input('Informar a nota do 4b: '))


nota = (b1, b2, b3, b4)

media = sum(nota) / len(nota)
print(media)
