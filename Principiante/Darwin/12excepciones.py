# Manejo básico
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Fin del programa")
