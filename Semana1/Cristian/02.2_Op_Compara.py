#----------------------------- Primeros ejercicios para aprender Python -----------------------------#
#----------------------------------------- Inicio Ejercicio 02.2 -----------------------------------------#

# En Python existen diferentes tipos de operadores de comparación, los cuales se utilizan para comparar números
# o cadenas de texto. Estos operadores son:

# Tipos de operadores de comparación en Python:
#   1. Mayor que (>)
#   2. Menor que (<)
#   3. Mayor o igual que (>=)
#   4. Menor o igual que (<=)
#   5. Igual que (==)
#   6. Diferente que (!=)

# Ejemplo de operadores de comparación con números:
print('Ejemplo de operadores de comparación con números:')
print('Mayor que:', 4 > 3)
print('Menor que:', 4 < 3)
print('Mayor o igual que:', 4 >= 3)
print('Menor o igual que:', 4 <= 3)
print('Igual que:', 4 == 3)
print('Diferente que:', 4 != 3)

# Cuando utilizamos los operadores de comparación en textos, Python compara el valor ASCII de cada letra.
# Por ejemplo, la letra 'A' tiene un valor ASCII de 65, y la letra 'a' tiene un valor ASCII de 97.
# Por lo tanto, 'A' < 'a' es True.

# ¿Qué es el valor ASCII?
# Es un sistema de codificación de caracteres que asigna un número a cada letra, símbolo o caracter especial.

# ¿Cómo se asigna el valor ASCII?
# Según la tabla ASCII, que contiene todos los caracteres con su respectivo valor numérico.

# Ejemplo de comparación entre cadenas de texto:
print('\nEjemplo de operadores de comparación con cadenas de texto:')
print('Mayor que:', 'Hola' > 'Adios')
print('Menor que:', 'Hola' < 'Adios')
print('Mayor o igual que:', 'Hola' >= 'Adios')
print('Menor o igual que:', 'Hola' <= 'Adios')
print('Igual que:', 'Hola' == 'Adios')
print('Diferente que:', 'Hola' != 'Adios')

# También podemos comparar la longitud de las cadenas usando len(), que cuenta la cantidad de caracteres:
print('\nComparación de longitud de cadenas:')
print(len('Hola') > len('Patatas'))  # 4 > 7 → False
print(len('Hola') < len('Patatas'))  # 4 < 7 → True
print(len('Hola') >= len('Patatas')) # 4 >= 7 → False
print(len('Hola') <= len('Patatas')) # 4 <= 7 → True
print(len('Hola') == len('Patatas')) # 4 == 7 → False
print(len('Hola') != len('Patatas')) # 4 != 7 → True

# Recuerda: len() mide el número de caracteres, no el valor textual de las cadenas.

# También se pueden comparar valores booleanos, aunque no suele ser tan común:
print('\nComparación de booleanos:')
print('True == True:', True == True)
print('True == False:', True == False)
print('False == False:', False == False)

# Además de los operadores anteriores, existen otros que se usan para comparar elementos:
#   1. in       → verificar si un valor está contenido en otro
#   2. not in   → verificar si un valor no está contenido en otro
#   3. is       → verificar si dos objetos son el mismo (por identidad, no por valor)
#   4. is not   → verificar si dos objetos no son el mismo

# Ejemplos con cadenas de texto:
print('\nOperadores especiales con cadenas:')
print('Hola in "Hola Mundo":', 'Hola' in 'Hola Mundo')           # True
print('Hola not in "Hola Mundo":', 'Hola' not in 'Hola Mundo')   # False
print('"Hola" is "Hola":', 'Hola' is 'Hola')                     # True (aunque no se recomienda usar "is" con strings)
print('"Hola" is not "Hola\\n":', 'Hola' is not 'Hola\n')        # True

# Ejemplos con números:
print('\nOperadores especiales con números:')
# print(4 in 4)          # Error: no se puede usar 'in' con enteros
# print(4 not in 4)      # Error: lo mismo
print('4 is 4:', 4 is 4)             # True (mismo objeto en memoria para pequeños enteros)
print('4 is not 4:', 4 is not 4)     # False

# Nota: Usar 'is' o 'is not' con números o strings no es lo ideal en la mayoría de casos. Se usa más con objetos y estructuras complejas.
