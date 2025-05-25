# 1. Crear un conjunto
animales = {'gato', 'perro', 'loro'}
print("Conjunto de animales:", animales)

# 2. No permite duplicados
animales = {'gato', 'perro', 'gato'}
print("Sin duplicados:", animales)

# 3. Añadir elementos
animales.add('pez')
print("Después de add:", animales)

# 4. Agregar múltiples elementos
animales.update(['conejo', 'tortuga'])
print("Después de update:", animales)

# 5. Eliminar elementos
animales.discard('loro')
print("Después de discard:", animales)

# 6. Comprobar existencia
print("¿'gato' está en el conjunto?", 'gato' in animales)

# 7. Operaciones de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}
print("Unión:", a | b)
print("Intersección:", a & b)
print("Diferencia:", a - b)
print("Diferencia simétrica:", a ^ b)
