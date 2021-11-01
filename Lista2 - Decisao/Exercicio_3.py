# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

a = input('Favor informar o sexto (M) ou (F): ')


if a.lower() == 'm':
    print('Masculino')
elif a.lower() == 'f':
    print('Feminino')
else:
    print('Inválido, digite (M) ou (F)')
