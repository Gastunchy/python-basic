# Ejercicio 4

""" Construir un programa que simule el funcionamiento de una calculadora que pueda realizar las 4 operaciones
aritmeticas basicas (suma, resta, multiplicacion y division). El usuario debe especificar la operacion con el primer
caracter del nombre de la operacion."""

num1 = float(input("Ingrese el 1er numero: "))
num2 = float(input("Ingrese el 2do numero: "))

operacion = (input("Operacion"
                   "\n- S, s=suma"
                   "\n- R, r=resta"
                   "\n- M, m, P, p=multiplicacion"
                   "\n- D, d=division"
                   "\n: ")).upper()  # upper convierte lo que ponga el usuario en mayuscula

resultado = "Resultado: "

if operacion == "S":
    suma = num1 + num2
    print(f"{resultado}{suma:.2f}")
elif operacion == "R":
    resta = num1 - num2
    print(f"{resultado}{resta:.2f}")
elif operacion == "M" or operacion == "P":
    multi = num1 * num2
    print(f"{resultado}{multi:.2f}")
elif operacion == "D":
    div = num1 / num2
    print(f"{resultado}{div:.2f}")
else:
    print("\n- Se equivocó de operación -")
