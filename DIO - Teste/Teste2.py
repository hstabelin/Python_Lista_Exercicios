tab = 7


def tabuada(num, senha):
    while num <= senha:
        print(f'{num} * {tab} = ', num * tab)
        num = num + 1


print(tabuada(0, 10))
