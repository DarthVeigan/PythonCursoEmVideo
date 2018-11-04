frase = 'Curso Em Vídeo Python'
print(frase.replace('Python','Android'))

'''
|c|u|r|s|o| |e|m| |v|í|d|e|o| |p|y|t|h|o|n|
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 
'''
#fatiamento
print(frase[9])
print(frase[9:21]) #
print(frase[9:21:2]) #x:y:z z = pular de 2 em 2
print(frase[:5]) #começa no 0 e termina no 5
print(frase[15:]) #começa no 15 e termina no último
print(frase[9::3]) #começa no 9, vai até o último e pula de 3 em 3

#análise
print(len(frase)) #comprimento da frase
print(frase.count('o')) #contador do alfabeto
print(frase.count('o',0,13)) #fatiamento
print(frase.find('deo')) #diz onde encontrou e começou
print(frase.find('Android')) #retorna -1 não foi encontrado na string frase
print('curso'in frase) #busca palavra na string e retorna true or false

#transformação
print(frase.replace('Python','Android'))
print(frase)
print(frase.upper()) # Oque está em minúsculo fica maiúsculo
print(frase.lower()) # Oque está em maiúsculo fica em minúsculo
print(frase.capitalize()) #joga tudo para minúsculo e deixa o primeiro em maiúsculo
print(frase.title()) #primeiro caractere de cada palavra fica em maiúsculo
print(frase.strip()) #apaga espaços em branco no começo e no final da string
print(frase.rstrip()) #apaga espaços em branco no final da string a direita
print(frase.lstrip()) #apaga espaços em branco no começo da string a esquerda

#divisão
print(frase.split()) #cada palavra recebe indexação nova, são string's colocadas dentro de uma lista e essa listas terão numeração
dividido = frase.split()
print(dividido[2])
print(dividido[2][3])

#junção
print(''.join(frase))