from time import sleep

print('Seja bem-vindo ao Caixa de Pagamentos! \n')
sleep(2)

print('\033[1;30;43m Possuímos as seguintes formas de pagamento:\033[m \n')
sleep(2)

print('1 - Dinheiro/Cheque/Pix \n2 - Cartão à Vista \n3 - Até 2x no Cartão \n4 - 3x ou mais no cartão \n')

valor = float(input('Qual é o valor do produto que deseja comprar? '))
pg = int(input('Digite a forma de pagamento: '))

v1 = valor*0.9 #valor do produto pagando à vista no dinheiro/cheque/pix
v2 = valor*0.95 #valor do produto pagando à vista no cartão
v3 = valor #valor do produto parcelando em até 2x no cartão
v4 = valor*1.2 #valor do produto parcelando em 3x ou mais no cartão

if pg == 1:
    print('O método escolhido foi \033[1;30;42mDinheiro/Cheque/Pix\033[m, assim o valor fica R${:.2f}'.format(v1))
elif pg == 2:
    print('O método escolhido foi \033[1;30;42mÀ Vista no Cartão\033[m, assim o valor fica R${:.2f}'.format(v2))
elif pg == 3:
    print('O método escolhido foi \033[1;30;42mEm Até 2x No Cartão\033[m, assim o valor fica R${:.2f}'.format(v3))
else:
    print('O método escolhido foi \033[1;30;42m3x ou Mais No Cartão\033[m, assim o valor fica R${:.2f}'.format(v4))