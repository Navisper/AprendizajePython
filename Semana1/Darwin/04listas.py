### Listas ###
# 1. Crear una lista
frutas = ['manzana', 'banana', 'cereza']
print("Lista de frutas:", frutas)

# 2. Acceder a elementos por índice
print("Primera fruta:", frutas[0])  # manzana
print("Última fruta:", frutas[-1])  # cereza

# 3. Modificar un elemento
frutas[1] = 'kiwi'
print("Lista modificada:", frutas)

# 4. Agregar elementos
frutas.append('naranja')
print("Después de append:", frutas)

frutas.insert(1, 'uva')
print("Después de insert:", frutas)

# 5. Eliminar elementos
frutas.remove('manzana')  # Elimina la primera aparición de 'manzana'
print("Después de remove:", frutas)

fruta_eliminada = frutas.pop()  # Elimina y retorna el último elemento
print("Fruta eliminada con pop:", fruta_eliminada)
print("Después de pop:", frutas)

del frutas[0]  # Elimina el elemento en el índice 0
print("Después de del:", frutas)

# 6. Otras operaciones
print("Número de frutas:", len(frutas))
print("¿'kiwi' está en la lista?", 'kiwi' in frutas)

# 7. Concatenar listas
otras_frutas = ['mango', 'papaya']
todas_las_frutas = frutas + otras_frutas
print("Todas las frutas:", todas_las_frutas)

# 8. Repetir listas
frutas_repetidas = otras_frutas * 2
print("Frutas repetidas:", frutas_repetidas)

# 9. Sublistas (slicing)
print("Sublista de todas_las_frutas[1:3]:", todas_las_frutas[1:3])

# 10. Recorrer una lista
print("Recorriendo la lista todas_las_frutas:")
for fruta in todas_las_frutas:
    print("-", fruta)

# 11. Crear una lista con range()
numeros = list(range(1, 6))
print("Lista de números:", numeros)

# 12. Comprensión de listas
cuadrados = [x**2 for x in range(1, 6)]
print("Cuadrados:", cuadrados)


