#! python
numero = int(input('Informe um valor de 0 a 10: '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


while numero not in lista:
    print('Valor incorreto, informe novamente o valor')
    numero = int(input('Informe um valor de 0 a 10: '))

print(f'Valor {numero} está correto!')
