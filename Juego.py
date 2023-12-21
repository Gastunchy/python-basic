with open("mitupla.txt", "r") as original:

    dato = original.readline()

dato = list(dato)

while True:
    print("\n.:Menu:.")
    print("1 - Ingresar palabra")
    print("2 - Ingresar numero")
    print("3 - Ver los datos")
    print("4 - finalizar app")

    seleccion = int(input("Ingrese una opcion: "))

    if seleccion == 1:
        dato.append(str(input("Ingrese una palabra: ")))
    elif seleccion == 2:
        dato.append(float(input("Ingrese un numero: ")))
    elif seleccion == 3:
        print(dato)
    elif seleccion == 4:
        dato_str = str(dato)
        with open("mitupla.txt", "w") as archivo:
            archivo.write(dato_str)
            print("Fin de app")
            break
