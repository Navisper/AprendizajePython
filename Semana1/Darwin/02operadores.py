### Operadores ###
print("----------------------------------------------------------")
print("Operadores")
print('Suma:', 4 + 3)
print('Resta:', 4 - 3)
print('Multiplicación:', 4 * 3)
print('División:', 4 / 3)
print('Módulo:', 4 % 3)
print('División entera:', 4 // 3)   # Aproxima al entero más cercano hacia abajo(flor division)
print('Potencia:', 4 ** 3)

print("Pruebas con strings")
print("Hola"+"Python")
#print("Hola"+5) no se puede trabajar con 2 tipos de variable distintas a no ser de que se use una funcion
print("Hola"+ str(2))
print("----------------------------------------------------------")

### Operadores Comparativos ###
print("----------------------------------------------------------")
print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

print("Pruebas de operadores con strings")
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" <= "abaa") # Ordenacion alfabetica
print("aaaa" >= "abaa")
print(len("aaaa") >= len("abba")) #Cuenta la cadela (longitud)",
print("Hola" == "Python")
print("Hola" != "Python")
print("----------------------------------------------------------")
### Operadores Logicos ###
print("----------------------------------------------------------")
print(3 > 4 and "hola" > "python")
print(3 > 4 or "hola" > "python")
print(3 < 4 and "hola" < "python")
print(3 < 4 or "hola" > "python")
print(3 < 4 or "hola" > "python" and 4 == 4)
print(not(3 > 4))
print("----------------------------------------------------------")
