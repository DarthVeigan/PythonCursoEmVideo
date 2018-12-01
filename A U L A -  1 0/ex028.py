"""

JOGAR COM A MÁQUINA 

"""

"""

JOGAR COM A MÁQUINA 

"""

from random import randint

print('\n$$$$$$$$$$$$$$$$$ B E M - V I N D O $$$$$$$$$$$$$$$$$')
print('$ Estou pensando em um número. Pode variar de 1 a 5 $')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
pc = randint (1,5)

pessoa = int(input('Em que número estou pensando? '))

print('\nAnalisando dados... Opa, pera lá. Muita calma ladrão! ')

if(pessoa<1 or pessoa>5):
    print('\nTic-Tac ainda é 09:40 o relógio na cadeia anda em câmera lenta! \n')
else:
    print('\nJesus Chorou!')
if(pessoa == pc):
    print('\nO guina foi e deu mais 3\n')

elif(pessoa != pc and pessoa>0 and pessoa<6):
    print('FIIIIIIU. SUMIU, ENTREI PELO SEU RÁDIO, CÊ NEM VIU! \n')
