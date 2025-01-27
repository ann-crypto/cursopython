# Escreva um programa que leia os dias alugados e os km rodados e informe o valor total a pagar. Considerando o valor de 60 reais o dia e 15 centavos por km rodado

dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km o carro rodou? '))
valor = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(valor))
