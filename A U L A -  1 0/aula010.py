n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2

if(m<3):
    print('Você foi reprovado')
elif(m>3 or m<7):
    print('Você vai para final')
else:
    print('Você passou. Parabéns!!!')