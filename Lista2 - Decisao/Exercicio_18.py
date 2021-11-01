# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
#  se a mesma é uma data válida

data = input('Informe uma data no formato dd/mm/aaaa: ')


b1 = data[2:3]
b2 = data[5:6]
msgerr = 'Erro - Favor informar no formato dd/mm/aaaa'

if b1 != '/':
    print(msgerr)
    exit()
elif b2 != '/':
    print(msgerr)
    exit()
elif len(data) > 10:
    print(msgerr)
    exit()
elif len(data) < 10:
    print(msgerr)
    exit()
else:
    d = int(data[:2])
    m = int(data[3:5])
    a = int(data[-4:])


if d < 1 or d > 31:
    print('Valor dia está incorreto')
elif m < 1 or m > 12:
    print('Valor mês está incorreto')
elif a < 1 or a > 3000:
    print('Valor ano está incorreto')
else:
    print('Valor está incorreto')
