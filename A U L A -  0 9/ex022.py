"""

    MAIÚSCULAS, MINÚSCULAS 
    CARACTERES
    PRIMEIRO NOME, ÚLTIMO NOME
    TOTAL PRIMEIRO E ÚLTIMO NOME
    TEM O NOME? 
    LETRA APARECEU X VEZES, A PRIMEIRA LETRA APARECEU X VEZES, A ÚLTIMA LETRA APARECEU X VEZES
    
    len começa com 1 e split começa com 0 

"""

nome = str(input('Digite seu nome: ')).strip()
nome = nome.upper().strip()
div = nome.split()

#----------------------------------------------------------------------------------------------------------
print('MAIÚSCULA: {} '.format(nome.upper()))
print('minúscula: {} '.format(nome.lower()))
#----------------------------------------------------------------------------------------------------------
print('Total caracteres {} '.format(len(nome)-nome.count(' ')))
print('Primeiro nome: {} '.format(div[0]))
print('Último nome: {} '.format(div[len(div)-1]))
#----------------------------------------------------------------------------------------------------------
print('Total primeiro nome {} '.format(len(div[0])))
print('Total último nome {} '.format(len(div[len(div)-1])))
#----------------------------------------------------------------------------------------------------------
print('Seu nome tem Oliveira ? {} '.format('OLIVEIRA' in nome ))
#----------------------------------------------------------------------------------------------------------
print('Letra A apareceu {} '.format(nome.count('A')))
print('Letra A aparece primeiro na posição {} '.format((nome.find('A')+1)))
print('Letra A apareceu por último na posição {} '.format((nome.rfind('A')+1)-(nome.count(' '))))
#----------------------------------------------------------------------------------------------------------

















#nome = 'thyago oliveira nunes'
#print(dividido[0]) #mostrando o nome na lista 0
#print(dividido[0].count(''))
#nome[0]=t  =!=  dividido[0]=thyago
#print('Nome separado em listas fica \n {} '.format(nome.split())) #quebrou o nome completo em 3 listas
#dividido = nome.split() #atribui o nome.split a variável dividido