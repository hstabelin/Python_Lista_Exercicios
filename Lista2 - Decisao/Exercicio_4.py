a = input('Informe a letra: ')
vogal = ['a', 'e', 'i', 'o', 'u']


if a.lower() in vogal:
    print('vogal')
elif len(a) > 1:
    print('parametro inválido')
else:
    print('consoante')
