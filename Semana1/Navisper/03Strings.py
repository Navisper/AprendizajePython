### STRINGS ###
# Strings are a sequence of characters
# Strings are immutable
# Strings can be created using single quotes, double quotes, or triple quotes
# Strings can be concatenated using the + operator
# Strings can be repeated using the * operator
# Strings can be indexed using square brackets
# Strings can be sliced using the : operator
# Strings can be formatted using the format() method or f-strings
# Strings can be converted to uppercase or lowercase using the upper() and lower() methods
# Strings can be split using the split() method
# Strings can be joined using the join() method
# Strings can be stripped of whitespace using the strip() method
# Strings can be checked for membership using the in operator
# Strings can be checked for equality using the == operator
# Strings can be checked for inequality using the != operator
# Strings can be checked for greater than or less than using the > and < operators
# Strings can be checked for greater than or equal to or less than or equal to using the >= and <= operators
# Strings can be checked for length using the len() function
# Strings can be checked for presence of a substring using the find() method
# Strings can be checked for presence of a substring using the index() method
# Strings can be checked for presence of a substring using the count() method
# Strings can be checked for presence of a substring using the startswith() method
# Strings can be checked for presence of a substring using the endswith() method

### example ###
# # Strings can be created using single quotes, double quotes, or triple quotes
string1 = 'Hello'
string2 = "World"
string3 = '''Hello World'''
string4 = """Hello World"""
print(string1)
print(string2)
print(string3)
print(string4)
# # Strings can be concatenated using the + operator
string5 = string1 + ' ' + string2
print(string5)
# # Strings can be repeated using the * operator
string6 = string1 * 3
print(string6)
# # Strings can be indexed using square brackets
string7 = string1[0]
print(string7)
# # Strings can be sliced using the : operator  
string8 = string1[0:2]
print(string8)
# # Strings can be formatted using the format() method
string9 = 'Hello {}'.format(string2)
print(string9)
# # Strings can be formatted using f-strings
string10 = f'Hello {string2}'
print(string10)
# # Strings can be converted to uppercase or lowercase using the upper() and lower() methods
string11 = string1.upper()
print(string11)
string12 = string1.lower()
print(string12)
# # Strings can be split using the split() method
string13 = string1.split('l')
print(string13)
# # Strings can be joined using the join() method
string14 = '-'.join(string13)
print(string14)
# # Strings can be stripped of whitespace using the strip() method
string15 = '   Hello World   '
string16 = string15.strip()
print(string16)
# # Strings can be checked for membership using the in operator
string17 = 'Hello' in string1
print(string17)
# # Strings can be checked for equality using the == operator
string18 = string1 == string2
print(string18)
# # Strings can be checked for inequality using the != operator
string19 = string1 != string2
print(string19)
# # Strings can be checked for greater than or less than using the > and < operators
string20 = string1 > string2
print(string20)
# # Strings can be checked for greater than or equal to or less than or equal to using the >= and <= operators
string21 = string1 >= string2
print(string21)
# # Strings can be checked for length using the len() function
string22 = len(string1)
print(string22)
# # Strings can be checked for presence of a substring using the find() method
string23 = string1.find('l')
print(string23)
# # Strings can be checked for presence of a substring using the index() method
string24 = string1.index('l')
print(string24)
# # Strings can be checked for presence of a substring using the count() method
string25 = string1.count('l')
print(string25)
# # Strings can be checked for presence of a substring using the startswith() method
string26 = string1.startswith('H')
print(string26)


### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo