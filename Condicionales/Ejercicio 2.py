# Ejercicio 3
''' Hacer un programa  que pida 3 numeros y determine cual es el mayor 3>2>1'''

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un numero: "))
num3 = float(input("Ingrese un numero: "))

if num1>=num2 and num1>=num3:
    print(f"El mayor numero es {num1:.2f}") # para tener resultado con dos decimales ":.2f"
elif num2>=num1 and num2>=num3:
    print(f"El mayor numero es {num2:.2f}") # para tener resultado con dos decimales ":.2f"
elif num3>=num1 and num3>=num2:
    print(f"El numero mayor es {num3:.2f}") # para tener resultado con dos decimales ":.2f"