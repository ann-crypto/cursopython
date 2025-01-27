#Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome separadamente.
#exemplo: ana maria de souza, primeiro = ana. ultimo = souza
nome = str(input('Qual o seu nome completo? ')).strip()
n = nome.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}.'.format(n[0]))
print('Seu último nome é {}.'.format(n[len(n)-1]))
