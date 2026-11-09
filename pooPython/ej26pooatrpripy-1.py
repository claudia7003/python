#Ejercicio 2

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self._nombre = nombre
        self._sueldo_base = sueldo_base

        # if nombre == "":
        #     raise ValueError("El nombre no puede estar vacío")
        # if sueldo_base no mayor que 0  y menor que 200.000:
        #     raise ValueError("El sueldo base no puede ser negativo")

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre

    @property
    def sueldo_base(self):
        return self._sueldo_base
    
    @sueldo_base.setter
    def sueldo_base(self, sueldo_base):
        if sueldo_base > 0 and sueldo_base < 200.000:
            raise ValueError("El sueldo base no puede ser negativo")
        self._sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self._sueldo_base
    
    
class Vendedor (Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self._comision = comision

        # if comision menor que el 50% del sueldo base:
        #     raise ValueError("La comisión no puede ser negativa")
        
    @property
    def comision(self):
        return self._comision
    @comision.setter
    def comision(self, comision):
        if self.sueldo_base >= comision * 0.50:
            raise ValueError("La comisión no puede ser negativa")
        self._comision = comision
    
    def calcular_sueldo(self):
        return self._comision +self._sueldo_base

class Gerente (Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self._bono_gestion = bono_gestion

        # if bono_gestion menor que el sueldo base:    
        #     raise ValueError("El bono de gestión no puede ser negativo")
    
    @property
    def bono_gestion(self):
        return self._bono_gestion
    @bono_gestion.setter
    def bono_gestion(self, bono_gestion):
        if self.sueldo_base >= bono_gestion * 0.50:
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

#Prueba con 100€
