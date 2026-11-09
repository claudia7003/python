#Ejercicio 2

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self._nombre = nombre
        self._sueldo_base = sueldo_base

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        if sueldo_base < 0:
            raise ValueError("El sueldo base no puede ser negativo")


    def calcular_sueldo(self):
        return self._sueldo_base
    
    
class Vendedor (Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self._comision = comision

        if comision < 0:
            raise ValueError("La comisión no puede ser negativa")
        
    def calcular_sueldo(self):
        return self._comision +self._sueldo_base

class Gerente (Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self._bono_gestion = bono_gestion

        if bono_gestion < 0:    
            raise ValueError("El bono de gestión no puede ser negativo")

    def calcular_sueldo(self):
        return self._sueldo_base + self._bono_gestion

if __name__ == "__main__":
    empleados = [
        Empleado("Ana", 1200),
        Vendedor("Carlos", 1200, 350),
        Gerente("Marta", 2000, 500)
    ]

print("Sueldo de cada empleado:")
for empleado in empleados:
    print(f"{empleado._nombre}: {empleado.calcular_sueldo()}")