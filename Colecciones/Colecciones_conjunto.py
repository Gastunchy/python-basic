# Conjuntos
# https://www.youtube.com/watch?v=rmRrvol4XcM&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=28

"""
Los conjuntos son un tipo de coleccion donde se almacenan elementos, la particularidad de estos elementos es que:
- No puede ser otro tipo de coleccion ej. lista o tupla
- Se agregan de forma desordenada
- NO puede haber duplicados

Un conjunto se crea con dos comandos, esto se hace dado que los diccionarios y conjuntos se almacenan en llaves '{}'

nombre_de_variable = set() --> esto especifica que va a ser un conjunto
nombre_de_variable = {} --> crea el conjunto

"""
conjunto = set()

conjunto = {1, 2, 3, 4, 4, 6, 7, 3}

print("Contenido del conjunto 'conjunto = {1, 2, 3, 4, 4, 6, 7, 3}': ", conjunto)

conjunto.add(52)
print("\nSe pueden agregar elementos numero con 'conjunto.add(52)': ", conjunto)

conjunto.add("hola")
print("\nSe pueden agregar elementos letra/palabra con 'conjunto.add('hola')': ", conjunto)

conjunto.discard("hola")
print("\nSe pueden eliminar elementos con 'conjunto.discard(xxx) --> Elimine 'hola'': ", conjunto)

print("Se puede buscar un elemento con '(x in conjunto)' --> busque 3: ", 3 in conjunto)
print("Se puede consultar si un elemento NO esta '(x not in conjunto)' --> busque 540: ", 540 not in conjunto)

conjunto.clear()
print("Se puede borrar todo un conjunto con 'conjunto.clear()': ", conjunto)

# Conjuntos p2
# https://www.youtube.com/watch?v=UKD3CMINxik&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=29

"""
Un conjunto vacio comienza con set(), pero cuando creamos un conjunto que ya contenga elementos, la parte set() al 
inicio ya no es necesaria
"""
print("\n....: Comienza la parte 2 de conjuntos:....")
a = {1, 2, 3}
b = {3, 4, 5, 6}

print("Contenido del conjunto 'a': ", a)
print("Contenido del conjunto 'b': ", b)

print("Para hacer inmutable un conjunto se usa 'frozenset({'elementos'})")
print("Ver igualdad entre conjutno 'a == b' --> 'false' dado que no son iguales: ", a == b)
print("Cantidad de elementos de un conjunto con 'let(xx)': ", "a --> ", len(a), ", B --> ", len(b))
print("Union de conjuntos con '|'--> 'a | b': ", a | b, "(los valores repetidos no se repiten en la union, ej:3)")
print("Ver elementos en ambos conjuntos (interseccion) con & --> a & b: ", a & b, "(3 se repite en los dos)")
print("Ver la diferencia con '-' --> a - b: ", a - b, "(1 y 2 estan en 'a' pero no en 'b')")
print("Diferencia simetrica, descarta elementos que estan en ambos, '^' --> a ^ b: ", a ^ b, "(^ con: alt + 94)")
print("Subconjunto (uno dentro de otro) con --> 'a.issubset(b) --> 'a' esta en 'b')': ", a.issubset(b))
print("superconjunto (uno contiene a otro) con --> 'b.issuperset(a)' --> 'b' contiene a 'a': ", b.issuperset(a))
print("Disconeccion, no comparten elementos con --> a.isdisjoint(b): ", a.isdisjoint(b), "(False, comparte el '3')")
