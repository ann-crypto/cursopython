from math import sqrt, ceil, floor
import random
import emoji

num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
raiz = sqrt(num)
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
#print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {}.'.format(num, ceil(raiz)))
print('A raiz de {} é igual a {}.'.format(num, floor(raiz)))
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))

numero = random.randint(1, 10)
print(numero)

print(emoji.emojize("Oi :sungalsses:", language='alias'))
