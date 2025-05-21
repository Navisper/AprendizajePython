#----------------------------- Primeros ejercicios para aprender Python -----------------------------#
#----------------------------------------- Inicio Ejercicio 02.2 -----------------------------------------#

# En Python existen diferentes tipos de operadores lógicos, los cuales se utilizan para realizar comparaciones 
# entre valores (como números o cadenas de texto). Estos operadores devuelven resultados booleanos (True o False).

# Tipos de operadores lógicos en Python:
#   1. And (y lógico)
#   2. Or (o lógico)
#   3. Not (negación lógica)

# Estos son los operadores lógicos más básicos y comunes.

print('Ejemplo de operadores lógicos:')

# Estas comparaciones dan resultados booleanos (True o False) y se rigen por las reglas de la lógica booleana.

# False and False = False
print(3 > 4 and "Hola" > "Python")  # 3 no es mayor que 4 (False) y "Hola" no es mayor que "Python" (False)

# False or False = False
print(3 > 4 or "Hola" > "Python")   # 3 no es mayor que 4 (False) o "Hola" no es mayor que "Python" (False)

# True and True = True
print(3 < 4 and "Hola" < "Python")  # 3 es menor que 4 (True) y "Hola" es menor que "Python" (True)

# True or True = True
print(3 < 4 or "Hola" < "Python")   # 3 es menor que 4 (True) o "Hola" es menor que "Python" (True)

# El operador "not" niega una condición lógica.
# Es decir, si la condición es True, "not" la convierte en False, y si es False, la convierte en True.

print(not(3 > 4))  # 3 > 4 es False, pero "not False" se convierte en True.
