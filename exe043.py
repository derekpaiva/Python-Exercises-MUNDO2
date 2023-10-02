import math
from time import sleep

print('-==-' *12)
print('Bem-vindo! Vamos iniciar a \033[1;40mCalculadora de IMC!\033[m')
print('-==-' *12)
print('INCIANDO...')
sleep(3)
p = float(input('Digite o valor do seu peso (em kg): '))
a = float(input('Agora, digite o valor da sua altura (em metros): '))
print('PROCESSANDO...')
sleep(3)

imc = p/pow(a, 2)

if imc < 18.5:
    print('Seu IMC é {:.2f} \n Você está \033[1;30;41mABAIXO DO PESO\033[m \n Cuidado, você deve procurar um profissional!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f} \n Você está \033[1;30;42mPESO IDEAL\033[m \n Mantenha-se saudável'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f} \n Você está \033[1;30;43mSOBREPESO\033[m \n Tome um pouco de cuidado!'.format(imc))
else:
    print('Seu IMC é {:.2f} \n Você está \033[1;30;41mOBSEDIDADE MÓRBIDA\033[m \n Cuidado, você deve procurar um profissional!'.format(imc))