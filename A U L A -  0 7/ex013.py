"""

PORCENTAGEM DE AUMENTO DE SALÁRIO

"""

salario = float(input('Digite seu salário R$ = '))

aumento = 15
print('Seu salário teve aumento de {}% '.format(aumento))
print('{}% é igual a {:.2f} Reais'.format(aumento,salario*0.15))
print('Seu novo salário é igual a: {:.2f} Reais'.format(salario+salario*0.15))