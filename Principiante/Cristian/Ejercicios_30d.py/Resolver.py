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

#------------------------------------------ Solucion ------------------------------------------#

# Ejercicio práctico:
# Solicitar al usuario el número de años que ha vivido y calcular cuántos segundos ha vivido,
# asumiendo que una persona puede vivir 100 años.

print('\nCalcula cuántos segundos ha vivido una persona según años de vida')

# Aquí colocarás la entrada de datos y cálculos

years = int(input('Cuantos años haz vivido?: '))

d = (years * 365 )
h = (d * 24)
m = (h * 60)
s = (m * 60)

print(f'Has vivido {years} años que equivalen a {d} dias, {h} horas, {m} minutos y {s} segundos')
#-------------------------------------------- Fin --------------------------------------------#