# Operacion aritmetica
'''
Prioridad de operaciones de aritmetica
1- Parentesis
2- exponenciacion **
3- multiplicacion, division y modulo *, /, %
4- suma y resta +, -
'''
num1 = 2
num2 = 5

resultado = num1 + num2
resultado2 = num1 - num2
resultado3 = num1 * num2
resultado4 = num1 / num2

print(f"Resultado de operacion aritmetica(num1=2, num2=5) - Suma: {resultado}, Resta: {resultado2}, Multiplicacion: {resultado3}, Division: {resultado4}")


# Operadores Relacionales
'''
- Se utiliza para establecer una relacion entre dos valores
- compara estos valores entre si y esta comparacion produce un resultado de certeza o falsedad (verdadero o falso)
- Tiene el mismo nivel de prioridad en su evaluacion
- Los operadores relacionales tienen menor prioridad que los aritmeticos.
< Mayor que
> Menor que
>= menor o igual que
<= Mayor o igual que
!= diferente
== igual
'''
resultado = 10 < 20
resultado2 = 10 > 20
resultado3 = 10 >= 20
resultado4 = 10 <= 20
resultado5 = 10 != 20
resultado6 = 10 == 20

print(f"Resultado de operadores relacionales entre 10 y 20, <: {resultado}, >: {resultado2}, >=: {resultado3}, <=: {resultado4}, !=: {resultado5}, ==: {resultado6}")

# Operadores lógicos
'''
Permiten construir operaciones logicas, se obtienen como resultado booleanos (Verdadero o falso // true or false // 1 o 0)
AND (Conjuncion o multiplicacion logica) - Se usan dos operando (o mas) y el resultado solo sera true si los operando son true (es decir 1x1=1, 1X0=0, 0x0=0, 0x1=0), le resto re las opciones es false
OR (Disyuncion o suma logica) - se usan dos operando (o mas) y el resultado sera true salvo cuando ambos operando sean false (es decir 1+1=1, 1+0=0, 0+1=1, 0+0=0
NOT (Negacion o cambio) si el resultado es cambiado cuando se añade NOT, es decir que true pasa a false y false a true, true --> Not(true)=False
Prioridades:
1- NOT
2- AND
3- OR


a = 10
b = 12
c = 13
d = 10

((a>b) or (a<c)) and ((a==c) or (a>=b))
False or True and False or False
(0 or 1) and (0 or 0)
True and False
False
'''
'''
#Prioridades de los operadores en General
1- ()
2- **
3- *, /, mod, not
4- +, -, and
5- >, <, ==, >=, <=. !=, or
6- 
'''

a = 10
b = 15
c = 20

resultado = ((a<b) and (b<c))

print( f"Resultado de operadores logicos '((a<b) and (b<c))': {resultado}")

# Operadores de asignacion
'''
a comienza con el valot 0 y despues se le suman 5, quedando con valor 5

"a = a + 5" es igual a "a += 5" es una abreviacion, esto se conoce como la suma en asignacion, tambien otras operaciones, ej:
a -= 5 (resta en asignacion)
a x= 10 (multiplicacion en asignacion)
a /= 2 (division en asignacion)
a **= 2 (potencia en asignacion)
a %= 2 (Modulo en asignacion) - residuo de lo que quedaria en una division si no es par
'''
a = 0
a += 5

print(f"Resultado de operador de asignacion (a=0 --> a += 5): {a}")

# Funciones integradas (Se usan para hacer conversiones entre tipos de datos)

'''
int - resultado de valor entero
float - resultado de valor con decimal o valor real
str - valor de cadena (texto)
bin - convierte el valor en binario
hex - pasa de binario a hexadecimal
'''

a = 5

print("int(a),  Muestra el valor de 'a' en numero entero:", int(a))
print("str(a), Muestra el valor de 'a' en como texto:", str(a))
print("float(a),  Muestra el valor de 'a' en numero en valor real o con decimales:", float(a))
print("bin(a), Muestra el valor de 'a' en como texto:", bin(a))
print("hex(a), Muestra el valor de 'a' en como texto:", hex(a))
