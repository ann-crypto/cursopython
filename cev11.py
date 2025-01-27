# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m².

larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
area = larg * altu
tint = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².\n'
      'Para pintar essa parede, você precisará de {}l de tinta.'.format(larg, altu, area, tint))
