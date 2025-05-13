"""
-Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
-Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje: Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

"""
# operadores aritmeticos 

# suma 
a = 8
b = 12
suma = a + b 
print("la respuesta es:", suma)
print(f"la respuesta es= {a+b}")
print(a+b)

# resta
a = 10
b = 5
resta = a - b
print("la respuesta es:", resta)
print(f"la respuesta es= {a-b}")
print(a-b)

# multiplicacion
a = 5
b = 10
multiplicasion = a * b
print("la respuesta es:", multiplicasion)
print(f"la respuesta es= {a*b}")
print(a*b)

# divicion
a = 20
b = 4
divicion = a / b
print("la respuesta es:", divicion)
print(f"la respuesta es= {a/b}")
print(a/b)

# divicion entera 
a = 19
b = 3
divicion_entera = a // b
print("la respuesta es:", divicion_entera)
print(f"la respuesta es= {a//b}")
print(a//b)

# modulo
a = 15
b = 6
modulo = a % b
print("la respuesta es:", modulo)
print(f"la respuesta es= {a%b}")
print(a%b)

# potencia
a = 5
b = 2
potencia = a ** b
print(" la respueta es:", potencia)
print(f"la respuesta es= {a**b}")
print(a**b)

# operadores logicos 

# and 
a = True
b = False
and_result = a and b
print("la respuesta es:", and_result)
print(f"la respuesta es= {a and b}")
print(a and b)

# or
a = True
b = False
or_result = a or b
print("la respuesta es:", or_result)
print(f"la respuesta es= {a or b}")
print(a or b)

# not
a = True
not_result = not a
print("la respuesta es:", not_result)
print(f"la respuesta es= {not a}")
print(not a)

# operadores de comparacion
a = 5
b = 10

# mayor que
mayor_que = a > b
print("la respuesta es:", mayor_que)
print(f"la respuesta es= {a > b}")
print(a > b)

# menor que
menor_que = a < b
print("la respuesta es:", menor_que)
print(f"la respuesta es= {a < b}")
print(a < b)

# mayor o igual que
mayor_o_igual_que = a >= b
print("la respuesta es:", mayor_o_igual_que)
print(f"la respuesta es= {a >= b}")
print(a >= b)

# menor o igual que
menor_o_igual_que = a <= b
print("la respuesta es:", menor_o_igual_que)
print(f"la respuesta es= {a <= b}")
print(a <= b)

# igual que
igual_que = a == b
print("la respuesta es:", igual_que)
print(f"la respuesta es= {a == b}")
print(a == b)

# diferente que
diferente_que = a != b
print("la respuesta es:", diferente_que)
print(f"la respuesta es= {a != b}")
print(a != b)

# operadores de asignacion
a = 5   
b = 10

# asignacion simple
a = b
print("la respuesta es:", a)
print(f"la respuesta es= {a}")
print(a)

# asignacion suma
a += b
print("la respuesta es:", a)
print(f"la respuesta es= {a}")
print(a)

# asignacion resta
a -= b
print("la respuesta es:", a)
print(f"la respuesta es= {a}")
print(a)

# asignacion multiplicacion
a *= b
print("la respuesta es:", a)
print(f"la respuesta es= {a}")
print(a)

# asignacion divicion
a /= b
print("la respuesta es:", a)
print(f"la respuesta es= {a}")
print(a)

# asignacion divicion entera
a //= b
print("la respuesta es:", a)
print(f"la respuesta es= {a}")
print(a)

# asignacion modulo
a %= b
print("la respuesta es:", a)
print(f"la respuesta es= {a}")
print(a)

# asignacion potencia
a **= b
print("la respuesta es:", a)
print(f"la respuesta es= {a}")
print(a)

# operadores de identidad
a = [1, 2, 3]
b = a
print("la respuesta es:", a is b)
print(f"la respuesta es= {a is b}")
print(a is b)
print("la respuesta es:", a is not b)
print(f"la respuesta es= {a is not b}")
print(a is not b)

# operadores de pertenencia
a = [1, 2, 3]
b = 2

# pertenece
pertenece = b in a
print("la respuesta es:", pertenece)
print(f"la respuesta es= {b in a}")
print(b in a)

# no pertenece
no_pertenece = b not in a
print("la respuesta es:", no_pertenece)
print(f"la respuesta es= {b not in a}")
print(b not in a)

# operadores de bits
a = 5  # 0101
b = 3  # 0011

# and
and_result = a & b
print("la respuesta es:", and_result)
print(f"la respuesta es= {a & b}")
print(a & b)

# or
or_result = a | b
print("la respuesta es:", or_result)
print(f"la respuesta es= {a | b}")
print(a | b)

# xor
xor_result = a ^ b
print("la respuesta es:", xor_result)
print(f"la respuesta es= {a ^ b}")
print(a ^ b)

# not
not_result = ~a
print("la respuesta es:", not_result)
print(f"la respuesta es= {~a}")
print(~a)

# desplazamiento a la izquierda
desplazamiento_izquierda = a << 1
print("la respuesta es:", desplazamiento_izquierda)
print(f"la respuesta es= {a << 1}")
print(a << 1)

# desplazamiento a la derecha
desplazamiento_derecha = a >> 1
print("la respuesta es:", desplazamiento_derecha)
print(f"la respuesta es= {a >> 1}")
print(a >> 1)

# estructuras de control

# condicionales

# if
a = 10
if a > 5:
    print("a es mayor que 5")
else:
    print("a no es mayor que 5")
    
# if-elif-else
a = 10
if a > 10:
    print("a es mayor que 10")
elif a == 10:
    print("a es igual a 10")
else:
    print("a es menor que 10")

# switch-case (simulado con if-elif-else)
a = 2
if a == 1:
    print("a es uno")
elif a == 2:
    print("a es dos")
elif a == 3:
    print("a es tres")
else:
    print("a no es uno, dos o tres")

# estructuras iterativas

# for
for i in range(5):
    print("Iteracion:", i)  

# while
i = 0
while i < 5:
    print("Iteracion:", i)
    i += 1

# excepciones
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Error: Division por cero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Bloque finally ejecutado")


"""
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

"""

print(f"los numeros son:")
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)






