# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(n, d, n, t, n, r))
print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*2), n, (n*3), n, (pow(n, (1/2)))))

