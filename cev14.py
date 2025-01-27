# Faça um programa que leia a temperadura em graus celsius e converta em fahrenheit

c = float(input('Informe a temperatura em ºC: '))
f = (c * 9/5) + 32
print('A temperadura {:.1f}ºC corresponde a {:.1f}ºF'.format(c, f))
