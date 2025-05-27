# 1. Crear un diccionario
persona = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Bogotá'
}
print("Diccionario persona:", persona)

# 2. Acceder a valores
print("Nombre:", persona['nombre'])

# 3. Modificar un valor
persona['edad'] = 31
print("Edad modificada:", persona)

# 4. Agregar un nuevo par clave-valor
persona['email'] = 'juan@mail.com'
print("Nuevo dato:", persona)

# 5. Eliminar un dato
del persona['ciudad']
print("Después de eliminar ciudad:", persona)

# 6. Métodos útiles
print("Claves:", list(persona.keys()))
print("Valores:", list(persona.values()))
print("Ítems:", list(persona.items()))

# 7. Recorrer un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# 8. Uso de get() con valor por defecto
print("Teléfono:", persona.get('telefono', 'No disponible'))

# 9. Diccionario anidado
empleado = {
    'nombre': 'Ana',
    'edad': 28,
    'contacto': {
        'email': 'ana@mail.com',
        'teléfono': '123456789'
    }
}
print("Email de Ana:", empleado['contacto']['email'])
