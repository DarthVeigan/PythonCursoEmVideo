"""

LOCADORA DE VEÍCULOS

"""

d = int(input('Quantidade de dias: '))
km = float(input('Quantidade de KM rodados: '))


print('$'*40)
print('\nVocê alugou o carro por {} dias, valor a ser pago {} Reais'.format(d,d*60))
print('Você rodou {}km s, valor a ser pago {:0.2f} Reais'.format(km,km*0.15))
print('Valor total de ({}) dias  e ({:0.2f}) Kms rodados é igual a {:0.2f} Reais \n'.format(d,km,(d*60)+(km*0.15)))
print('$'*40)