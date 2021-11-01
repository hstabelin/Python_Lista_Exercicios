# Faça um Programa que pergunte quanto você ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário
#  no referido mês, sabendo-se que são descontados 11% para o Imposto
#  de Renda, 8% para o INSS e 5% para o sindicato

horas = float(input('Informe a quantidade de horas trabalhadas: '))
valor = float(input('Informe o valor da hora: '))


salario_bruto = valor * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario = salario_bruto - descontos

print('+ Salário Bruto: R${:0.2f}'.format(salario_bruto))
print('- IR(11%): R${:0.2f}'.format(ir))
print('- INSS(8%): R${:0.2f}'.format(inss))
print('- Sindicato(5%): R${:0.2f}'.format(sindicato))
print('= Salário Liquido: R${:0.2f}'.format(salario))
