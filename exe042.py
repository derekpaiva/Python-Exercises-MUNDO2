a = float(input('Digite o valor do tamanho do primeiro segmento: '))
b = float(input('Digite o valor do tamanho do segundo segmento: '))
c = float(input('Digite o valor do tamanho do terceiro segmento: '))

print('\n')

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos informados podem formar um triângulo.')
    
    if a == b and b == c:
        print('Os segmentos informados formam um triângulo \033[1;30;42mEQUILÁTERO\033[m.')
    elif a == b or a == c or b == c:  # Corrigi a condição aqui
        print('Os segmentos informados formam um triângulo \033[1;30;42mISÓSCELES\033[m.')
    else:
        print('Os segmentos informados formam um triângulo \033[1;30;42mESCALENO\033[m.')
else:
    print('Os segmentos informados não podem formar um triângulo.')
