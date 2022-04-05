#6 Realiza a leitura de 1 float referente ao salário do cidadão e apresenta o salário com reajuste de 10% da inflação.

salario = float(input('Digite o valor do seu salário atual para descobrir como ficará o seu novo com o reajuste de 10%: R$ '))

salarioNovo = salario*1.10

print('Com o reajuste de 10%, seu novo salário será de: R$', salarioNovo)
