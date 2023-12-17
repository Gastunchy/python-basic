# Ejercicio 1

'''
Hacer un programa que pida 2 numeros y que se de cuenta cula de ellos es par, o si ambos lo son
'''

numero_1 = int(input("Ingrese un numero entero: "))
numero_2 = int(input("Ingrese un numero entero: "))

if numero_1%2==0 and numero_2%2==0:
    print("Los dos numeros son pares")
elif numero_1%2==0 and numero_2%2!=0:
    print(f"{numero_1} es par")
elif numero_1%2!=0 and numero_2%2==0:
    print(f"{numero_2} es par")
else:
    print("Los dos son impares")
