"""

PORÇÃO INTEIRA 

"""

from math import trunc

num = float(input('Digite um número: '))
print('A porção inteira de {} é {} '.format(num,trunc(num)))

''' ou 
num = float(input('Digite um número: '))
print('A porção inteira de {} é {} '.format(num,int(num))
'''