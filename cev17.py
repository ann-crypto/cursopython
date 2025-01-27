from math import hypot
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
'''hi = (co ** 2 + ca ** 2) ** (1/2)'''
'''hi = hypot(co, ca)'''

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))
