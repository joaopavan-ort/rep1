# Lista 1-8
print('Exercício 8')
m = int(input('Informe um valor em reais, desconsiderando centavos: '))
c100 = m // 100
c50 = (m % 100) // 50
c20 = ((m % 100) % 50) // 20
c10 = (((m % 100) % 50) % 20) // 10
c5 = ((((m % 100) % 50) % 20) % 10) // 5
c2 = (((((m % 100) % 50) % 20) % 10) % 5) // 2
print('100:', c100)
print('50:', c50)
print('20:', c20)
print('10:', c10)
print('5:', c5)
print('2:', c2) 
print('Total:', (c100 * 100) + (c50 * 50) + (c20 * 20) + (c10 * 10) + (c5 * 5) + (c2 * 2))