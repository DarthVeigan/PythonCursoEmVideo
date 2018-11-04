"""

A QUANTIDADE DE UMA LETRA, A PRIMEIRA E A ÚLTIMA VEZ QUE APARECERAM NA FRASE!

"""

frase = str(input('Digite uma frase: ')).strip()

frase = frase.upper()

print('A quantidade de A é {} '.format(frase.count('A')))
print('A primeira vez que A apareceu foi: {} '.format(frase.find('A')+1))
print('A última vez que A apareceu foi: {} '.format(frase.rfind('A')+1))


'''
dividido = frase.split()
print(dividido)]
print(''.format(dividido[].count(['a'])))
'''



