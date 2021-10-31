mb = float(input('Informe o tamanho do arquivo(MB): '))
link = float(input('Informe a velocidade: '))


veloc = (mb / link) / 60

print('O tempo de espera para o download é {:0.0f} minutos'.format(veloc))
