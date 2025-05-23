# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

# Concatenación de cadenas
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))
print("Hola " + str(5) + " " + "Python " + "¿Qué tal?")
print("Hola " + str(5) + " " + "Python " + str(5) + " " + "¿Qué tal?")
print("Hola " + str(5) + " " + "Python " + str(5) + " " + "¿Qué tal?" * 5)
print("Hola " + str(5) + " " + "Python " + str(5) + " " + "¿Qué tal?" * (2 ** 3))
# Concatenación de cadenas con variables
nombre = "Python"
print("Hola " + nombre + " " + "¿Qué tal?")
# Concatenación de cadenas con variables y números
nombre = "Python"
numero = 5
print("Hola " + nombre + " " + str(numero) + " " + "¿Qué tal?")

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))