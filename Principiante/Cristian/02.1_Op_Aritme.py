# ----------------------------- Primeros ejercicios para aprender Python ----------------------------- #
# ----------------------------------------- Inicio Ejercicio 02.1 ----------------------------------------- #

# En Python existen diferentes tipos de operadores aritméticos, que se usan para realizar operaciones matemáticas entre números. 
# Estos operadores son:

# Tipos de operadores aritméticos en Python:
#   1. Suma (+)
#   2. Resta (-)
#   3. Multiplicación (*)
#   4. División (/)
#   5. División entera (//)
#   6. Módulo (%)
#   7. Potencia (**)
#   8. Raíz cuadrada (sqrt)
#   9. Raíz cúbica (cbrt)
#  10. Raíz n (nrt)

# Podemos sumar, restar, multiplicar y dividir números enteros y decimales directamente con print() y el operador aritmético:

# Ejemplo de operadores aritméticos con números:
print('Suma:', 4 + 3)
print('Resta:', 4 - 3)
print('Multiplicación:', 4 * 3)
print('División:', 4 / 3)
print('División entera:', 4 // 3)     # Aproxima al entero más cercano hacia abajo
print('Módulo:', 4 % 3)
print('Potencia:', 4 ** 3)

# ------------------------------------------------------------------------------------------------------------ #

# Los operadores aritméticos también se pueden usar con cadenas de texto, aunque no es tan común:

# Ejemplo de operadores aritméticos con texto:

# Suma de texto (concatenación):
print('Suma de texto:', 'Hola' + ' ' + 'Mundo')  # Une dos cadenas con un espacio
print('Suma de texto (alternativa):', 'Hola ' + 'Mundo')  # Otra forma más directa

# Resta de texto (no válida):
# print('Resta de texto:', 'Hola' - 'Mundo')  # Error: no se puede restar texto

# Multiplicación de texto:
print('Multiplicación de texto:', 'Hola ' * 3)  # Repite la cadena 3 veces

# Potencia aplicada a texto (no directa):
# print('Elevar texto:', 'Hola' ** 3)  # Error: no se puede elevar texto
# Pero se puede simular con paréntesis:
print("Elevar texto con multiplicación:", ("Hola " * (2 ** 3)))  # 2**3 = 8 → imprime 'Hola ' 8 veces

# ------------------------------------------------------------------------------------------------------------ #

# Ejercicio práctico con operadores aritméticos:
score = 0
score = 4 + 3       # score = 7
score = 4 - 3       # score = 1
score = 4 * 3       # score = 12
score = 4 / 3       # score = 1.333...
score = 4 % 3       # score = 1

print(f'El número final luego de realizar todas las operaciones es: {score}\n')

# ------------------------------------------ Fin Ejercicio 02.1 ------------------------------------------ #
