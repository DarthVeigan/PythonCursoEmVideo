"""

CONVERSOR DE TEMPERATURAS ºC E ºF

"""

c = float(input('Informe a temperatura em ºC: '))
f = float(input('Informe a temperatura em ºF: '))
Tc = (f-32)/1.8
Tf = (c*1.8)+32

print('A temperatura de {:.2f}ºC Corresponde a {:.2f}ºF '.format(c,Tf))
print('A temperatura de {:.2f}ºF Corresponde a {:.2f}ºC'.format(f,Tc))

#ºC->ºF = ((9*c)/5)+32
#ºF->ºC = ((