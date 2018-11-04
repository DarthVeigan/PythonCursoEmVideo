"""

SENO, COSSENO E TANGENTE

"""

from math import radians,cos,sin,tan

ângulo = float(input('Digite o ângulo desejado: '))

seno = sin(radians(ângulo))
print('O seno do ângulo {:.2f} é {:.2f} '.format(ângulo,seno))
cosseno = cos(radians(ângulo))
print('O cosseno do ângulo {:.2f} é {:.2f} '.format(ângulo,cosseno))
tangente = tan(radians(ângulo))
print('A tangente do ângulo {:.2f} é {:.2f} '.format(ângulo,tangente))
