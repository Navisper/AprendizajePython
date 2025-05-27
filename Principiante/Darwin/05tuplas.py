# 1. Crear una tupla
colores = ('rojo', 'verde', 'azul')
print("Tupla de colores:", colores)

# 2. Acceder a elementos
print("Primer color:", colores[0])
print("Último color:", colores[-1])

# 3. Longitud de la tupla
print("Número de colores:", len(colores))

# 4. Tupla de un solo elemento
tupla_un_elemento = ('hola',)
print("Tupla con un solo elemento:", tupla_un_elemento)

# 5. Convertir entre lista y tupla
lista_colores = list(colores)
print("Convertida a lista:", lista_colores)

nueva_tupla = tuple(lista_colores)
print("Convertida de nuevo a tupla:", nueva_tupla)

# 6. Desempaquetado
a, b, c = colores
print("Desempaquetado:", a, b, c)

# 7. Indexación y slicing
print("Colores del medio:", colores[1:2])
