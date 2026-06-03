class ValidadorConsultas:
    def __init__(self, consultorio_id, saldo_inicial=0):
        self.consultorio_id = consultorio_id
        self.__recaudacion = saldo_inicial
        self.__historial_consultas = []
        self.__estado_activo = True
        self.__registrar_evento(f"Sistema activado en {consultorio_id} con base de ${saldo_inicial}")

    @property
    def recaudacion(self):
        return self.__recaudacion

    @property
    def estado_activo(self):
        return self.__estado_activo

    @property
    def historial(self):
        return list(self.__historial_consultas)

    def registrar_consulta(self, costo):
        if costo <= 0:
            raise ValueError("El costo de la consulta no puede ser nulo o negativo")
        self.__recaudacion += costo
        self.__registrar_evento(f"Consulta cobrada: +${costo}")
        return self

    def anular_consulta(self, costo):
        if costo <= 0:
            raise ValueError("La cantidad a anular debe ser positiva")
        if costo > self.__recaudacion:
            raise ValueError(f"No se puede anular: excede recaudación actual (${self.__recaudacion})")
        self.__recaudacion -= costo
        self.__registrar_evento(f"Anulación / Devolución: -${costo}")
        return self

    def transferir_recaudacion(self, caja_central, monto):
        self.anular_consulta(monto)
        caja_central.registrar_consulta(monto)
        self.__registrar_evento(f"Transferencia de fondos a {caja_central.consultorio_id}: -${monto}")
        return self

    def __registrar_evento(self, operacion):
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M:%S")
        self.__historial_consultas.append(f"[{hora}] {operacion}")

    def __str__(self):
        return f"Consultorio({self.consultorio_id}: ${self.__recaudacion:.2f})"

v1 = ValidadorConsultas("Nutri-Sur01", 50.0)
v2 = ValidadorConsultas("Caja-Central", 1000.0)

v1.registrar_consulta(45.00).registrar_consulta(35.00)
v1.transferir_recaudacion(v2, 25.0)

print(v1)
print(v2)
print(f"Recaudación neta V1: ${v1.recaudacion:.2f}")

for registro in v1.historial:
    print(f"  {registro}")