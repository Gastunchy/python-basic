# Colas
# https://www.youtube.com/watch?v=wuGYzEcgTTw&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=33

"""
Al igual que las pilas son estructura de datos que no existen como tan en python pero se pueden simular con listas.
Las colas son estructuras de tipo FIFO (Fist in, First out), el primero en entrar es el primero en salir
y para ello se utilizan los siguientes comandos:
Agregar elementos
(variable).append('Elemento')

Quitar elemento desde el principio

(variable).pop(0) --> quita un elemento que esta en la posicion 0 del indice

"""
cola = ["Marta", "Maria", "Jose", "Juan"]

print("Cola original: ", cola, '\n')

# Agregar elementos a la cola
print("Agregar elementos a la cola con variable.append('elemento'):\n")
cola.append("Gaston")
print("Se agrego 'Gaston' a la cola: ", cola, "\n")

cola.append("Gustavo")
print("Se agrego 'Gustavo' a la cola: ", cola, "\n")

# Quitar elementos desde el principio
print("Quitar elementos desde el principio con variable.pop(0) -> cero es el principio del indice/orden:\n")
print(f"Cola original: {cola}")
n = cola.pop(0)
print(f"Se quito '{n}' de la cola")
print(cola)
print("-")

print(f"Cola original: {cola}")
n = cola.pop(0)
print(f"Se quito '{n}' de la cola")
print(cola)
print("-")

print(f"Cola original: {cola}")
n = cola.pop(0)
print(f"Se quito '{n}' de la cola")
print(cola)
