from random import choice
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dles e escrevendo o nome do escolhido.

primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
