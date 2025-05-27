# Función simple
def saludar():
    print("Hola mundo")

saludar()

# Función con parámetros
def saludar_persona(nombre):
    print(f"Hola {nombre}")

saludar_persona("Juan")

# Función con retorno
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print("Suma:", resultado)

# Función con parámetros por defecto
def saludar_persona(nombre="invitado"):
    print(f"Hola {nombre}")

saludar_persona()
saludar_persona("Ana")
