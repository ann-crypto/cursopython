# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. considere 1 dolar a 3.27

real = float(input('Quantos reais você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))