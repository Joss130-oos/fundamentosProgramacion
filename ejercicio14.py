'''
Ejercicio 14:
  Programa que invierta las posición de 2 cifras de un número de 2 digitos
Entradas:
  número: int
Salidas:
  Número invertido
'''
numero = input("Ingresa el número: ")
numero = int(numero)
dec = numero // 10
uni = numero % 10
ninv = (uni * 10) + dec
print("El número invertido sera: ",ninv)