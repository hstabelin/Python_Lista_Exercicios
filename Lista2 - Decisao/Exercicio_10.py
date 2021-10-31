a = input('Informar o turno que estuda: (M) Matutino, (V) Vespertino'
          ' (N)Noturno:  ')


if a.lower() == 'm':
    print('Bom dia')
elif a.lower() == 'v':
    print('Boa tarde')
elif a.lower() == 'n':
    print('Boa noite')
else:
    print('Valor incorreto')
