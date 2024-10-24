'''
Ejercicio 8:
  Programa que calcule el sueldo de un vendedor por obtener el 10% extra de comisión de venta en un mes por tres ventas
Entradas:
  Sueldo: int
  Variable1: int
  Variable2: int
  Variable3: int
Salidas:
  Dinero ganado por mes
'''
variable1 = input("Ingresar venta: ")
variable1 = int(variable1)
variable2 = input("Ingresar venta: ")
variable2 = int(variable2)
variable3 = input("Ingresar venta: ")
variable3 = int(variable3)
sueldo = input("Ingresar sueldo: ")
sueldo = int(sueldo)
v1 = (variable1*10)/100
v2 = (variable2*10)/100
v3 = (variable3*10)/100
dinero = (sueldo + v1 + v2 + v3)
print("Tu sueldo es", dinero , "pesos")