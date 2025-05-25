### Strings ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string  = "Este es un string\nCon salto de linea"
print(my_new_line_string)

### Formateo

name, surname, age = "darwin", "ortiz", 22

print("Mi nombre es: {} {} y mi edad es: {}".format(name, surname, age))
print("Mi nombre es: %s %s y mi edad es: %d" %(name, surname, age))
# mejor forma para inferencia de datos 
print (f"Mi nombre es: {name} {surname} y mi edad es: {age}")

# Desempaqueado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(f)

#Division
laguage_slice = language[1:3]
print (laguage_slice)

language_slice = language[1]
print (language_slice)

language_slice = language[-2]
print (language_slice)

# Reverse 

reversed_language = language[::-1]
print(reversed_language)