class PlanNutricional:
    sistema = "Consultorio Dietético Quito"

    def __init__(self, codigo, capacidad):
        self.codigo = codigo
        self.capacidad = capacidad
        self.pacientes_actuales = 0

    def registrar_paciente(self, cantidad):
        if self.pacientes_actuales + cantidad <= self.capacidad:
            self.pacientes_actuales += cantidad
            return f"Ingreso exitoso. Pacientes en el programa: {self.pacientes_actuales}"
        else:
            return "Error: Capacidad máxima excedida"

    def vaciar_programa(self):
        self.pacientes_actuales = 0
        print(f"Programa {self.codigo} se encuentra sin pacientes activos.")

    def __str__(self):
        return f"Programa({self.codigo}, Capacidad: {self.capacidad})"

    def __repr__(self):
        return f"Programa(codigo={self.codigo!r}, capacidad={self.capacidad!r})"


keto = PlanNutricional("KETO-Q01", 1500)
vegano = PlanNutricional("VEGANO-42", 160)

print(keto.registrar_paciente(450))
print(vegano.registrar_paciente(100))
keto.vaciar_programa()
print(str(keto))
print(repr(keto))
print(PlanNutricional.sistema)