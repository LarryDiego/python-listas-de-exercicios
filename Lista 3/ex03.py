#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido.

sexo = str(input('Qual o seu sexo? (M/m para masculino e F/f para feminino) '))

if sexo == "M" or sexo == "m":
    print('MASCULINO')
elif sexo == "F" or sexo == "f":
    print('FEMININO')
else:
    print('SEXO INVÁLIDO')
