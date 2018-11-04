"""

LISTA NÃO ORDENADA

"""

from random import shuffle

a1 = str(input('Primeiro nome: ')).strip().upper()
a2 = str(input('Segundo nome: ')).strip().upper()
a3 = str(input('Terceiro nome: ')).strip().upper()
a4 = str(input('Quarto nome: ')).strip().upper()

lista = [ a1,a2,a3,a4 ]
shuffle(lista)

print('Ordem randômica é {} '.format(lista))


