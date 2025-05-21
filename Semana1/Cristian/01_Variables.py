#----------------------------- Primeros ejercicios para aprender Python -----------------------------#
#----------------------------------------- Ejercicio 01.1 -----------------------------------------#

# Variables en Python
# Las variables son espacios de memoria donde se almacenan datos temporales. Estos datos pueden ser de diferentes tipos:
# como enteros, decimales, cadenas de texto, booleanos, listas, etc.

"""
La forma correcta de declarar una variable es:
    nombre_variable = valor_variable 
    Cuando le colocamos nombre a nuestra variable y tenemos que separar las palabras, usamos guiones bajos (_).
    Esto es una buena práctica para que el nombre de la variable sea legible y entendible.

    Ejemplo:
"""
NombreUno = 'cristian'  # Esta variable puede estar mal escrita, ya que no es entendible
nombre_uno = 'cristian' # Esta variable es correcta, ya que es legible y entendible. Usamos el guion bajo y todo en minúsculas.

# Tipos de datos en Python:
    # 1. Números enteros (int): 1, 2, 3, 4, 5
    # 2. Números decimales (float): 1.0, 2.5, 3.14
    # 3. Cadenas de texto (str): 'Hola', 'Python'
    # 4. Booleanos (bool): True, False
    # 5. Listas (list): [1, 2, 3], ['Hola', 'Mundo'], [True, False]

# Ejemplos de los tipos de datos:

# 1. Número entero (int)
numero_entero = 5
print('El número entero es:', numero_entero)

# 2. Número decimal (float)
numero_decimal = 5.5
print('El número decimal es:', numero_decimal)

# 3. Cadena de texto (str)
cadena_texto = 'Hola Mundo'
print('La cadena de texto es:', cadena_texto)

# 4. Booleano (bool)
booleano = True
print('El booleano es:', booleano, '\n')

# Variables en una sola línea (evita abusar de esta sintaxis):
name, surname, alias, age = "Cristian", "Marquez", 'TIKI', 22
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Función len()
# len() permite contar la cantidad de caracteres que tiene una cadena de texto.

cadena_texto = 'Hola Mundo'
cadena_texto_contar = len(cadena_texto)
print('La cantidad de caracteres que tiene la cadena de texto es:', cadena_texto_contar)

# Ejercicio práctico:
# Realizar un código que cuente la cantidad de caracteres que tiene una cadena de texto, usando la función len()

# Solución:
cadena_texto = input('Ingrese un texto: ')
contar_cadena = len(cadena_texto)
print('La cantidad de caracteres que tiene la cadena de texto (contando espacios) es:', contar_cadena)

# Si se desea contar solo las letras (sin espacios), se puede usar replace()
replace_cadena = cadena_texto.replace(' ', '')  # Elimina los espacios
contar_cadena = len(replace_cadena)
print('La cantidad de caracteres sin contar los espacios es:', contar_cadena)

# En Python, podemos cambiar el tipo de dato de una variable
# Ejemplo:

cadena_texto = 'Hola Mundo'  # Primero es una cadena de texto
cadena_texto = 5.5           # Luego es un número decimal (float)
cadena_texto = True          # Finalmente, un booleano

print('El tipo de dato actual de la variable cadena_texto es:', type(cadena_texto))

# Nota: Cambiar el tipo de dato de una variable puede causar errores si no se controla bien.

#------------------------------------------ Fin Ejercicio 01.1 ------------------------------------------#
