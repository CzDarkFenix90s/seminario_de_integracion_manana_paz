class ProgramaNutricional:
    def __init__(self, id_programa, especialidad, año_creacion):
        self.id_programa = id_programa
        self.especialidad = especialidad
        self.año_creacion = año_creacion
        self._progreso_paciente = 0

    def avanzar_progreso(self, incremento):
        self._progreso_paciente += incremento
        return self

    def retroceder_progreso(self, decremento):
        self._progreso_paciente = max(0, self._progreso_paciente - decremento)
        return self

    def __str__(self):
        return f"[{self.id_programa}] {self.especialidad} ({self.año_creacion}) — Progreso: {self._progreso_paciente}%"

class PlanAlimentario(ProgramaNutricional):
    def __init__(self, id_programa, especialidad, año_creacion, dias_duracion=40):
        super().__init__(id_programa, especialidad, año_creacion)
        self.dias_duracion = dias_duracion

    def enviar_recordatorio(self):
        return f"Programa {self.id_programa}: ¡Es momento de registrar tus porciones!"

    def __str__(self):
        return f"{super().__str__()} ({self.dias_duracion} días)"

class ClinicaMetabolica(ProgramaNutricional):
    def __init__(self, id_programa, especialidad, año_creacion, numero_fases):
        super().__init__(id_programa, especialidad, año_creacion)
        self.numero_fases = numero_fases

    def anunciar_fase(self, nombre_fase):
        return f"🥑 Próxima etapa del tratamiento: {nombre_fase}"

    def __str__(self):
        return f"{super().__str__()} ({self.numero_fases} fases)"

class PlanKetoInteligente(PlanAlimentario):
    def __init__(self, id_programa, especialidad, año_creacion, limite_carbohidratos_g):
        super().__init__(id_programa, especialidad, año_creacion)
        self.__carbs_maximos = limite_carbohidratos_g
        self.__cetosis_porcentaje = 100

    def ajustar_cetosis(self, porcentaje=100):
        self.__cetosis_porcentaje = min(100, self.__cetosis_porcentaje + porcentaje)
        return self

    @property
    def carbs_disponibles(self):
        return self.__carbs_maximos * self.__cetosis_porcentaje / 100

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Nivel de Cetosis: {self.__cetosis_porcentaje}% | "
                f"Carbohidratos Netos: {self.carbs_disponibles:.0f}g")


paciente_k1 = PlanKetoInteligente("K-DIET-042", "Keto Clínica Avanzada", 2026, 30)
paciente_k1.avanzar_progreso(50)
print(paciente_k1)

print(isinstance(paciente_k1, PlanKetoInteligente)) 
print(isinstance(paciente_k1, PlanAlimentario))           
print(isinstance(paciente_k1, ProgramaNutricional)) 
print(isinstance(paciente_k1, ClinicaMetabolica))     

print(PlanKetoInteligente.__mro__)