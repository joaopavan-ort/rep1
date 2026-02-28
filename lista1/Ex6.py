# Lista 1-6
print('Exercício 6')
X = float(input('Escolha um valor para X: '))
Y = float(input('Agora escolha um valor para Y: '))
X, Y = map(float, input('Escolha 2 valores para X e Y ').split())
print('Agora vou invertê-los')
print('')
print('invertendo...')
X, Y = Y, X
print('Feito, agora X =', X, 'e Y =', Y)