### Operadores ###

print("Operadores aritméticos")
# Operadores aritméticos
# Sumar
suma = 5 + 3
print("Suma:", suma) 
# Restar  
resta = 5 - 3
print("Resta:", resta)
# Multiplicar
multiplicacion = 5 * 3
print("Multiplicación:", multiplicacion)
# Dividir
division = 5 / 3
print("División:", division)
# Potencia
potencia = 5 ** 3
print("Potencia:", potencia)
# Módulo
modulo = 5 % 3 #resto de la división
print("Módulo:", modulo)
# División entera
division_entera = 5 // 3 #parte entera de la división
print("División entera:", division_entera)

# Operadores de comparación
print("Operadores de comparación")
# Mayor que
mayor_que = 5 > 3
print("Mayor que:", mayor_que)
# Menor que
menor_que = 5 < 3
print("Menor que:", menor_que)
# Mayor o igual que
mayor_o_igual_que = 5 >= 3
print("Mayor o igual que:", mayor_o_igual_que)
# Menor o igual que
menor_o_igual_que = 5 <= 3
print("Menor o igual que:", menor_o_igual_que)
# Igual que
igual_que = 5 == 3
print("Igual que:", igual_que)
# Diferente de
diferente_de = 5 != 3
print("Diferente de:", diferente_de)

# Operadores lógicos
print("Operadores lógicos")
# Y
y = True and False
print("Y:", y)
# O
o = True or False
print("O:", o)
# No
no = not True
print("No:", no)
# Operadores de asignación
print("Operadores de asignación")
# Asignación simple
a = 5
print("Asignación simple:", a)
# Asignación con suma
a += 3 # a = a + 3
print("Asignación con suma:", a)
# Asignación con resta
a -= 3 # a = a - 3
print("Asignación con resta:", a)
# Asignación con multiplicación
a *= 3 # a = a * 3
print("Asignación con multiplicación:", a)
# Asignación con división
a /= 3 # a = a / 3
print("Asignación con división:", a)
# Asignación con módulo
a %= 3 # a = a % 3
print("Asignación con módulo:", a)
# Asignación con división entera
a //= 3 # a = a // 3
print("Asignación con división entera:", a)
# Asignación con potencia
a **= 3 # a = a ** 3
print("Asignación con potencia:", a)
# Operadores de identidad
print("Operadores de identidad")
# is
a = [1, 2, 3]
b = a
print("is:", a is b) # True
# is not
a = [1, 2, 3]
b = [1, 2, 3]
print("is not:", a is not b) # True
# Operadores de pertenencia
print("Operadores de pertenencia")
# in
a = [1, 2, 3]
b = 2
print("in:", b in a) # True
# not in
a = [1, 2, 3]
b = 4
print("not in:", b not in a) # True
# Operadores de bits
print("Operadores de bits")
# AND
a = 5 # 0101
b = 3 # 0011
c = a & b # 0001
print("AND:", c) # 1
# OR
a = 5 # 0101
b = 3 # 0011
c = a | b # 0111
print("OR:", c) # 7
# XOR
a = 5 # 0101
b = 3 # 0011
c = a ^ b # 0110
print("XOR:", c) # 6
# NOT
a = 5 # 0101
b = ~a # 1010
print("NOT:", b) # -6
# Desplazamiento a la izquierda
a = 5 # 0101
b = a << 1 # 1010
print("Desplazamiento a la izquierda:", b) # 10
# Desplazamiento a la derecha
a = 5 # 0101
b = a >> 1 # 0010
print("Desplazamiento a la derecha:", b) # 2
# Operadores ternarios
print("Operadores ternarios")
# Operador ternario
a = 5
b = 3
c = a if a > b else b
print("Operador ternario:", c) # 5
# Operador ternario con cadena
a = 5
b = 3
c = "a es mayor" if a > b else "b es mayor"
print("Operador ternario con cadena:", c) # a es mayor
# Operador ternario con cadena y formato
a = 5
b = 3
c = f"{a} es mayor" if a > b else f"{b} es mayor"
print("Operador ternario con cadena y formato:", c) # 5 es mayor



