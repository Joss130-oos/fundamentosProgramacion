'''
Ejercicio 11:
  Programa que pida al usuario dos números y muestre la distancia entre ellos, en un valor absoluto de forma que el resultado siempre sea positivo
Entradas:
  Número mayor: int
  Número menor: int
Salidas:
  Distancia
'''
numeroa = input("Ingresar primer número: ")
numeroa = int(numeroa)
numerob = input("Ingresar segundo número: ")
numerob = int(numerob)
distancia = abs(numeroa - numerob)
print("Distancia: ",distancia)