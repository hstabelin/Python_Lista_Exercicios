# Faça um programa que leia 5 números e informe a soma e a média dos números

a = int(input('Informe um número: '))
b = int(input('Informe um número: '))
c = int(input('Informe um número: '))
d = int(input('Informe um número: '))
e = int(input('Informe um número: '))
f = [a, b, c, d, e]

soma = sum(f)
media = sum(f) / len(f)
print(f'A soma dos valores é {soma} e a média é {media}')
