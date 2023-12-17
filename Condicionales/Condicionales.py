# Condicionales
'''
Estas sentencias se usan para comparar dos valores y esa comparacion da un resultado, verdadero (true) o falso (false), si una determinada condicion se cumple se van a ejecutar un determinado numero de acciones y si no, puede que se ejecuten otras o no se ejecute nada
'''

#Ejemplo de condicionales dobles if (si) else (de lo contrario) y elif (de lo contrario al if se pone entre if y else)

numero = int(input("Ingrese numero: "))

if numero>0: # siempre se finaliza con :
    print(f"El numero {numero} es positivo")
elif numero==0:
    print("El numero es igual a cero")
else:
    print(f"El numero {numero} es un numero negativo")

print("Fin del analisis")

# aca le pusimos testeo
