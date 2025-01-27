from math import sin, cos, tan, radians

# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

a = float(input('Digite o angulo que voce deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O angulo de {} tem o SENO de {:.2f}'
      '\nO angulo de {} tem o COSSENO de {:.2f}'
      '\nO angulo de {} tem a TANGENTE de {:.2f}'.format(a, s, a, c, a, t))
