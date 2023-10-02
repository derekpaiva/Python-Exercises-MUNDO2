n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

m = (n1 + n2)/2

if m < 5:
    print('Sua média é {} e você está \033[1;30;41mREPROVADO!\033[m'.format(m))
elif m >= 5 and m < 6.9:
    print('Sua média é {} e você está de \033[1;30;43mRECUPERAÇÃO!\033[m'.format(m))
else:
    print('Parabéns, sua média é {} e você está \033[1;30;42mAPROVADO!\033[m'.format(m))