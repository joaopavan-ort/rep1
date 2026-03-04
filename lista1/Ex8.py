# Lista 1-8
print('Exercício 8')
m = int(input('Informe um valor em reais, desconsiderando centavos: '))
c100 = m // 100
c50 = (m % 100) // 50
c20 = ((m % 100) % 50) // 20
c10 = (((m % 100) % 50) % 20) // 10
c05 = ((((m % 100) % 50) % 20) % 10) // 5
c02 = (((((m % 100) % 50) % 20) % 10) % 5) // 2
m01 = ((((((m % 100) % 50) % 20) % 10) % 5) % 2)
total = (c100 * 100) + (c50 * 50) + (c20 * 20) + (c10 * 10) + (c05 * 5) + (c02 * 2) + m01
print('100:', c100)
print('50:', c50)
print('20:', c20)
print('10:', c10)
print('5:', c05)
print('2:', c02) 
print('1:', m01)
print('Total: R$ {:.2f}'.format(total))
print('Nº de Notas Usadas:', c100 + c50 + c20 + c10 + c05 + c02 + m01)
