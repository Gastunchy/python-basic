# Ejercicio 2

"""
Escriba un programa que tenga dos listas y que, a continuacion, cree las siguientes listas (en las que no debe haber
repeticiones)

- Lista de palabras que aparecen en las dos listas
- Lista de palabras que aparecen en la primera lista, pero no en la segunta
- Lista de palabras que aparecen en la segunda lista, pero no en la primera
- Lista de palabras que aparecen en ambas listas

"""

lista1 = ["marta", "maria", "federico", "samuel", "nancy"]

lista2 = ["gustavo", "manuel", "maria", "samuel", "federico"]

print(f"Lista 1: {lista1}\nLista 2: {lista2}")

lista1 = set(lista1)
lista2 = set(lista2)

print(f"Las listas se convierten en conjuntos para validar:\n\t'Lista 1': {lista1}\n\t'Lista 2': {lista2}")

print(f"Elementos en las dos listas: {list(lista1 | lista2)}")
print(f"Estan en 1 pero no en 2: {list(lista1 - lista2)}")
print(f"Estan en 2 pero no en 1: {list(lista2 - lista1)}")
print(f"Estan en las dos: {list(lista2 & lista1)}")
