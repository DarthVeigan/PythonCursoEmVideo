import emoji
print(emoji.emojize('Olá, Mundo :earth_americas:',use_aliases=True))


import math
from math import sqrt,floor,ceil
num = float(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} pra baixo é {:.2f} '.format(num,floor(raiz)))
print('A raiz quadrada de {} pra cima é {:.2f} '.format(num,ceil(raiz)))

import random
print('\n')
numR = random.randint(1,2)
print(numR)

nlista = random.randrange(1,4)
print('{}'.format(nlista))

