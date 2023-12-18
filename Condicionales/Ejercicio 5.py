# Ejercicio 5

"""
Hacer un programa que simule ser un cajero automatico con el saldo inicial de $1000 y tendra el siguiente menu de
opciones.

1- Ingresar dinero a la cuenta
2- Retirar dinero de la cuenta
3- Mostrar dinero disponible
4- Salir
"""
saldo = 1000

print("\t.:MENU:.")
print("1- Ingresar dinero a la cuenta")
print("2- Retirar dinero de la cuenta")
print("3- Mostrar dinero disponible")
print("4- Salir")

opcion = int(input("Seleccione una opcion: "))

print()

if opcion == 1:
    extra = float(input("Monto a ingresar -> "))
    saldo += extra
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 2:
    retiro = float(input("Cuando dinero quiere retirar -> "))
    if retiro > saldo:
        print(f"Fondos insuficiente")
    else:
        saldo -= retiro
        print(f"Dinero en la cuenta: {saldo}")
elif opcion == 3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 4:
    print("Gracias por usar nuestros servicios")
else:
    print("Ingreso una opcion invalida")