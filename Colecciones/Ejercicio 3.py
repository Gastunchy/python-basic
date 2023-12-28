# Ejercicio 3

"""
Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos.

1-
Nombre: Aragon
Clase: Guerrero
Raza: Dunadan del Norte

2-
Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar

3-
Nombre: Gandalf
Clase: Mago
Raza: Istar
"""

personajes = []  # lista vacia

p = {
    "Nombre": "Aragon",
    "Clase": "Guerrero",
    "Raza": "Dúnadan del Norte"
}

personajes.append(p)  # Agregamos a la lista el personaje

p = {
    "Nombre": "Legolas",
    "Clase": "Arquero",
    "Raza": "Elfo Sindar"
}

personajes.append(p)

p = {
    "Nombre": "Gandalf",
    "Clase": "Mago",
    "Raza": "Instar"
}

personajes.append(p)

print(personajes)