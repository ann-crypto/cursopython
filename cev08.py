# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

m = float(input('Digite um valor em metros: '))
cent = m * 100
mili = m * 1000
print('A medida de {}m corresponde a:\n{:.0f}cm\n{:.0f}mm'.format(m,cent,mili))
