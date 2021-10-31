caixa = input('Favor informar o valor do saque (Min R$10,00 e Max R$ 600,00): ')


if int(caixa) < 10 or int(caixa) > 600:
    print('Valor incorreto (Min R$10,00 e Max R$ 600,00)')
    exit()
elif len(caixa) == 2:
    if int(caixa) > 50:
        n50 = int(caixa) -50
    
    

