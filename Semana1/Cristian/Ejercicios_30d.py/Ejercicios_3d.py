import math

# ---------------------------------- Sobre la librería math ---------------------------------- #
# La librería 'math' es un módulo estándar de Python que provee funciones matemáticas avanzadas
# y constantes que no están disponibles directamente con operadores básicos.
#
# Es importante usarla cuando necesitamos realizar cálculos como raíces cuadradas, funciones trigonométricas,
# logaritmos, redondeos especializados, entre otros.
#
# Ejemplos comunes de uso:
#   - math.sqrt(x): Calcula la raíz cuadrada de x
#   - math.pi: Constante π (aprox. 3.1416)
#   - math.sin(x), math.cos(x): Funciones trigonométricas (x en radianes)
#   - math.ceil(x): Redondea x hacia arriba
#   - math.floor(x): Redondea x hacia abajo
#
# Ejemplo rápido:
#   print(math.sqrt(16))  # Imprime 4.0
#   print(math.pi)        # Imprime 3.141592653589793
# -------------------------------------------------------------------------------------------- #

#------------------------------------------- Ejercicios Practicos -------------------------------------------#

# ----------------------------------------- Inicio Ejercicio 1 ----------------------------------------- #

# Ejercicio práctico:
# Realizar por consola una suma, resta, multiplicación y división entre dos números enteros

A = int(input('Ingrese el primer número entero: '))
B = int(input('Ingrese el segundo número entero: '))

print(f'La suma de {A} + {B} es: {A + B}')
print(f'La resta de {A} - {B} es: {A - B}')
print(f'La multiplicación de {A} * {B} es: {A * B}')
print(f'La división de {A} / {B} es: {A / B}')

# ------------------------------------------ Fin Ejercicio 1 ------------------------------------------ #
# ----------------------------------------- Inicio Ejercicio 2 ----------------------------------------- #

# Ejercicio práctico:
# Realizar un código que convierta grados Fahrenheit a grados Celsius
# Fórmula: °C = (°F - 32) / 1.8

F = int(input('\nIngrese la temperatura en grados Fahrenheit: '))
print('El tipo de dato de F es:', type(F))

C = int((F - 32) / 1.8)  # Se convierte el resultado a entero

print(f'La temperatura en grados Celsius es: {C}\n')

# ------------------------------------------ Fin Ejercicio 2 ------------------------------------------ #
# ----------------------------------------- Inicio Ejercicio 3 ----------------------------------------- #

# Ejercicio práctico:
# Usando el operador de potencia (**) calcular el índice de masa corporal (IMC)
# Fórmula: IMC = peso / (altura ** 2)

P = int(input('Ingrese su peso en kilogramos: '))
A = float(input('Ingrese su altura en metros: '))

print(f'Peso: {P} kg\nAltura: {A} m')

IMC = float(P / (A ** 2))  # Calcula el IMC
IMC = round(IMC, 1)        # Redondea a un decimal

print(f'Su índice de masa corporal es: {IMC}')

#------------------------------------------ Fin Ejercicio 3 ------------------------------------------ #
#-------------------------------------- Inicio del Ejercicio 4 --------------------------------------#

#Ejercicio practico
#Usando lo aprendido realizar un script que le pida al usuario dos números A y B, con estos calcula la hipotenusa
#Formula = c = √(a² + b²)

print('\nIngresa los catetos del triángulo para calcular su hipotenusa.')
A = float(input('Ingrese el lado a:'))
B = float(input('Ingrese el lado b:'))

C = math.sqrt(float(A**2 + B**2))
C = round(C, 2)  # Redondea a 2 decimales

print(f'La hipotenusa del triángulo es: {C}')

#-------------------------------------- Fin del Ejercicio 4 --------------------------------------#
#------------------------------------ Inicio del Ejercicio 5 ------------------------------------#

# Ejercicio práctico
# Realizar un programa que le pida al usuario indicar el monto que tiene en pesos colombianos, soles y reales,
# y calcule el total en dólares (USD) usando tasas de cambio fijas.

print('\nIndica la cantidad de pesos, soles y reales que tienes para calcular el total en dólares (USD).')

# Entradas del usuario
pesos = float(input('Ingresa la cantidad de pesos colombianos que tienes: '))
soles = float(input('Ingresa la cantidad de soles que tienes: '))
reales = float(input('Ingresa la cantidad de reales que tienes: '))

# Conversión a dólares según tasas de cambio fijas
# (estos valores deberían actualizarse regularmente si se usan en producción)
usd_pesos = pesos / 4173.70     # COP a USD
usd_soles = soles / 3.67        # PEN a USD
usd_reales = reales / 0.18      # BRL a USD

# Cálculo del total
total_usd = usd_pesos + usd_soles + usd_reales
total_usd = round(total_usd, 2) # Redondear a 2 decimales

# Mostrar resultado
print(f'Tienes en total {total_usd} USD.')

#-------------------------------------- Fin del Ejercicio 5 --------------------------------------#
#------------------------------------ Inicio del Ejercicio 6 ------------------------------------#

#Ejercicio practico:
#Escriba un script que solicite al usuario ingresar la base y la altura de un triangulo y calcular el area del triangulo 
#Formula: Area = (base x altura) / 2
#Formula: a = (b*h) / 2

print('\nIngrese la BASE y la ALTURA del triangulo para encontra su AREA')
B = float(input('Ingrese la base del triangulo: '))
A = float(input('Ingrese la altura del triangulo: '))

area = ((B*A) / 2)

print(f'El area del triangulo es igual a {area:.1f}')

#-------------------------------------- Fin del Ejercicio 6 --------------------------------------#
#------------------------------------ Inicio del Ejercicio 7 ------------------------------------#

#Ejercio practico:
#Escriba un script que solicite al usuario ingresar los lados a, b y c del triángulo.Calcula el perimetro del triangulo
#Formula: perimetro = (a + b + c)

print('\nIngresa los lados del triangulo A,B y C para calcular su perimetro')

a = float(input('Ingresa el lado A del triangulo: '))
b = float(input('Ingresa el lado b del triangulo: '))
c = float(input('Ingresa el lado c del triangulo: '))

print('El perimetro del triangulo es de:', round(a + b + c,2))

#-------------------------------------- Fin del Ejercicio 7 --------------------------------------#
#------------------------------------ Inicio del Ejercicio 8 ------------------------------------#

#Ejercicio practico:
#Calcula el largo y el ancho de un rectángulo usando las instrucciones.
#Formulas: Calcula su área (área = largo x ancho) y su perímetro (perímetro = 2 x (largo + ancho)).

print('\nIngresa la longitud y el ancho del rectangulo para calcular su area y perimetro')

long = float(input('Ingresa la longitud del rectangulo: '))
anch = float(input('Ingresa el ancho del rectangulo: '))

print('El area del rectangulo es igual a:', round(long * anch,1))
print('El perimetro del rectangulo es igual a:', round(2 * (long + anch),1))

#-------------------------------------- Fin del Ejercicio 8 --------------------------------------#
#------------------------------------ Inicio del Ejercicio 9 ------------------------------------#

# Ejercicio práctico:
# Obtener el radio de un círculo usando input. Calcular su área (area = pi * r * r)
# y la circunferencia (c = 2 * pi * r), donde pi = 3.14.

print('\nIngresa el radio del círculo para calcular su área y circunferencia')

R = float(input('Porfavor indica el radio del circulo: '))

print('El area del circulo es igual a:', round(float((math.pi * (R**2))),2))
print('La circunferencia del circulo es igual a:', round(float(2 * math.pi * R),2))

#------------------------------------ Fin del Ejercicio 9 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 10 ------------------------------------#

# Ejercicio práctico:
# Calcular la pendiente (slope), la intersección en x (x-intercept) y la intersección en y (y-intercept)
# de la recta y = 2x - 2.

print('\nCalcula la pendiente y las intersecciones de la recta y = 2x - 2')

# 1. Mostrar la ecuación
print("\nEcuación de la recta: y = 2x - 2")

# --------------------------
# 3. DEFINICIÓN DE VARIABLES
# --------------------------
# Ecuación: y = mx + b
m = 2   # pendiente
b = -2  # intersección en Y

# -----------------------------------
# 4. CÁLCULOS MATEMÁTICOS REQUERIDOS
# -----------------------------------

# Intersección en Y (cuando x = 0)
x_intercept_y = 0
y_intercept_y = m * x_intercept_y + b

# Intersección en X (cuando y = 0)
# 0 = mx + b => mx = -b => x = -b / m
x_intercept_x = -b / m
y_intercept_x = 0

# -------------------------
# 5. IMPRESIÓN DE RESULTADOS
# -------------------------
print("Pendiente (slope):", m)
print("Intersección en Y: (", x_intercept_y, ",", y_intercept_y, ")")
print("Intersección en X: (", x_intercept_x, ",", y_intercept_x, ")")

#------------------------------------ Fin del Ejercicio 10 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 11 ------------------------------------#

# Ejercicio práctico:
# Calcular la pendiente (slope) usando la fórmula m = (y2 - y1) / (x2 - x1)
# y la distancia euclidiana entre los puntos (2, 2) y (6, 10).

# Aquí colocarás la entrada de datos y cálculos
print('\nCalcula la pendiente y la distancia euclidiana entre los puntos (2, 2) y (6, 10)')

# --------------------------
# 3. DEFINICIÓN DE VARIABLES
# --------------------------
x1, y1 = 2, 2
x2, y2 = 6, 10

# -----------------------------------
# 4. CÁLCULOS MATEMÁTICOS REQUERIDOS
# -----------------------------------

# Fórmula de la pendiente
# m = (y2 - y1) / (x2 - x1)

m = (y2 - y1) / (x2 - x1)

# Fórmula de distancia euclidiana
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

# -------------------------
# 5. IMPRESIÓN DE RESULTADOS
# -------------------------
print("Pendiente (slope):", m )          # Aquí va el resultado de m
print("Distancia euclidiana:", d)       # Aquí va el resultado de d

#------------------------------------ Fin del Ejercicio 11 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 12 ------------------------------------#

# Ejercicio práctico:
# Comparar las pendientes obtenidas en los ejercicios 10 y 11.

print('\nCompara las pendientes calculadas en los ejercicios anteriores')

# Aquí colocarás la entrada de datos y cálculos

#Definimos variables

m1 = 2   # pendiente 1
m2 = 2   #Pendiente 2

print('Las pendientes son iguales?',m1 == m2)

#------------------------------------ Fin del Ejercicio 12 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 13 ------------------------------------#

# Ejercicio práctico:
# Calcular el valor de y = x^2 + 6x + 9 para diferentes valores de x.
# Determinar para qué valor de x, y es igual a 0.

print('\nCalcula y = x^2 + 6x + 9 para distintos valores de x y encuentra cuando y=0')

# Aquí colocarás la entrada de datos y cálculos

x= 1

y = (x**2) + (6*x) + 9

print(f'El valor de y es igual a:{y}')

#------------------------------------ Fin del Ejercicio 13 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 14 ------------------------------------#

# Ejercicio práctico:
# Encontrar la longitud (length) de las cadenas 'python' y 'dragon' y realizar una comparación falsa entre ellas.

print('\nEncuentra la longitud de "python" y "dragon" y realiza una comparación falsa')

# Aquí colocarás la entrada de datos y cálculos

med1 = ('dragon')
med2 = ('python')

log1 = len(med1)
log2 = len(med2)

print(f'La longitud de {med1} es igual a: {log1}')
print(f'La longitud de {med2} es igual a: {log2}')

print(f'{med1}>{med2}',log1 > log2)

#------------------------------------ Fin del Ejercicio 14 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 15 ------------------------------------#

# Ejercicio práctico:
# Usar el operador 'and' para verificar si la cadena 'on' está en ambas palabras 'python' y 'dragon'.

print('\nVerifica si "on" está en ambas palabras "python" y "dragon" usando el operador and')

# Aquí colocarás la entrada de datos y cálculos

r1 = ('on' in 'dragon')
r2 = ('on' in 'python')

print('se encuentra on en la palabra dragon?:', r1)
print('se encuentra on en la palabra python?:', r2)

print('on se encuentra tanto en python como en dragon?', r1 and r2)

#------------------------------------ Fin del Ejercicio 15 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 16 ------------------------------------#

# Ejercicio práctico:
# Usar el operador 'in' para verificar si la palabra 'jargon' está en la oración:
# "I hope this course is not full of jargon."

print('\nVerifica si la palabra "jargon" está en la oración usando el operador in')

# Aquí colocarás la entrada de datos y cálculos

pal1 = 'jargon'
pal2 = 'I hope this course is not full of jargon.'

print('La oraacion es:', pal2)
print(f'¿La palabra "{pal1}" se encuentra en la oración? ->', pal1 in pal2)


#------------------------------------ Fin del Ejercicio 16 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 17 ------------------------------------#

# Ejercicio práctico:
# Verificar si no existe la cadena 'on' en ambas palabras 'dragon' y 'python'.

print('\nVerifica que no exista "on" en ambas palabras "dragon" y "python"')

r1 = ('on' in 'dragon')
r2 = ('on' in 'python')

r3 = not(r1 and r2)

print('La palabra on no existe en las palabras dragon y python?', r3 )

# Aquí colocarás la entrada de datos y cálculos

#------------------------------------ Fin del Ejercicio 17 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 18 ------------------------------------#

# Ejercicio práctico:
# Encontrar la longitud de la palabra 'python', convertir ese valor a float y luego a string.

print('\nCalcula la longitud de "python", conviértela a float y luego a string')

# Aquí colocarás la entrada de datos y cálculos

pal = len('python')
pal = float(pal)
pal = str(pal)

print(f'La palabra python es de tipo:', type(pal))

#------------------------------------ Fin del Ejercicio 18 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 19 ------------------------------------#

# Ejercicio práctico:
# Verificar si un número es par o no. Un número es par si su residuo al dividir por 2 es cero.

print('\nVerifica si un número es par o no')

# Aquí colocarás la entrada de datos y cálculos

print('Ingresa un numero para determinar si es par o no')

num = int(input('Ingresa un numero porfavor: '))
num1 = int(num / 2)#Sin usar % que saca automaticamente el residuo
num2 = int(num1 * 2)
num3 = int(num - num2)
fin = bool(num3 == 0)

print('Tu numero es par?:', fin )


#------------------------------------ Fin del Ejercicio 19 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 20 ------------------------------------#

# Ejercicio práctico:
# Verificar si la división entera de 7 entre 3 es igual al valor entero de 2.7.

print('\nVerifica si la división entera de 7 entre 3 es igual al valor entero de 2.7')

# Cálculos
d = int(7 / 3)     # División 7 entre 3, convertida a entero
v = int(2.7)       # Conversión directa a entero

# Mostrar resultados intermedios
print('La división entera de 7 entre 3 es igual a:', d)
print('El valor entero de 2.7 es igual a:', v)

# Comparación
print('¿Son iguales?:', d == v)

#------------------------------------ Fin del Ejercicio 20 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 21 ------------------------------------#

# Ejercicio práctico:
# Verificar si el tipo de dato de '10' (cadena) es igual al tipo de dato de 10 (entero).

print('\nVerifica si el tipo de dato de "10" es igual al tipo de dato de 10')

# Aquí colocarás la entrada de datos y cálculos

d1 = str('10')
d2 = int('10')


print('10(cadena) es igual a 10(entero)?:', d1 == d2)

#------------------------------------ Fin del Ejercicio 21 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 22 ------------------------------------#

# Ejercicio práctico:
# Verificar si int('9.8') es igual a 10.

print('\nVerifica si int("9.8") es igual a 10')

# Aquí colocarás la entrada de datos y cálculos

#------------------------------------ Fin del Ejercicio 22 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 23 ------------------------------------#

# Ejercicio práctico:
# Escribir un script que solicite al usuario ingresar horas trabajadas y tarifa por hora,
# y calcule el pago semanal.

print('\nCalcula el pago semanal según horas trabajadas y tarifa por hora')

# Aquí colocarás la entrada de datos y cálculos

#------------------------------------ Fin del Ejercicio 23 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 24 ------------------------------------#

# Ejercicio práctico:
# Solicitar al usuario el número de años que ha vivido y calcular cuántos segundos ha vivido,
# asumiendo que una persona puede vivir 100 años.

print('\nCalcula cuántos segundos ha vivido una persona según años de vida')

# Aquí colocarás la entrada de datos y cálculos

#------------------------------------ Fin del Ejercicio 24 ------------------------------------#


#------------------------------------ Inicio del Ejercicio 25 ------------------------------------#

# Ejercicio práctico:
# Escribir un script que muestre la siguiente tabla:
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print('\nMuestra la tabla solicitada')

# Aquí colocarás la entrada de datos y cálculos

#------------------------------------ Fin del Ejercicio 25 ------------------------------------#

