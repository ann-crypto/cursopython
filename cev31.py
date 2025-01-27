'''Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem,
cobrando R$ 0,50 por KM para viagens até 200km e R$ 0.45 para viagens mais longas.'''

dist = float(input('Qual é a distância da sua viagem? '))
if dist <= 200:
    print('Você está prestes a começar uma viagem de {}Km.'.format(dist))
    print('E o preço da sua passagem será de R$ {:.2f}'.format(dist*0.5))
else:
    print('Você está prester a começar uma viagem de {}Km.'.format(dist))
    print('E o preço da sua passagem será de R$ {:.2f}'.format(dist*0.45))
