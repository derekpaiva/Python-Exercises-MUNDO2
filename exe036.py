from time import sleep

print('-==-' *16)
print('Olá, seja bem vindo a \033[1;40mCalculadora de Financiamento Imobiliário!\033[m')
print('-==-' *16)

print('\033[1;30;43mINCIANDO...\033[m')
sleep(3)
print('-==-' *16)
casa_valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite a quantidade de meses que deseja financiar a casa: '))
print('-==-' *16)
print('\033[1;30;42mCALCULANDO...\033[m')
sleep(3)

prest = casa_valor/anos
faixa = salario*0.30

if prest <= faixa:
    print('Parabéns, seu financiamento foi aceito!!! \n O valor da prestação é de R${:.2f}'.format(prest))
else:
    print('Infelizmente o financiamento não foi aceito! \n O valor da prestação de R${:.2f} ultrapasa o limite de nossa base de cálculo.'.format(prest))