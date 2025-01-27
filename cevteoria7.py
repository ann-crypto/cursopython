nome = input('Qual o seu nome? ')
print ('Olá {:20}!'.format(nome))
print ('Olá {:>20}!'.format(nome))
print ('Olá {:<20}!'.format(nome))
print ('Olá {:^20}!'.format(nome))
print ('Olá {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print ('A soma vale {}'.format(n1+n2))

n3 = int(input('Digite um valor: '))
n4 = int(input('Digite outro valor: '))
s = n3 + n4
m = n3 * n4
d = n3 / n4
di = n3 // n4
e = n3 ** n4
print('A soma é {},\n o produto é {}\n e a divisão é {:.3f} '.format(s,m,d), end=' ')
print('Divisão inteira {} e potência {}'.format(di,e))
