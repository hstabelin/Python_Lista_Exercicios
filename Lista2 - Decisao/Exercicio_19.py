num = (input('Informar o número (limita a 999): '))


if int(num) > 999:
    print('Erro - Valor informado inválido')
    exit()
elif len(num) == 2:
    d = num[0]
    u = num[1]
    if int(d) > 1:
        d1 = 'Dezenas'
    else:
        d1 = 'Dezena'
    if int(u) > 1:
        u1 = 'Unidades'
    else:
        u1 = 'Unidade'
elif len(num) == 1:
    u = num[0]
    if int(u) > 1:
        u1 = 'Unidades'
    else:
        u1 = 'Unidade'
else:
    c = num[0]
    d = num[1]
    u = num[2]
    if int(c) > 1:
        c1 = 'Centenas'
    else:
        c1 = 'Centena'
    if int(d) > 1:
        d1 = 'Dezenas'
    else:
        d1 = 'Dezena'
    if int(u) > 1:
        u1 = 'Unidades'
    else:
        u1 = 'Unidade'


if len(num) == 3:
    print('O valor é de {} {}, {} {} e {} {}'. format(c, c1, d, d1, u, u1))
elif len(num) == 2:
    print('O valor é de {} {} e {} {}'.format(d, d1, u, u1))
else:
    print('O valor é de {} {}'.format(u, u1))
