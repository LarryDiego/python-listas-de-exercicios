#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

valor = float(input('Quanto você ganha por hora? R$ '))
horas = int(input('Quantas horas por mês você trabalha? '))

total = valor*horas

print('Nesse mês você ganhou: R$', total)
