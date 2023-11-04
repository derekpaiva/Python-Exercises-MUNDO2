from time import sleep

num = int(input('Digite um número inteiro qualquer: '))
sleep(2)

print('\n')

print('Escolha uma das bases para a conversão: \n[ 1 ] converte para BINÁRIO \n[ 2 ] converte para OCTAL \n[ 3 ] converte para HEXADECIMAL')

print('\n')

option = int(input('Escolha a sua opção: '))

print('\n')

if option == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else: print('Não existe base numérica com a opção digitada!')