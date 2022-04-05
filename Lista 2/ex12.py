#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal.
#Usando a seguinte fórmula: (72.7*altura)–58

altura = float(input('Para descobrir o seu peso ideal, digite a sua altura: '))

pesoIdeal = (72.7*altura) - 58

print('O seu peso ideal é: {:.2f} Kg'.format(pesoIdeal))
