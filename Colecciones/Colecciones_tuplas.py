# Tuplas
# https://www.youtube.com/watch?v=PjCBukZttG4&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=27

"""
Las tuplas son similares a las listas, pero estas son inmutables, es decir que NO se pueden agregar, eliminar ni
modificar los elementos que ya contienen, las tuplas son mas rapidas en ejecucion y ocupan menos memoria

Las tuplas a diferencia de las listas, se crean con parentesis ()

Al igual que las listas, pueden contener distintos tipos de valores como numeros enteros y con decimales, letras,
palabras, listas, etc

Una tupla se puede convertir en una lista u viseversa
"""
tupla = ("hola", 1, 2, 3, 4, 5, 6, "hola", [4, 3, 2, 1])
print(tupla)

print("Se puede contar su contenido con 'len(tupla)': ", len(tupla))  # se puede contar su contenido
print("Se puede indicar el posicion a mostrar con 'tupla[1]': ", tupla[1])  # Se puede indicar el posicion a mostrar
print("Se puede indicar desde que posicion mostrar con 'tupla[3:]': ", tupla[3:])  # Se puede mostrar desde un posicion
print("Se puede indicar hasta que posicion mostrar con 'tupla[:3]': ", tupla[:3])  # Se puede mostrar hasta un posicion
print("En las tuplas tambien se puede buscar contenido con '(4 in tupla)': ", (4 in tupla))  # Se puede buscar
print("Se puede la posicion de un dato con '(tupla.index(5))' --> 5 esta en posicion 5: ", (tupla.index(5)))
print("Se puede contar la cantidad de veces que esta un valor con '(tupla.count('hola'))': ", (tupla.count("hola")))

# Convertir la tupla en lista
lista_desde_tupla = list(tupla)
print("\nSe puede convertir una tupla en lista con 'list(tupla)': ",  lista_desde_tupla)

# Convertir una lista en tupla

lista = [3, 5, 7, 9, "hola", "como", "estas"]
print("Contenido de una lista: ", lista)
print("Convertir de lista (anterior) a tupla con 'tuple(lista)': ", tuple(lista))
