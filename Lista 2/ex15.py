#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu 
#salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
#programa que nos dê:
#- salário bruto.
#- quanto pagou de Imposto de Renda.
#- quanto pagou ao INSS.
#- quanto pagou ao sindicato.
#- o salário líquido.
#- calcule os descontos e o salário líquido, conforme a tabela à direita.

valorHora = float(input('Quanto você ganha por hora? R$ '))
horas = float(input('Número de horas trabalhadas: '))

bruto = valorHora * horas
impostoRenda = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
descontos = (impostoRenda + inss + sindicato)
liquido = bruto - descontos

print('Salário bruto: R$', bruto)
print('Imposto de Renda: R$', impostoRenda)
print('INSS: R$', inss)
print('Sindicato: R$', sindicato)
print('Total de descontos: R$', descontos)
print('Salário líquido: R$', liquido)
