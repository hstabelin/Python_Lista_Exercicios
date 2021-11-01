# Faça um Programa que verifique se uma letra digitada é vogal ou consoante

a = input('Informe a letra: ')
vogal = ['a', 'e', 'i', 'o', 'u']


if a.lower() in vogal:
    print('vogal')
elif len(a) > 1:
    print('parametro inválido')
else:
    print('consoante')
