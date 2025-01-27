'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, motre uma mensagem dizendo que ele
foi multado.
A multa vai custar R$ 7,00 por cada KM acima do limite.'''

permitido = 80
velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > permitido:
    print('MULTADO! Voce excedeu o limite permitido que é de 80KM/h')
    multa = (velocidade - permitido) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
