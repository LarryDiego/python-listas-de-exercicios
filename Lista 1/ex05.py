#5 Realiza a leitura de 1 float referente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%.

valor = float(input('Digite o valor do produto: R$ '))

desconto10 = valor*0.9
desconto20 = valor*0.8
desconto50 = valor*0.5

print('O produto com 10% de desconto fica: R$', desconto10)
print('O produto com 20% de desconto fica: R$', desconto20)
print('O produto com 50% de desconto fica: R$', desconto50)
