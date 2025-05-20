#----------------------------- Primeros ejercicio para aprender Python -----------------------------#
#----------------------------------------- Ejercicio 01.1 -----------------------------------------#
#Variales en Python
#Las variables son espacios de memoria donde se almacenan datos temporales, estos datos pueden ser de diferentes tipos como enteros, decimales, cadenas de texto, booleanos, listas, etc.
"""
La forma correcta de declarar una variable es:
    nombre_variable = valor_variable #Cuando le colocamos nombre a nuestra variable y tenemos que separar las palabras con guiones bajos(_)
    esto es una buena practica para que el nombre de la variable sea legible y entendible
    Ejemplo:                                                                              """
NombreUno = 'cristian'#esta variable puede estar mal escrita ya que no es entendible
nombre_uno = 'cristian' #esta variable es correcta ya que es entendible, unsamos el guion bajo para separar las palabras y todo en minusculas

#Aqui veremos los tipos de datos en Python

#Los tipos de datos son:
    #1. Numeros enteros (int) un ejemplo es : (1, 2, 3, 4, 5)
    #2. Numeros decimales (float) un ejemplo es : (1.0, 2.0, 3.0, 4.0, 5.0)
    #3. Cadenas de texto (str) un ejemplo es : ('Hola', 'Mundo', 'Python')
    #4. Booleanos (bool) un ejemplo es : (True, False)
    #5. Listas (list) un ejemplo es : ([1, 2, 3], ['Hola', 'Mundo'], [True, False])

#Ejemplo de los tipos de datos:
#1. Numeros enteros(int)
numero_entero = 5
print('El numero entero es:', numero_entero)#int

#2. Numeros decimales(float)
numero_decimal = 5.5
print('El numero decimal es:', numero_decimal)#float

#3. Cadenas de texto(str)
cadena_texto = 'Hola Mundo'
print('La cadena de texto es:', cadena_texto)#str

#4. Booleanos(bool)
booleano = True
print('El booleano es:', booleano, '\n')#bool

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Cristian", "Marquez", 'TIKI', 22 #Declaramos las variables en una sola linea, separando cada variable con una coma
print("Me llamo:", name, surname, ". Mi edad es:",age, ". Y mi alias es:", alias)


#Dentro de python existen diferentes tipos de funciones como (len), len() es una funcion que nos permite contar la cantidad de caracteres que tiene una cadena de texto, por ejemplo:

#Ejemplo de la funcion len():
cadena_texto = 'Hola Mundo'
cadena_texto_contar = len(cadena_texto)#len() cuenta la cantidad de caracteres que tiene la cadena de texto, en este caso 10
print('La cantidad de caracteres que tiene la cadena de texto es:', cadena_texto_contar)#Imprime la cantidad de caracteres que tiene la cadena de texto

#Ejercicio practico:
#Realizar un codigo que cuente la cantidad de caracteres que tiene una cadena de texto, usando la funcion len()

#Solucion:
cadena_texto = input('Ingrese un texto:')#Pide al usuario que ingrese una cadena de texto y lo convierte a un string
contar_cadena = len(cadena_texto)#len() cuenta la cantidad de caracteres que tiene la cadena de texto
print('La cantidad de caracteres que tiene la cadena de texto contando los espacios es:', contar_cadena)#Imprime la cantidad de caracteres que tiene la cadena de texto contando espacios y caracteres especiales

#En caso de que quieras solo contar las letras y no los espacios puedes usar la funcion replace() que reemplaza un caracter por otro, en este caso reemplazamos los espacios por nada, es decir, los eliminamos
#replace() es una funcion que nos permite reemplazar un caracter por otro, por ejemplo:
#Ejemplo de la funcion replace():
#cadena_texto = input('Ingrese una texto:')#Pide al usuario que ingrese una cadena de texto y lo convierte a un string
replace_cadena = cadena_texto.replace(' ', '')#replace() reemplaza los espacios por nada, es decir, los elimina
contar_cadena = len(replace_cadena)#len() cuenta la cantidad de caracteres que tiene la cadena de texto previamente eliminando los espacios
print('La cantidad de caracteres que tiene la cadena de texto sin contar los espacios es:', contar_cadena)#Imprime la cantidad de caracteres que tiene la cadena de texto contando espacios y caracteres especiales

#En python podemos assignarle a una variable un tipo de dato y luego cambiarle el tipo de dato a otro tipo de dato, por ejemplo:
#Ejemplo de cambiar el tipo de dato de una variable:

cadena_texto = 'Hola Mundo'#Prinmero le asignamos un tipo de dato string a la variable cadena_texto
cadena_texto = 5.5##Luego le cambiamos el tipo de dato a un float
cadena_texto = True#Y por ultimo le cambiamos el tipo de dato a un booleano
print('El tipo de dato de la variable cadena_texto es:', type(cadena_texto))#Imprime el tipo de dato de la variable cadena_texto, en este caso es un booleano
#Tener cuidado con esto ya que puede causar errores en el programa si no se tiene cuidado al cambiar el tipo de dato de una variable
#------------------------------------------ Fin Ejercicio 01.1 ------------------------------------------#
