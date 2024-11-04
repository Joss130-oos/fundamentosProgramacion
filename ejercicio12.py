'''
Ejercicio 12:
  Programa que pida al usuario dos pares de números x1, y2 y x2, y2 que representen dos puntos en un plano, calculando la distancia entre ellos
Entradas:
  x1: int
  x2: int
  y2: int
Salidas: 
  Distancia
'''
x1 = input("Ingresar x1: ")
x1 = int(x1)
x2 = input("Ingresar x2: ")
x2 = int(x2)
y1 = input("Ingresar y1: ")
y1 = int(y1)
y2 = input("Ingresar y2: ")
y2 = int(y2)
distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
print("Distancia entre los puntos: ",distancia)