# Faça um Programa que calcule a área de um quadrado, em seguida
# mostre o dobro desta área para o usuário.

largura = float(input('Informe a largura: '))
comprimento = float(input('Informe o comprimento: '))


area = largura * comprimento
dobro_area = area * 2


print('O dobro da área é: {}'.format(dobro_area))
