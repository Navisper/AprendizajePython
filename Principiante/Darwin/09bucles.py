# Bucle while
contador = 1
while contador <= 5:
    print("Contador:", contador)
    contador += 1

# Bucle for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)

# Bucle con range()
for i in range(5):
    print("Número:", i)

# break y continue
for i in range(10):
    if i == 3:
        continue  # salta el 3
    if i == 7:
        break  # termina el bucle en 7
    print(i)
