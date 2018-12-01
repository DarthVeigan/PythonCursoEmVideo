'''

AUMENTO DE SALÁRIO EM % 

'''

salario = float(input('Digite o valor do seu salário: '))

if(salario<=1250):
    print('15% de {:.2f} é {:.2f} Seu novo salário é {:.2f} '.format(salario,salario*0.15,salario+(salario*0.15)))
else:
    print('10% de {:.2f} é {:.2f} Seu novo salário é {:.2f} '.format(salario, salario * 0.1, salario + (salario * 0.1)))
