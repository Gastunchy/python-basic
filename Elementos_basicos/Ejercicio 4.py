# https://www.youtube.com/watch?v=xCqX_BnjSNc&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=16

import math

radio = float(input("Ingresar el valor del radio: "))

area = math.pi * radio**2
longitud =2* math.pi *radio

print(f"El area es: {area:.3f}") # el :.3f me dice que me va a devolver 3 decimales
print(f"La longitud es: {longitud:.2f}")
