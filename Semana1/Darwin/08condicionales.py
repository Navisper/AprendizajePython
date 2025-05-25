edad = 18

# Condicional simple
if edad >= 18:
    print("Eres mayor de edad")

# Condicional con else
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

# Condicional con elif
nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")

# Condicional con múltiples condiciones
usuario = "admin"
clave = "1234"

if usuario == "admin" and clave == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")
