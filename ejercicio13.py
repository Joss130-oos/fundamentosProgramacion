'''
Ejercicio 13:
  Programa que lea un número y muestre su raíz cuadrada y su raíz cúbica
Entradas:
  número: int
Salidas:
  raíz cuadrada
  raíz cúbica
'''
numero = input("Ingresar el número: ")
numero = int(numero)
raizcuadrada = (numero**0.5)
raizcubica = (numero**(1/3))
print("La raíz cuadrada es: ",raizcuadrada , "y la raíz cúbica es: ",raizcubica)