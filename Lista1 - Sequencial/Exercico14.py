peso = float(input('Informar o peso dos peixes: '))


limite = 50
multa = (peso - limite) * 4

if (peso > 50):
    print('O valor de sua multa é de R$:{:0.2f}'.format(multa))
else:
    print('Peso dentro do limite, não há multa')
