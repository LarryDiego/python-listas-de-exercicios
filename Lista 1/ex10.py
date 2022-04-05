#10 Faça um programa que pede dois inteiros e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

n3 = n1
n1 = n2
n2 = n3

print('O primeiro número foi:', n1)
print('O segundo número foi:', n2)
