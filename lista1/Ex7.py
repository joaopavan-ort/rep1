# Lista 1-7
print('Exercício 7')
tempo = input('Que horas são? [00:00] ')
hora = int(tempo[0:2])
minuto = int(tempo[3:5])
print('')
print('Horas:', hora)
print('Minutos:', minuto)
print('Se passaram', (hora * 60) + minuto, 'minutos desde o início do dia.')