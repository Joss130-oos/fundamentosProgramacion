'''
Ejercicio 7:
  Programa que reciba una cantidad de minutos y los transforme en horas y minutos correspondientes
Entradas:
  minutos: int
Salidas:
  Horas: int
  Minutos: int
'''
minutos = input("Ingresa los minutos: ")
minutos = int(minutos)
horas = minutos//60
minutos = minutos % 60
print("Las horas y minutos son: ",horas , ":", minutos)