from random import randint

n1 = randint(1,9999)
n2 = randint(1,9999)
n3 = randint(1,9999)

print('='*36)
print('n1 = {}\nn2 = {}\nn3 = {} '.format(n1,n2,n3))

if(n1 > n2 > n3):
    print('{} é o Maior número '.format(n1))
    print('{} é o Menor número '.format(n3))
elif(n1 > n3 > n2):
    print('{} é o Maior número '.format(n1))
    print('{} é o Menor número '.format(n2))

elif(n2 > n1 > n3):
    print('{} é o Maior número '.format(n2))
    print('{} é o Menor número '.format(n3))
elif(n2 > n3 > n1):
    print('{} é o Maior número '.format(n2))
    print('{} é o Menor número '.format(n1))

elif(n3 > n1 > n2):
    print('{} é o Maior número '.format(n3))
    print('{} é o Menor número '.format(n2))
elif(n3 > n2 > n1):
    print('{} é o Maior número '.format(n3))
    print('{} é o Menor número '.format(n2))

elif(n1 == n2 == n3):
    print('Números íguais ')

elif(n1 > n2 == n3 ):
    print('{} é o Maior número '.format(n1))
    print('{} e {} são iguais '.format(n2,n3))

elif(n2 > n1 == n3 ):
    print('{} é o Maior número '.format(n2))
    print('{} e {} são iguais '.format(n1,n3))

elif(n3 > n1 == n2 ):
    print('{} é o Maior número '.format(n3))
    print('{} e {} são iguais '.format(n1,n2))
