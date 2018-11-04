"""

UNIDADE, DEZENA E CENTENA!

"""

n = int(input('Digite um número de 0 a 9999: '))


U = n % 10 // 1
D = n % 100 // 10
C = n % 1000 // 100
M = n % 10000 // 1000

print('Unidade {} '.format(U))
print('Dezena {} '.format(D))
print('Centena {} '.format(C))
print('Milhar {} '.format(M))



