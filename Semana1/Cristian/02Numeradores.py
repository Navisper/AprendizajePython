#----------------------------- Primeros ejercicio para aprender Python -----------------------------#
#----------------------------------------- Inicio Ejercicio 02.1 -----------------------------------------#

#En python existen diferentes tipos de operadores aritmeticos, los cuales son utilizados para realizar operaciones matematicas entre numeros. Estos operadores son:

#Tipos de operadores aritmeticos en Python:
    #1. Suma (+)
    #2. Resta (-)
    #3. Multiplicacion (*)
    #4. Division (/)
    #5. Division entera (//)
    #6. Modulo (%)
    #7. Potencia (**)
    #8. Raiz cuadrada (sqrt)
    #9. Raiz cubica (cbrt)
    #10. Raiz n (nrt)

#Realizar un ejercicio usando los operadores aritmeticos en Python:
#Ejemplo de los operadores aritmeticos:

score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print(f'El numero final luego de realizar todas las operaciones es:{score} \n')# Output: 1

#Ejercicio practico:
#Realiza un codigo que cambie de grados farenheit a grados centigrados usando la siguiente formula:
#Grados centigrados = (Grados farenheit - 32) * 5/9 o,
#Grados centigrados = (Grados farenheit - 32) / 1.8

F = int(input('Ingrese la temperatura en grados farenheit:'))#Pide al usuario que ingrese la temperatura en grados farenheit y lo convierte a un numero entero

print(f'El dato es', type(F))#Imprime ek tipo de dato de la variable F

#F = int(F) #Convierte la temperatura de grados farenheit a un numero decimal si no es un numero entero

C = int((F - 32) / 1.8)#Covierte la respuesta en un entero y luego convierte la temperatura de grados farenheit a grados centigrados usando la formula 

#C = int(C) #Convierte la temperatura de grados centigrados a un numero entero si no es un numero entero

print(f'La temperatura en grados centigrados es: {C}', '\n')#Imprime la temperatura en grados centigrados

#------------------------------------------ Fin Ejercicio 02.2 ------------------------------------------#

#----------------------------------------- Inicio Ejercicio 02.3 -----------------------------------------#
#Usando el operador aritmetico de potencia (**) realiza un programa que calcule el indice de masa corporal (IMC) usando la siguiente formula:
#IMC = peso / (altura ** 2)

P = int(input('Ingrese su peso en kilogramos:'))#Pide al usuario que ingrese su peso en kilogramos y lo convierte a un numero entero
A = float(input('Ingrese su altura en metros:'))#Pide al usuario que ingrese su altura en metros y lo convierte a un numero flotante

print(f'El peso es:', P,'\nla altura es:', A)#Imprime el peso y la altura

IMC = float(P / (A ** 2))#Convierte la respuesta en un flotante y luego calcula el indice de masa corporal usando la formula

#round redondea el resultado a los decimales que le indiquemos un ejemplo es round(PI, 2) redondea el resultado a 2 decimales round(variable, decimales)
IMC = round(IMC, 1)#Redondea el resultado a 1 decimales

print(f'El indice de masa corporal es:', IMC)#Imprime el indice de masa corporal

#------------------------------------------ Fin Ejercicio 02.3 ------------------------------------------#