from abc import ABC, abstractmethod

class PlanNutricional(ABC):
    def __init__(self, codigo, capacidad, modalidad="Presencial"):
        self.codigo = codigo
        self.capacidad = capacidad
        self.modalidad = modality = modalidad

    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    @abstractmethod
    def obtener_duracion(self) -> str:
        pass

    def describir(self) -> str:
        return (f"{self.__class__.__name__} [{self.codigo}] ({self.modalidad}): "
                f"Costo=${self.calcular_costo():.2f}, Duración={self.obtener_duracion()}")

class PlanKeto(PlanNutricional):
    def __init__(self, codigo, capacidad, dias_seguimiento, modalidad="Presencial"):
        super().__init__(codigo, capacidad, modalidad)
        self.dias_seguimiento = dias_seguimiento

    def calcular_costo(self):
        return 45.00

    def obtener_duracion(self):
        return f"{self.dias_seguimiento} días de cetosis guiada"

class PlanVegano(PlanNutricional):
    def __init__(self, codigo, capacidad, suplementos_incluidos, modalidad="Presencial"):
        super().__init__(codigo, capacidad, modalidad)
        self.suplementos_incluidos = suplementos_incluidos

    def calcular_costo(self):
        return 35.00

    def obtener_duracion(self):
        return f"Mensual ({self.suplementos_incluidos} suplementos controlados)"

class PlanDeportista(PlanNutricional):
    def __init__(self, codigo, capacidad, sesiones_antropometria, modalidad="Presencial"):
        super().__init__(codigo, capacidad, modalidad)
        self.sesiones_antropometria = sesiones_antropometria

    def calcular_costo(self):
        return 60.00

    def obtener_duracion(self):
        return f"Trimestral con {self.sesiones_antropometria} mediciones de pliegues"

programas_activos = [
    PlanKeto("KETO-01", 1500, 30, "Online"),
    PlanVegano("VEG-45", 160, 3, "Presencial"),
    PlanDeportista("DEP-09", 10, 6, "Presencial")
]

for plan in programas_activos:
    print(plan.describir())

capacidad_total = sum(p.capacidad for p in programas_activos)
print(f"Capacidad total del consultorio: {capacidad_total} pacientes")