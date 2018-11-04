"""

TABUADA DE algum número soliciador 

"""

n1 = int(input('Tabuada de qual número: '))
mult = 1

for mult in range(10):
print('{} x {} é igual a {} '.format(n1,mult,(n1*mult)))