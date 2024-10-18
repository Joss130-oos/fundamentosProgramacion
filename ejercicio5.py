'''
Ejercicio 5:
  Programa que transforma los grados Farenheit a grados celsius
Entradas:
  grados Farenheit: int
Salidas:
  grados Celcius
'''
gradosf = input("Ingresa el grado f: ")
gradosf = int(gradosf)
gradosc = (gradosf-32)/1.8
print("El grados celcius es: ",gradosc)