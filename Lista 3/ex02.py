#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n = float(input('Digite um número: '))

if n == 0:
    print('NULO!')
elif n > 0:
    print('POSITIVO!')
else:
    print('NEGATIVO!')
