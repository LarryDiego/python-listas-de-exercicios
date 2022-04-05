#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

from re import L


lado = float(input('Quanto mede o lado do quadrado? '))

area = lado*lado
dobro = area*2

print('O quadrado tem área de {}, e o dobro dessa área é {}'.format(area, dobro))
