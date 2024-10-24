'''
Ejercicio 9:
  Programa que calcule el 15% de descuento de la compra total de un cliente
Entradas:
  Precio
Salidas:
  Descuento
'''
precio = input("Ingresa el precio del producto: ")
precio = int(precio)
descuento = (precio*15)/100
total = (precio - descuento)
print("El precio es: ", total)