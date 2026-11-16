#Ejercicio 5

from abc import ABC, abstractmethod


class Empleado (ABC):
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

    # def calcular_sueldo(self):
    #     return self._sueldo_base
    @abstractmethod
    def calcular_sueldo(self):
        pass

class EmpleadoBase(Empleado):
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
        EmpleadoBase("Ana", 1200),
        Vendedor("Carlos", 1200, 350),
        Gerente("Marta", 2000, 500)
    ]

print("Sueldo de cada empleado:")
for empleado in empleados:
    print(f"{empleado._nombre}: {empleado.calcular_sueldo()}")

#Prueba con 100€


class Departamento:
    def __init__(self, nombre, gerente):
        self._nombre = nombre
        self._gerente = gerente
        self.empleados = []

    def agregar_empleados(self, empleados):
        self.empleados.append(empleados)

    def calcular_nomina_total(self):
        total = self.gerente.calcular_sueldo()
        for emp in self.empleados:
            total += emp.calcular_sueldo()
        return total


    def mostrar_informacion(self):
        print(f"Departamento {self._nombre}")
        print(f"Gerente: {self._gerente.nombre} ")
        
        for emp in self.empleados:
            tipo = "Vendedor" if isinstance(emp, Vendedor) else "Empleado"
            print(f"{tipo} : {emp.nombre}, {emp.calcular_sueldo()} €")
        print(f"Nómina total del departamento {self.calcular_nomina_total()}€")

if __name__ == "__main__":
    # 1. Departamento Nacional
    gerente_nacional = Gerente("Marta", 2000, 450)
    depto_nacional = Departamento("Nacional", gerente_nacional)
    depto_nacional.agregar_empleado(Empleado("Ana", 1200))
    depto_nacional.agregar_empleado(Vendedor("Carlos", 1200, 350))

    # 2. Departamento Internacional
    gerente_internacional = Gerente("John", 2500, 850)
    depto_internacional = Departamento("Internacional", gerente_internacional)
    depto_internacional.agregar_empleado(Vendedor("Sarah", 1500, 600))
    depto_internacional.agregar_empleado(Vendedor("Pierre", 1500, 550))

    # 3. Departamento Nuevos Productos
    # Usamos a Marta como gerente nacional también para este departamento según el enunciado
    depto_nuevos = Departamento("Nuevos Productos", gerente_nacional)
    depto_nuevos.agregar_empleado(Empleado("Jaime", 1200))
    depto_nuevos.agregar_empleado(Vendedor("Secundino", 1200, 350))

    # Imprimir información global de cada departamento
    departamentos = [depto_nacional, depto_internacional, depto_nuevos]
    
    for depto in departamentos:
        depto.mostrar_informacion()