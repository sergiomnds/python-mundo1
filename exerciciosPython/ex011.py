
#? Faça um programa que leia a largura e a altura de uma parede em metros,
#? calcule a sua área e a quantidade de tinta necessária para pintá-la,
#? sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = larg * alt
print('A área da parede é {:.2f}m² e será necessário {:.1f}L de tinta para pintá-la'.format(area, area/2))
