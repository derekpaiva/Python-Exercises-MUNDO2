from datetime import date

sexo = int(input('Digite o seu sexo: [1] para masculino e [2] para feminino: '))

if sexo == 1:
    print('Você é do sexo masculino.')

    nasc = int(input('Digite o seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    saldo1 = 18 - idade
    saldo2 = idade - 18

    print('Quem nasceu em {} completa {} anos em {}!'.format(nasc, idade, ano_atual))

    if idade == 18:
        print('Você já possui {} anos! \nJá está na hora de você se alistar!'.format(idade))
    elif idade > 18:
        print('Você tem {} anos! \nSeu alistamento foi há {} anos!\nCorra para a junta militar de sua cidade!'.format(idade, saldo2))
    else:
        print('Você tem {} anos! \nAinda faltam {} anos para você se alistar! \nAguarde os seus 18 anos!'.format(idade, saldo1))
else:
    print('Você é do sexo feminino! \nNão há necessidade de alistamento!')