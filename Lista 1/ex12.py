#12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos deve obedecer à tabela acima. Média Conceito:
# - Entre 9 e 10 A
# - Entre 7.5 e 9 B
# - Entre 6 e 7.5 C
# - Entre 4 e 6 D
# - Entre 0 e 4 E

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

print('Média:', media)

if media >= 9 and media <= 10:
  print('Conceito A')
elif media >= 7.5 and media < 9:
  print('Conceito B')
elif media >= 6 and media < 7.5:
  print('Conceito C')
elif media >= 4 and media < 6:
  print('Conceito D')
else:
  print('Conceito E')
