#11 As Organizações Hamurabi Medeiros resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5%

salario = float(input('Qual o seu salário? R$ '))

if salario <= 280:
  aumento20 = salario*0.2
  aumento20Novo = salario*1.2
  print('Antigo salário: R$ {}. Novo salário com aumento de R$ {}(20%) será de R$ {}'.format(salario, aumento20, aumento20Novo))
elif salario > 280 and salario <= 700:
  aumento15 = salario*0.15
  aumento15Novo = salario*1.15
  print('Antigo salário: R$ {}. Novo salário com aumento de R$ {}(15%) será de R$ {}'.format(salario, aumento15, aumento15Novo))
elif salario > 700 and salario < 1500:
  aumento15 = salario*0.1
  aumento15Novo = salario*1.1
  print('Antigo salário: R$ {}. Novo salário com aumento de R$ {}(10%) será de R$ {}'.format(salario, aumento15, aumento15Novo))
else:
  aumento5 = salario*0.05
  aumento5Novo = salario*1.05
  print('Antigo salário: R$ {}. Novo salário com aumento de R$ {}(5%) será de R$ {}'.format(salario, aumento5, aumento5Novo))
