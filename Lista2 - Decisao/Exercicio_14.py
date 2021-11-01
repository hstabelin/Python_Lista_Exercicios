# Faça um programa que lê as duas notas parciais obtidas por um aluno
#  numa disciplina ao longo de um semestre, e calcule a sua média.
#  A atribuição de conceitos obedece à tabela abaixo

n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
media = (n1 + n2) / 2


if media > 10:
    print('valor inválido')
elif media < 0:
    print('valor inválido')
elif media > 9:
    print('Suas notas foram', n1, 'e', n2, 'Conceito A - Sua média é: ',
          media, ' e voce foi Aprovado')
elif media >= 7.5:
    print('Suas notas foram', n1, 'e', n2, 'Conceito B - Sua média é: ',
          media, ' e voce foi Aprovado')
elif media >= 6:
    print('Suas notas foram', n1, 'e', n2, 'Conceito C - Sua média é: ',
          media, ' e voce foi Aprovado')
elif media >= 4:
    print('Suas notas foram', n1, 'e', n2, 'Conceito D - Sua média é: ',
          media, ' e voce foi Reprovado')
else:
    print('Suas notas foram', n1, 'e', n2, 'Conceito E - Sua média é: ',
          media, ' e voce foi Reprovado')
