# Condicionales combinados

# ejemplo simpre

edad = int(input("Ingrese su edad: "))

if edad>0 and edad<100: #tambien se puede resumir con "0<edad<=100"
    #print("Edad correcta")
    if edad >=18:
        print("Usted es mayor de edad.")
    else:
        print("Usted es menor de edad.")
else:
    print("Edad incorrecta")

'''
Dado que en el ejemplo anterior se pueden poner numeros en negativo o edades muy grandes como 120 y como sabemos un numero negativo no puede ser una 
edad y hasta donde se sabe, nadie llego a 150 años y este "error" tiene solucion con una condicion anidada, se agrego un
if dentro de un if y un and en la calidacion
'''


