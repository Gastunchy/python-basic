# Pilas or Stack
# https://www.youtube.com/watch?v=cXXO0qQGSPA&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=32

"""
Las pilas son estructuras de datos de tipo LIFO (Last In, First Out), ultimo en entrar, primero en salir.
En pyhton la estructura de dato tipo pila no existe como tal, pero se puede simular con una lista y los comandos:
(variable).append("elemento") para agregar un elemento al final de la lista
(variable).pop() para quitar el ultimo elemento agregado
"""

# Armamos una pila

pila_de_fila = [1, 2, 3, 4]
print("\n'Pila' original: ", pila_de_fila, "\n")

pila_de_fila.append(5)
print("Elemento nuevo '5'--> pila_de_fila.append(5)", pila_de_fila)

pila_de_fila.append(6)
print("Elemento nuevo '6'--> pila_de_fila.append(6)", pila_de_fila)

pila_de_fila.append(7)
print("Elemento nuevo '7'--> pila_de_fila.append(7)", pila_de_fila)

# Quitar elementos

print("\nPara quitar elementos se usa '(Variable).pop()'\n")

n = pila_de_fila.pop()  # Se muestra el elemento que se saca de la pila
print(pila_de_fila)
print(f"Elemento retirado: {n}")

n = pila_de_fila.pop()
print(pila_de_fila)
print(f"Elemento retirado: {n}")

n = pila_de_fila.pop()
print(pila_de_fila)
print(f"Elemento retirado: {n}")

n = pila_de_fila.pop()
print(pila_de_fila)
print(f"Elemento retirado: {n}")