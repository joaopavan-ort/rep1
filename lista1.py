# Lista 1-1
print('Exercício 1')
salarioM = float(input('Quanto é o seu salário? '))
print('Seu ganho anual é', salarioM * 12)
print('')

# Lista 1-2
print('Exercício 2')
n1 = float(input('Qual é sua nota 1? '))
n2 = float(input('Qual é sua nota 2? '))
n3 = float(input('Qual é sua nota 3? '))
n4 = float(input('Qual é sua nota 4? '))
media = (n1 + n2 + n3 + n4) / 4
print('Sua média final é', media)
print('')

# Lista 1-3
print('Exercício 3')
base = float(input('Quanto mede a base do retângulo? '))
altura = float(input('Quanto mede a altura do retângulo? '))
print('Perímetro:', (2 * base) + (2 * altura))
print('Área:', base * altura)

# Lista 1-4
print('Exercício 4')
N = int(input('Me diz um número de 1 a 10. '))
if N > 10:
    print('Precisa ser um número de 1 a 10')
    N = int(input('Me diz um número de 1 a 10, sem gracinhas dessa vez. '))
print('Tabuada do', N)
print(N, 'x 1 =', N * 1)
print(N, 'x 2 =',N * 2)
print(N, 'x 3 =',N * 3)
print(N, 'x 4 =',N * 4)
print(N, 'x 5 =',N * 5)
print(N, 'x 6 =',N * 6)
print(N, 'x 7 =',N * 7)
print(N, 'x 8 =',N * 8)
print(N, 'x 9 =',N * 9)
print(N, 'x 10 =',N * 10)