'''
Ejercicio 10:
  Programa que calcule la calificación final de un alumno de programación
Entradas:
  Parcial 1: int
  Parcial 2: int
  Parcial 3: int
  Calificación del examén final: int
  Calificación del trabajo final: int
Salidas:
  Calificación final
'''
parcial1 = input("Ingresar calificación del parcial 1: ")
parcial1 = int(parcial1)
parcial2 = input("Ingresar calificación del parcial 2: ")
parcial2 = int(parcial2)
parcial3 = input("Ingresar calificación del parcial 3: ")
parcial3 = int(parcial3)
examen = input("Ingresar calificación del examén final: ")
examen = int(examen)
trabajo = input("Ingresar calificación del trabajo final: ")
trabajo = int(trabajo)
promedio = (parcial1 + parcial2 + parcial3)/3
promediofinal = (promedio*55)/100
examenfinal = (examen*30)/100
trabajofinal = (trabajo*15)/100
calificacionfinal = (promediofinal + examenfinal + trabajofinal)
print("Calificación final: ",calificacionfinal)