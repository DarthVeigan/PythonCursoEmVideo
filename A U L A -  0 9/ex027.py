"""

PRIMEIRO E ÚLTIMO NOME

"""

n = str(input('Digite o nome completo: '))

dividido = n.split()

print(dividido)
print('Seu primeiro nome é: {} '.format(dividido[0]))
print('Seu último nome é: {} '.format(dividido[len(dividido)-1]))