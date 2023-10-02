from datetime import date

print('Olá, seja bem vindo!')
ano = int(input('Por favor, digite o ano de nascimento do atleta: '))
ano_atual = date.today().year

idade = ano_atual - ano

if idade <= 9:
    print('Sua idade é {} e você está na categoria \033[1mMIRIM\033[m'.format(idade))
elif idade > 9 and idade <= 14:
    print('Sua idade é {} e você está na categoria \033[1mINFANTIL\033[m'.format(idade))
elif idade > 14 and idade <= 19:
    print('Sua idade é {} e você está na categoria \033[1mJÚNIOR\033[m'.format(idade))
elif idade > 19 and idade == 20:
    print('Sua idade é {} e você está na categoria \033[1mSÊNIOR\033[m'.format(idade))
else:
    print('Sua idade é {} e você está na categoria \033[1mMASTER\033[m'.format(idade))