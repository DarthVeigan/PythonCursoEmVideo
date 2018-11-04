"""

SABER SE VOCÊ ESTÁ NO LIMITE. LIMITE MÁXIMO DE VELOCIDADE É 80 KM/H

"""

carro = float(input('Digite a velocidade do carro: '))

if(carro<80 and carro>0):
    print('Você está no limite ')
elif(carro<=0):
    print('ERROR')
else:
    print('Você está a {}km/h e será multado em {:.2f} reais '.format(carro,(carro-80)*7))