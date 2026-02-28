# Lista 1-3
print('Exercício 3')
# base = float(input('Quanto mede a base do retângulo? '))
# altura = float(input('Quanto mede a altura do retângulo? '))
base, altura = map(float, input('Informe a base e a altura do retângulo: ').split())
print('Perímetro:', (2 * base) + (2 * altura))
print('Área:', base * altura)