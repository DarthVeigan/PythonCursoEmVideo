print('-='*30)
print('\t\t\t\tAnalisador de triângulo')
print('-='*30)
a = int(input('Lado A tem: '))
b = int(input('lado B tem: '))
c = int(input('Lado C tem: '))

if(a < b+c and b < a+c and c < a+b ):
    print('Os segmentos acima podem formar um triângulo ')
else:
    print('Os segmentos não podem formar um triângulo')
