#9 Faça um Programa que leia dois números inteiros e mostre o maior deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro número é maior que o segundo!')
elif n1 == n2:
    print('Os números são iguais!')
else:
    print('O segundo número é maior que o primeiro!')
