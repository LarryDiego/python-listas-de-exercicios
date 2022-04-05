#1 Realiza a leitura de 2 floats e imprime as seguintes operações: soma, subtração, multiplicação, divisão e resto da divisão.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1/n2
restoDivisao = n1%n2

print('A soma entre {} e {} é {}'.format(n1, n2, soma))
print('A subtração entre {} e {} é {}'.format(n1, n2, subtracao))
print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicacao))
print('A divisão entre {} e {} é {:.2f}'.format(n1, n2, divisao))
print('O resto da divisão entre {} e {} é {}'.format(n1, n2, restoDivisao))
