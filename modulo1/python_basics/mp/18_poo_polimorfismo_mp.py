class AlertaConsultorio:
    def __init__(self, paciente_id, mensaje):
        self.paciente_id = paciente_id
        self.mensaje = mensaje

    def emitir(self):
        raise NotImplementedError("Las subclases deben implementar emitir()")

    def __str__(self):
        return f"{self.__class__.__name__} → Paciente: {self.paciente_id}"

class AlertaPantalla(AlertaConsultorio):
    def emitir(self):
        return f"🖥️ Pantalla Sala de Espera: Paciente {self.paciente_id} pasar a: {self.mensaje}"

class AlertaAltavoz(AlertaConsultorio):
    def emitir(self):
        return f"🔊 Audio Clínica: 'Atención, el Nutricionista {self.mensaje} espera al paciente {self.paciente_id}'"

class AlertaApp(AlertaConsultorio):
    def emitir(self):
        return f"📲 Notificación App NutriSalud: {self.paciente_id} - Su recordatorio: {self.mensaje[:30]}..."

def ejecutar_alertas(alertas: list):
    for alerta in alertas:
        print(f"  {alerta.emitir()}")

avisos = [
    AlertaPantalla("PAC-Q01", "Consultorio 3"),
    AlertaAltavoz("PAC-42", "Mateo Paz"),
    AlertaApp("PAC-10", "Es hora de registrar su consumo de agua"),
]

print("Emisión de alertas del sistema:")
ejecutar_alertas(avisos)


class PagoQR:
    def procesar_pago(self): return "Pago de consulta procesado con código QR"
    def registrar_log(self, datos): print(f"Log Servidor: {datos}...")

class PagoTarjeta:
    def procesar_pago(self): return "Pago de consulta procesado con tarjeta física"
    def registrar_log(self, datos): print(f"Log Local: {datos}...")

class PagoTransferencia:
    def procesar_pago(self): return "Pago de consulta procesado con transferencia bancaria"
    def registrar_log(self, datos): print(f"Log Seguridad: {datos}...")

def realizar_cobro(validador):
    confirmacion = validador.procesar_pago()
    print(f"Estado: {confirmacion}")
    validador.registrar_log(f"Transacción_OK_{confirmacion[:10]}")

for dispositivo in [PagoQR(), PagoTarjeta(), PagoTransferencia()]:
    realizar_cobro(dispositivo)