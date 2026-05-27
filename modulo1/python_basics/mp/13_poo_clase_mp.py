class UnidadTransporte:
    sistema = "Transporte Público Quito"

    def __init__(self, codigo, capacidad):
        self.codigo = codigo
        self.capacidad = capacidad
        self.pasajeros_actuales = 0

    def registrar_abordaje(self, cantidad):
        if self.pasajeros_actuales + cantidad <= self.capacidad:
            self.pasajeros_actuales += cantidad
            return f"Abordaje exitoso. Pasajeros a bordo: {self.pasajeros_actuales}"
        else:
            return "Error: Capacidad máxima excedida"

    def vaciar_unidad(self):
        self.pasajeros_actuales = 0
        print(f"Unidad {self.codigo} se encuentra vacía.")

    def __str__(self):
        return f"Unidad({self.codigo}, Capacidad: {self.capacidad})"

    def __repr__(self):
        return f"Unidad(codigo={self.codigo!r}, capacidad={self.capacidad!r})"


metro = UnidadTransporte("METRO-Q01", 1500)
trole = UnidadTransporte("TROLE-42", 160)

print(metro.registrar_abordaje(450))
print(trole.registrar_abordaje(100))
metro.vaciar_unidad()
print(str(metro))
print(repr(metro))
print(UnidadTransporte.sistema)