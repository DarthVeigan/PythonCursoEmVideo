"""

CONHECENDO ALGUMAS FUNÇÕES BOOLEAN

"""

e = (input('Digite algo: '))
print('O tipo primtivo desse valor é {}'.format(type(e)))

print('Só tem espaço?',e.isspace())
print('É um número? ',e.isnumeric())
print('É alfabético? ',e.isalpha())
print('É alfanumérico? ',e.isalnum())
print('Está em maiúsculo? ',e.isupper())
print('Está em minúsculo? ',e.islower())
print('Está capitalizada? ',e.istitle())


n = (input('Digite algo: '))
print(type(n))
b = bool(input('Digite algo: '))
print(b)

#Métodos de testes para tipos