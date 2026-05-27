from abc import ABC, abstractmethod

class VehiculoTransporte(ABC):
    def __init__(self, codigo, capacidad, color="blanco"):
        self.codigo = codigo
        self.capacidad = capacidad
        self.color = color

    @abstractmethod
    def calcular_tarifa(self) -> float:
        pass

    @abstractmethod
    def obtener_autonomia(self) -> str:
        pass

    def describir(self) -> str:
        return (f"{self.__class__.__name__} [{self.codigo}] {self.color}: "
                f"Tarifa=${self.calcular_tarifa():.2f}, Autonomía={self.obtener_autonomia()}")

class Metro(VehiculoTransporte):
    def __init__(self, codigo, capacidad, vagones, color="blanco"):
        super().__init__(codigo, capacidad, color)
        self.vagones = vagones

    def calcular_tarifa(self):
        return 0.45

    def obtener_autonomia(self):
        return "Eléctrica (Cateneria)"

class BusArticulado(VehiculoTransporte):
    def __init__(self, codigo, capacidad, combustible_litros, color="blanco"):
        super().__init__(codigo, capacidad, color)
        self.combustible_litros = combustible_litros

    def calcular_tarifa(self):
        return 0.35

    def obtener_autonomia(self):
        autonomia_km = self.combustible_litros * 2.5
        return f"{autonomia_km:.1f} km"

class Teleferico(VehiculoTransporte):
    def __init__(self, codigo, capacidad, longitud_cable, color="blanco"):
        super().__init__(codigo, capacidad, color)
        self.longitud_cable = longitud_cable

    def calcular_tarifa(self):
        return 0.60

    def obtener_autonomia(self):
        return "Sistema de cables por motor central"

flota = [
    Metro("TREN-01", 1500, 6, "azul"),
    BusArticulado("BRT-45", 160, 200, "rojo"),
    Teleferico("TEL-09", 10, 2500, "blanco")
]

for vehiculo in flota:
    print(vehiculo.describir())

capacidad_total = sum(v.capacidad for v in flota)
print(f"Capacidad total del sistema: {capacidad_total} pasajeros")