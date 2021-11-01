# Faça um programa que leia um nome de usuário e a sua senha e não aceite
#  a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando
#  a pedir as informações

user = input('Informe o nome do usuário: ')
senha = input('Informe a senha: ')


while user == senha:
    print('Senha não pode ser igual o nome do usuário, informe outra senha')
    senha = input('Informe a senha: ')


print('Senha cadastrada com sucesso!')
