# Ejercicio 1
# https://www.youtube.com/watch?v=Nl_CxwKaZJk&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=34

"""
Escriba un programa donde tenga una lista y que, a continuacion, elimine elementos repetidos, por ultimo mostrar la
lista.
"""

lista = [1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 8, 9, 10, 11, 12]

print(lista)

# Al convertir la lista en un conjunto, se elimina los repetidos ya que en los conjuntos no puede haber repetidos

nueva_lista_en_conjunto = set(lista)

nueva_lista = list(nueva_lista_en_conjunto)

print(nueva_lista)

# o tambien se puede hacer simplificado

lista =list(set(lista))

print(lista)