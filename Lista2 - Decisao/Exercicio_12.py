a = float(input('Informe o valor da hora: '))
b = float(input('Informe a quantidade de horas: '))

slrbruto = a * b

ir1 = 0.2
ir2 = 0.1
ir3 = 0.05

if slrbruto > 2500:
    ir = slrbruto * ir1
elif slrbruto > 1500:
    ir = slrbruto * ir2
elif slrbruto > 900:
    ir = slrbruto * ir3
else:
    ir = 0

sindi = slrbruto * 0.03
inss = slrbruto * 0.1
fgts = slrbruto * 0.11
descontos = ir + sindi + inss
aliquota = (ir/slrbruto) * 100

print('Salário Bruto: R$ ', slrbruto)
print('(-) IR ({:0.0f}%): R$'.format(aliquota), ir)
print('(-) INSS (10%): R$', inss)
print('(-) Sindicato (3%): R$', sindi)
print('FGTS (11%): R$ ', fgts)
print('Total de descontos: R$', (ir + inss + sindi))
print('Salário Liquído: R$', (slrbruto - descontos))
