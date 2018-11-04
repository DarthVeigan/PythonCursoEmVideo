"""

CÁLCULO DA HIPOTENUSA

"""

from math import hypot

co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa é {:.2f} '.format(hi))