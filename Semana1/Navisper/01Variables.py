#variables

mi_dato = 10
print(mi_dato)

mi_texto = 'Hola mundo'
print(mi_texto)

mi_bool = True
print(mi_bool)

print(mi_bool,mi_texto, mi_dato)

mi_variable_int_a_string = str(mi_dato)
print(mi_variable_int_a_string)
print(type(mi_variable_int_a_string))

mi_nombre = input('¿Cuál es tu nombre? ')
mi_edad = input('¿Cuál es tu edad? ')

print('Hola', mi_nombre, 'tienes', mi_edad, 'años')

#podemos cambiar el tipo de dato de una variable
mi_variable_int_a_string = str(mi_dato)
print(mi_variable_int_a_string)
mi_bool = 'Hola'
print(type(mi_bool))
mi_texto = -2j
print(type(mi_texto))

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))