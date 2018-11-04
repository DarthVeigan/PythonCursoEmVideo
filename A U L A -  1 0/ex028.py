"""

JOGAR COM A MÁQUINA 

"""

from random import randint
pc = randint(1,5)
pessoa = int(input('Digite um número de 1 a 5: '))

if (pessoa<1 or pessoa>5):
    print('Digite um número válido. Válido de 1 a 5 ')

else:
    print('\nColetando dados... \n')
    print('Você escolheu {} e a máquina sorteou {} '.format(pessoa,pc))
    print('\nResultado: ')

if ( pessoa == pc ):
    print('Você ganhou! \n')
    

elif(pessoa != pc and pessoa>0 and pessoa<6):
    print('Você perdeu! \n'
