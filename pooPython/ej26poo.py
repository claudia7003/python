#Ejercicio 1

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base

class Vendedor (Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self):
        return self.comision +self.sueldo_base

class Gerente (Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self.bono_gestion = bono_gestion

    def calcular_sueldo(self):
        return self.sueldo_base + self.bono_gestion

if __name__ == "__main__":
    empleados = [
        Empleado("Ana", 1200),
        Vendedor("Carlos", 1200, 350),
        Gerente("Marta", 2000, 500)
    ]

print("Sueldo de cada empleado:")
for empleado in empleados:
    print(f"{empleado.nombre}: {empleado.calcular_sueldo()}")
