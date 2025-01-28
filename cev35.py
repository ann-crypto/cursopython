'''Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário
se elas podem ou não formar um triangulo'''

print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR triangulo')
else:
    print('os segmentos acima NÃO PODEM FORMAR triangulo')
