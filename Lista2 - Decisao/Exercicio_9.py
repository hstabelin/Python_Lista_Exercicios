# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

num = [a, b, c]

s = {a, b, c}
s -= {min(s), max(s)}


print('O maior valor é: ', max(num))
print('O valor do meio é: ', s.pop())
print('O maior valor é: ', min(num))
