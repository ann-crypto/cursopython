from math import trunc
# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.
# Exemplo: Digite um número: 6.127. O número digitado 6.1127 tem a parte inteira 6.

num = float(input("Digite un valor: "))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

'''num = float(input("Digite un valor: ")
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''