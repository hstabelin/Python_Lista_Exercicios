# As Organizações Tabajara resolveram dar um aumento de salário aos
#  seus colaboradores e lhe contraram para desenvolver o programa
# que calculará os reajustes.

a = float(input('Informe o salário atual: '))

faixa1 = 1.2
faixa2 = 1.15
faixa3 = 1.1
faixa4 = 1.05


if a > 1500:
    nsal = a * faixa4
elif a >= 700:
    nsal = a * faixa3
elif a >= 280:
    nsal = a * faixa2
else:
    nsal = a * faixa1

print('O salário atual é R$:', a)
print('O valor do aumento é R$: {:0.2f}'.format((((nsal/a)-1)*100)), '%')
print('O valor do aumento é de R$', (nsal-a))
print('O novo salário será R$:', nsal)
