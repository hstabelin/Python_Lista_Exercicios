# Faça um Programa para leitura de três notas parciais de um aluno.
#  O programa deve calcular a média alcançada por aluno

n1 = float(input('Favor informar a sua nota n1: '))
n2 = float(input('Favor informar a sua nota n2: '))
n3 = float(input('Favor informar a sua nota n3: '))


notas = [n1, n2, n3]
media = sum(notas) / len(notas)


if media > 10 or media < 0:
    print('Erro - Valores informados estão incorretos')
elif media == 10:
    print(
        'Sua média foi {:.1f} e você foi Aprovado com Distinção'.format(media))
elif media >= 7:
    print('Sua média foi {:.1f} e você foi Aprovado'.format(media))
else:
    print('Sua média foi {:.1f} e você foi Reprovado'.format(media))
