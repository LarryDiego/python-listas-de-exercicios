#2 Realiza a leitura de 1 int e imprime o seu antecessor e o seu sucessor.

numero = int(input('Digite um número e descubra o seu antecessor e o seu sucessor: '))

antecessor = numero-1
sucessor = numero+1

print('Seu número:', numero)
print('Seu antecessor é {} e o seu sucessor é {}!'.format(antecessor, sucessor))
