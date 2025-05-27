# Definición de clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear objeto
persona1 = Persona("Carlos", 25)
persona1.saludar()

# Herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self.cargo = cargo

    def mostrar_cargo(self):
        print(f"Soy {self.nombre} y trabajo como {self.cargo}")

empleado1 = Empleado("Lucía", 30, "Ingeniera")
empleado1.saludar()
empleado1.mostrar_cargo()
