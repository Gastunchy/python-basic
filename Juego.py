"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje nombre tiene edad años, vive en dirección y su número de teléfono es
teléfono"""

info = {
    "Nombre": "",
    "Edad": "",
    "Direccion": "",
    "Telefono": "",
}

for i in info:
    dato = str(input("Cual es tu " + i + ":\t"))
    info[i] = dato

print(f"{info["Nombre"]} edad {info["Edad"]}, vive en {info["Direccion"]} y su número de teléfono es {info["Telefono"]}")

archivo = open("Diccionario.txt", "w")

archivo.write(str(info))

archivo.close()
