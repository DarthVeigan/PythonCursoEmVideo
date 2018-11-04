viagem = float(input('Digite a quantidade de KMs da sua viagem: '))

if(viagem<=0):
    print('ERROR')
elif(viagem>=1 or viagem<=200):
    print('Você viajou {} Kms e gastou {:.2f} reais '.format(viagem,(viagem*0.5)))
elif(viagem>200 ):
    print('Você viajou {} Kms e gastou {:.2f} reais '.format(viagem,viagem*0.45))