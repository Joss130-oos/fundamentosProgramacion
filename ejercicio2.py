'''
Programa 2:
  Crear un programa que calcule area y perimetro de un rectangulo
Entradas:
  base: integer
  altura: interger
Salidas:
  area: integer
  perimetro: integer
'''
base = input('Ingresa la base: ')
base = int(base)
altura = input('Ingresa la altura: ')
altura = int(altura)
area = base + altura
perimetro = (base + altura)/2
print("El area del rectangulo es", area)
print("El perimetro del rectangulo es", perimetro)