#Crie um programa que leia o nome completo de uma pessoa, e mostre:
#O nome com todas as letras maiusculas, todas minusculas, quantas letras ao todo sem considerar espaços
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
nse = nome.replace(' ','')
primeiro = nome.split()[0]

print('Analisando seu nome...'
      '\nSeu nome em maiúsculas é {}'
      '\nSeu nome em minúsculas é {}'
      '\nSeu nome tem ao todo {} letras'
      '\nSeu primeiro nome é {} e ele tem {} letras.'''.format(nome.upper(), nome.lower(), len(nse), primeiro, len(primeiro)))


'''print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))'''
'''print('Seu primeiro nome tem {} letras'.format(nome.find(' '))'''
'''separa = nome.split()'''
'''print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))'''
