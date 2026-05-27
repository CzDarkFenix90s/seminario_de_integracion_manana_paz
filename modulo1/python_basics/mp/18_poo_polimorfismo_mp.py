class AlertaTransporte:
    def __init__(self, unidad_id, mensaje):
        self.unidad_id = unidad_id
        self.mensaje = mensaje

    def emitir(self):
        raise NotImplementedError("Las subclases deben implementar emitir()")

    def __str__(self):
        return f"{self.__class__.__name__} → Unidad: {self.unidad_id}"

class AlertaPantalla(AlertaTransporte):
    def emitir(self):
        return f"🖥️ Pantalla Central: Unidad {self.unidad_id} reporta: {self.mensaje}"

class AlertaAltavoz(AlertaTransporte):
    def emitir(self):
        return f"🔊 Audio Estación: 'Atención pasajeros, {self.mensaje} en unidad {self.unidad_id}'"

class AlertaApp(AlertaTransporte):
    def emitir(self):
        return f"📲 Notificación App: {self.unidad_id} - {self.mensaje[:30]}..."

def ejecutar_alertas(alertas: list):
    for alerta in alertas:
        print(f"  {alerta.emitir()}")

avisos = [
    AlertaPantalla("METRO-Q01", "Llegada en 2 minutos"),
    AlertaAltavoz("TROLE-42", "Unidad con retraso por tráfico"),
    AlertaApp("ECO-10", "Nueva ruta habilitada para esta unidad"),
]

print("Emisión de alertas del sistema:")
ejecutar_alertas(avisos)

class ValidadorQR:
    def procesar_pago(self): return "Pago procesado con código QR"
    def registrar_log(self, datos): print(f"Log Servidor: {datos}...")

class ValidadorTarjeta:
    def procesar_pago(self): return "Pago procesado con tarjeta física"
    def registrar_log(self, datos): print(f"Log Local: {datos}...")

class ValidadorBiometrico:
    def procesar_pago(self): return "Pago procesado con reconocimiento facial"
    def registrar_log(self, datos): print(f"Log Seguridad: {datos}...")

def realizar_cobro(validador):
    confirmacion = validador.procesar_pago()
    print(f"Estado: {confirmacion}")
    validador.registrar_log(f"Transacción_OK_{confirmacion[:10]}")

for dispositivo in [ValidadorQR(), ValidadorTarjeta(), ValidadorBiometrico()]:
    realizar_cobro(dispositivo)