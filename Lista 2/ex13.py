#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal.
#Utilize as seguintes fórmulas:
#Para homens: (72.7*h) –58
#Para mulheres: (62.1*h) -44.7

altura = float(input('Para descobrir o seu peso ideal, digite a sua altura(em metros): '))

pesoHomem = (72.7*altura)-58
pesoMulher = (62.1*altura)-44.7

print('Se o seu sexo é masculino, o seu peso ideal é: {:.2f} Kg, e se o seu sexo é feminino, o seu peso ideal é: {:.2f} Kg'.format(pesoHomem, pesoMulher))
