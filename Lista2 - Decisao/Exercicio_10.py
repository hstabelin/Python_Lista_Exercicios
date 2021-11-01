# Faça um Programa que pergunte em que turno você estuda. Peça para
#  digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
#  "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
#  conforme o caso

a = input('Informar o turno que estuda: (M) Matutino, (V) Vespertino'
          ' (N)Noturno:  ')


if a.lower() == 'm':
    print('Bom dia')
elif a.lower() == 'v':
    print('Boa tarde')
elif a.lower() == 'n':
    print('Boa noite')
else:
    print('Valor incorreto')
