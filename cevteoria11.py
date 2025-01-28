print('\033[7;30mOlá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{} \033[me \033[31m{} \033[m'.format(a, b))

nome = 'Annessa'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[36m', nome, '\033[m'))

nome1 = 'Siqueira'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome1, cores['limpa']))
