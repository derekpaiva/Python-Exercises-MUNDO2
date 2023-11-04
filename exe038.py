a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

if a>b:
    print('O primeiro número digitado [ {} ] é o maior.'.format(a))
elif b>a:
    print('O segundo número digitado [ {} ] é o maior.'.format(b))
else:
    print('Não existe valor maior, os dois são iguais.')