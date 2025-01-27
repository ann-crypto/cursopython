from random import randint
from time import sleep
'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

pc = randint(0, 5)
print('--='* 20)
print('Pensei em um número entre 0 e 5, você consegue adivinhar? ')
print('--='* 20)

num = int(input('Qual foi o número que eu escolhi? '))
print('PROCESSANDO...')
sleep(3)
if num == pc:
    print('PARABÉNS! Voce conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(pc, num))
