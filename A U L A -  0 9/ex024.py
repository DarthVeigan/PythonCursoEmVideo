"""

COMPARAR SE A CIDADE COMEÇA COM A LETRA DESEJADA

"""

cidade = str(input('Nome da cidade: ')).strip()

cidade = cidade.upper()
div = cidade.split()

print('A cidade que você nasceu começa com C de caruaru? {} '.format('C' in cidade))
print('Analisando...')
print('Começa com CARUARU? {} '.format(div[0] == 'CARUARU'))
'''
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
'''