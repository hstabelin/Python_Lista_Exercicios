# Faça um programa que peça o tamanho de um arquivo para download (em MB)
#  e a velocidade de um link de Internet (em Mbps), calcule e informe o
#  tempo aproximado de download do arquivo usando este link (em minutos).

mb = float(input('Informe o tamanho do arquivo(MB): '))
link = float(input('Informe a velocidade: '))


veloc = (mb / link) / 60

print('O tempo de espera para o download é {:0.0f} minutos'.format(veloc))
