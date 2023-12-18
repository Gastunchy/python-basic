# Lista Eliminar elementos
# https://www.youtube.com/watch?v=aF1tiL5A-iU&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=26
# Para eliminar elementos de la lista existen varias funciones

lis_elim = [1, 2, 3, 4, 5, "Verde", False, True]

print("Lista completa: ", lis_elim)

lis_elim.pop()  # pop cuando esta vacio, elimina el ultimo elemento

print("Se elimino el ultimo elemento con 'lis_elim.pop()': ", lis_elim)

lis_elim.pop(3)  # Eliminar el elemento del indice 3

print("Se elimino el ultimo elemento del indice '3' con 'lis_elim.pop(3)', el 4 ya no está: ", lis_elim)

lis_elim.remove("Verde")

print("Se elimino 'Verde' usando 'lis_elim.remove('Verde')': ", lis_elim)

lis_elim.clear()  # Elimina todos los elementos de la lista

print("Eliminar todos los elementos de la lista con 'lis_elim.clear()': ", lis_elim)

# Otras opciones
print("\nOtras funciones que se pueden hacer con la lista: \n")

Testeo = [1, 620, 3, 54, 5, 63, 3, 8]
print("Original: ", Testeo, "\n")
Testeo.reverse()  # Invierte el order "de atras para adelante"

print("Cambiar el orden de los elementos con 'Testeo.reverse()': ", Testeo)

Testeo.sort()
print("Ordena la lista ascendentemente con 'Testeo.sort()': ", Testeo)

Testeo.sort(reverse=True)
print("Ordena la lista descendentemente con 'Testeo.sort(reverse=True)': ", Testeo)
