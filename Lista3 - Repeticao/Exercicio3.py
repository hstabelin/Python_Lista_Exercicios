# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


sexo_l = ['m', 'f']
estado_l = ['s', 'c', 'v', 'd']


nome = input('Infome seu nome: ')
if len(nome) < 3:
    print('Nome informado inválido')
    exit()


idade = int(input('Informe sua idade: '))
if idade < 0 or idade > 150:
    print('Idade inválida')
    exit()


salario = int(input('Informe o seu salário: '))
if salario < 1:
    print('Salario inválido')
    exit()


sexo = input('Infome o seu sexo(M) ou (F)')
if sexo not in sexo_l:
    print('Sexo incorreto')
    exit()


estado = input('Informe o estado civil (s) solteiro,'
               '(c) casado, (v) víúvo, (d) divorciado')
if estado not in estado_l:
    print('Estado civil incorreto')
    exit()
else:
    print('Cadastro realizado de forma correta')
