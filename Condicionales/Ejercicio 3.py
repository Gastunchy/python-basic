# Ejercicio 3

'''
Hacer un programa que pida un caracter e indique si es una vocal o no
a - e - i - o - u
'''

letra = str(input("Ingrese una letra: ").lower())
'''.lower transforma todo en minuscula, tambien se puede usar .upper'''

if letra=='a'or letra=='e'or letra=='i'or letra=='o'or letra=='u':
    print(f"{letra} -> es una vocal")
else:
        print(f"{letra} -> no es una vocal")
