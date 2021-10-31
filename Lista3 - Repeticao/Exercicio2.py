#! python
user = input('Informe o nome do usuário: ')
senha = input('Informe a senha: ')


while user == senha:
    print('Senha não pode ser igual o nome do usuário, informe outra senha')
    senha = input('Informe a senha: ')


print('Senha cadastrada com sucesso!')
