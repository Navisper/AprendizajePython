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

import math

#------------------------------------------- Ejercicios Practicos -------------------------------------------#

# ----------------------------------------- Inicio Ejercicio 1 ----------------------------------------- #
# Realizar por consola una suma, resta, multiplicación y división entre dos números enteros
# Fórmulas:
A = 2
B = 3
print("-------------------------------------")
#   suma = A + B
print(f"Suma el número {A} + el {B} = {A + B}")
#   resta = A - B
print(f"Resta el número {A} - el {B} = {A - B}")
#   multiplicación = A * B
print(f"Multiplica el número {A} * el {B} = {A * B}")
#   división = A / B
print(f"Divide el número {A} / el {B} = {A / B}")
print("-------------------------------------")
# ------------------------------------------ Fin Ejercicio 1 ------------------------------------------ #

# ----------------------------------------- Inicio Ejercicio 2 ----------------------------------------- #
# Convertir grados Fahrenheit a grados Celsius
# Fórmula: °C = (°F - 32) / 1.8
celsius = (12 - 32) / 1.8
print("-------------------------------------")
print(f"12 grados Fahrenheit equivale a {celsius:.2f} grados Celsius")
print("-------------------------------------")
# ------------------------------------------ Fin Ejercicio 2 ------------------------------------------ #

# ----------------------------------------- Inicio Ejercicio 3 ----------------------------------------- #
# Calcular el índice de masa corporal (IMC)
# Fórmula: IMC = peso / (altura ** 2)
IMC = 82 / (1.85 ** 2)
print("-------------------------------------")
print(f"El índice de masa corporal (IMC) es: {IMC:.2f}")
print("-------------------------------------")
# ------------------------------------------ Fin Ejercicio 3 ------------------------------------------ #

#-------------------------------------- Inicio del Ejercicio 4 --------------------------------------#
# Calcular la hipotenusa de un triángulo dados dos catetos A y B
# Fórmula: c = √(a² + b²)
a = 2
b = 2
c = math.sqrt(a ** 2 + b ** 2)
print("-------------------------------------")
print(f"La hipotenusa del triángulo con catetos {a} y {b} es: {c:.2f}")
print("-------------------------------------")
#-------------------------------------- Fin del Ejercicio 4 --------------------------------------#

#------------------------------------ Inicio del Ejercicio 5 ------------------------------------#
# Calcular el total en dólares (USD) dada una cantidad en pesos colombianos, soles y reales
# Fórmulas:
pesos = 4000
soles = 100
reales = 50

tasa_pesos = 4000
tasa_soles = 3.8
tasa_reales = 5.1

# Conversiones
usd_pesos = pesos / tasa_pesos
usd_soles = soles / tasa_soles
usd_reales = reales / tasa_reales
total_usd = usd_pesos + usd_soles + usd_reales

print("-------------------------------------")
print(f"Se convierten {pesos} pesos a USD: {usd_pesos:.2f}")
print(f"Se convierten {soles} soles a USD: {usd_soles:.2f}")
print(f"Se convierten {reales} reales a USD: {usd_reales:.2f}")
print(f"Total en dólares: {usd_pesos:.2f} + {usd_soles:.2f} + {usd_reales:.2f} = {total_usd:.2f}")
print("-------------------------------------")
#-------------------------------------- Fin del Ejercicio 5 --------------------------------------#


#------------------------------------ Inicio del Ejercicio 6 ------------------------------------#
# Calcular el área de un triángulo dada la base y la altura
# Fórmula: área = (base * altura) / 2
#-------------------------------------- Fin del Ejercicio 6 --------------------------------------#

#------------------------------------ Inicio del Ejercicio 7 ------------------------------------#
# Calcular el perímetro de un triángulo dados los lados a, b y c
# Fórmula: perímetro = a + b + c
#-------------------------------------- Fin del Ejercicio 7 --------------------------------------#

#------------------------------------ Inicio del Ejercicio 8 ------------------------------------#
# Calcular área y perímetro de un rectángulo dado el largo y el ancho
# Fórmulas:
#   área = largo * ancho
#   perímetro = 2 * (largo + ancho)
#-------------------------------------- Fin del Ejercicio 8 --------------------------------------#

#------------------------------------ Inicio del Ejercicio 9 ------------------------------------#
# Calcular área y circunferencia de un círculo dado su radio
# Fórmulas:
#   área = π * r^2
#   circunferencia = 2 * π * r
#------------------------------------ Fin del Ejercicio 9 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 10 ------------------------------------#
# Calcular la pendiente (slope), intersección en x (x-intercept) e intersección en y (y-intercept)
# de la recta y = 2x - 2
# Fórmulas:
#   pendiente = coeficiente de x (2 en este caso)
#   x-intercept: valor de x cuando y = 0
#   y-intercept: valor de y cuando x = 0
#------------------------------------ Fin del Ejercicio 10 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 11 ------------------------------------#
# Calcular pendiente entre dos puntos y distancia euclidiana entre ellos
# Fórmulas:
#   pendiente m = (y2 - y1) / (x2 - x1)
#   distancia = √((x2 - x1)^2 + (y2 - y1)^2)
#------------------------------------ Fin del Ejercicio 11 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 12 ------------------------------------#
# Comparar las pendientes obtenidas en ejercicios previos
# Fórmula:
#   comparar los valores de pendiente calculados
#------------------------------------ Fin del Ejercicio 12 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 13 ------------------------------------#
# Calcular y = x^2 + 6x + 9 para varios valores de x
# Encontrar x donde y = 0 (resolver ecuación cuadrática)
#------------------------------------ Fin del Ejercicio 13 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 14 ------------------------------------#
# Encontrar la longitud de las cadenas 'python' y 'dragon' y realizar una comparación falsa entre ellas
#------------------------------------ Fin del Ejercicio 14 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 15 ------------------------------------#
# Usar operador 'and' para verificar si la subcadena 'on' está en ambas palabras 'python' y 'dragon'
#------------------------------------ Fin del Ejercicio 15 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 16 ------------------------------------#
# Verificar si la palabra 'jargon' está en la oración:
# "I hope this course is not full of jargon."
#------------------------------------ Fin del Ejercicio 16 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 17 ------------------------------------#
# Verificar que no exista la cadena 'on' en ambas palabras 'dragon' y 'python'
#------------------------------------ Fin del Ejercicio 17 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 18 ------------------------------------#
# Encontrar la longitud de la palabra 'python', convertir ese valor a float y luego a string
#------------------------------------ Fin del Ejercicio 18 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 19 ------------------------------------#
# Verificar si un número es par
# Fórmula:
#   Un número es par si número % 2 == 0
#------------------------------------ Fin del Ejercicio 19 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 20 ------------------------------------#
# Verificar si la división entera de 7 entre 3 es igual al valor entero de 2.7
#------------------------------------ Fin del Ejercicio 20 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 21 ------------------------------------#
# Verificar si el tipo de dato de '10' (cadena) es igual al tipo de dato de 10 (entero)
#------------------------------------ Fin del Ejercicio 21 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 22 ------------------------------------#
# Verificar si int('9.8') es igual a 10
# Nota: int() no acepta strings con decimales directamente, se debe convertir a float primero
#------------------------------------ Fin del Ejercicio 22 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 23 ------------------------------------#
# Calcular el pago semanal dados las horas trabajadas y tarifa por hora
# Fórmula:
#   pago = horas_trabajadas * tarifa_por_hora
#------------------------------------ Fin del Ejercicio 23 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 24 ------------------------------------#
# Calcular cuántos segundos ha vivido una persona dado los años de vida (asumiendo 100 años max)
# Fórmula:
#   segundos = años * 365 * 24 * 60 * 60
#------------------------------------ Fin del Ejercicio 24 ------------------------------------#

#------------------------------------ Inicio del Ejercicio 25 ------------------------------------#
# Mostrar la tabla:
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
# (número de fila y potencias de ese número)
#------------------------------------ Fin del Ejercicio 25 ------------------------------------#
