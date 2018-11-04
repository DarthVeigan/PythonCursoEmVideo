"""

SABER SE O NÚMERO É NEUTRO, PAR OU IMPAR!

"""

n = int(input('Digite um número: '))

if(n == 0 ):
    print('Neutro')
elif(n % 2 == 0):
    print('Número {} é par '.format(n))
elif(n % 2 == 1):
    print('Número {} é ímpar '.format(n))

