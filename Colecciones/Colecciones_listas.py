# Colecciones - Listas

# https://www.youtube.com/watch?v=xdCJa2QXmJ8&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=25

"""
Las listas son parecidas a los arreglos o vectores en otros leguajes de programacion, en las listas podemos almacenar
valores tipo numericos, cadenas, valores booleanos se guardan entre corchetes y se separan por coma.

Una lista es una estructura de dato muy flexible

"""
variable = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40, 5.4, ["lista", "en", "lista"], False, True]

print("Ej toda la lista: ", variable)
print("Ej: variable[0]: ", variable[0])
'''Si a la valiable a imprimir le pongo entre corchetes el numero de un elemento de la lista, me muestra ese solo'''
print("Ej: variable[0:3]: ", variable[0:3])
print("Ej: variable[2:]: ", variable[2:])
print("Ej: variable[:4]: ", variable[:4])

# https://www.youtube.com/watch?v=aF1tiL5A-iU&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=26

lista = [5, "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40, 5.4, ["lista", "en", "lista"], False, 5, True]

lista.append(9)  # ingresa el numero nueve al final de la lista original
lista.append(input("ingrese algo a la lista: "))  # Permite que el usuario agregue algo al final de la lista
lista.insert(3, "Insert")  # Con insert agrega un valor y le tenemos que decir donde hay que agregarlo
lista.extend([5, 6, 7, 8])  # con extend, se extiende la lista con lo ingresado


print(lista)
print("Cantidad de elementos en 'lista' con 'len': ", len(lista))  # Len cuenta los elementos de una lista

print("El valor 3, esta en la lista?:", "3" in lista)  # Busca o "imprime" el numero 3 en la lista "lista"

print("Viernes, se encuentra en el lugar: ", lista.index("Viernes"))  # me dice en que indice/lubar de la lista esta la palabra "Viernes"

print("Cuantas veces esta el '5' en la lista: ", lista.count(5))

