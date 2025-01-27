#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Exemplo: Digite um número 1834, unidade 4, dezena 3, centena 8, milhar 1

num = str(input("Digite um número entre 0 e 9999: "))
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(num[3:]))
print('Dezena: {}'.format(num[2:3]))
print('Centena: {}'.format(num[1:2]))
print('Milhar: {}'.format(num[0:1]))

#essa formatação da errado, ver o arquivo cev23a.py