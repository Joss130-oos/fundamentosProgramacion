'''
Ejercicio 15:
  Programa que intercambie los valores de ambas variables y muestre cuanto valen al final las 2 variables
Entradas:
  NúmeroA: int
  NúmeroB: int
Salidas:
  NúmeroC
  NúmeroB
'''
n1 = input("Escribe un número: ")
n1 = int(n1)
n2 = input("Escribe un número: ")
n2 = int(n2)
nX = n1
n1 = n2
n2 = nX
nf = "La variable final es: ", n1, "y", n2
print(nf)