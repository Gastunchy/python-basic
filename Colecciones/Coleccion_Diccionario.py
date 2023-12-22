# Diccionario
# https://www.youtube.com/watch?v=vAy4IM7NLIQ&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=30

"""
Los diccionarios son otra coleccion de elementos y al igual que los conjuntos se ponen entre corchetes, pero
tienen dos elementos por posicion la clave y el valor "clave:valor" y no puede haber claves duplicadas.
un Diccionario tambien puede contener otras colecciones.
"""
diccionario = {"azul": "blue", "rojo": "red", "verde": "green"}

print("Diccionario completo: ", diccionario)
print("Para ver un elemento --> 'diccionario['clave']: ", diccionario["azul"], "<-- valor de la clave 'azul'")

diccionario["clave"] = "valor"
diccionario["azul"] = "BLUE"
print("Para agregar o modificar elementos se usa --> Diccionario['clave'] = 'valor': ", diccionario)
print("\t►En el anterior se agrego 'clave:valor' y se modifico 'blue a 'BLUE'")

gaston = {"lista": ["esto", "es", "lista"], "tupla": ("esto", "es", "tupla"), "Diccionario": {"edad": 40, "peso": 64}}
print("Se pueden agregar otras colecciones: ", gaston)
print(gaston)

ejemplo = {
    "Gaston": {
        "Edad": 40,
        "Peso": 64,
        "Altura": 1.66,
    },
    "Pablo": {
        "Edad": 35,
        "Peso": 53,
        "Altura": 1.56,

    }
}
print("Ejemplo de diccionario dentro de diccionario: ", ejemplo)
print("Datos de Gaston: ", ejemplo["Gaston"])
print("Dato de la altura de Gaston: ", ejemplo["Gaston"]["Altura"])

# Diccionario parte 2
# https://www.youtube.com/watch?v=hjNWsqLAPv4&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=31

print("\n Parte 2 de Diccionarios")
equipo = {
    10: "Dybala",
    11: "Douglas",
    7: "Ronaldo",
    17: "Farias"
}

print("Ver valor segun clave y respuesta si la clave no existe -> equipo.get(10,'No existe'): ", equipo.get(10, "No existe"))

print("Solo mostrar la clave con 'equipo.keys()': ", equipo.keys())
print("Solo mostrar el valor con 'equipo.values()': ", equipo.values())
print("Poner en tupla cada clave:valor con 'equipo.items': ", equipo.items())
print("Contar cuantas 'clave:valor' hay en el diccionario con 'len(equipo)': ", len(equipo))
print("Limpiar todo el equipo con 'equipo.clear': ", equipo.clear())

for i in equipo:
    print("Listado", i)

