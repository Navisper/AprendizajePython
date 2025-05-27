# Variables

my_string_variable = "Hola Mundo"
print(my_string_variable)

my_int_variable = 1
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable) 

# concatemaciom de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de la variable int: ",my_int_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea 
name, surname, alias, age = "darwin","ExitLife","deux",35
print("me llamo:",name,". mi username es:",surname,". mi edad es:",age, ". Y mi alias es:",alias)

# Uso de consola para pedir cosas al usuario #inputs
primer_name = input("¿Cual es tu nombre?")
edad = input("¿cual es tu edad?")

#imprimir en consola los datos del usuario
print("Tu nombre es: ", primer_name)
print("Tu edad es: ",edad)

# Cambiamos el tipo de variable 
name = 32
age = "darwin"
print(name)
print(age)

# Forzamos el tipo (No importa a)
address: str = "Mi direccion"
address = 32
print(address)

