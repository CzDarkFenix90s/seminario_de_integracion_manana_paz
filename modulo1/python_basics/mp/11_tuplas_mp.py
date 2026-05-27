vacia = ()
unitaria = ("Unidad-01",)
coordenada = (-0.21, -78.50)
tarifa_info = (0.35, "USD", "Quito")
registro_pago = ("ID-998", 15.75, "2026-05-08")


posicion = 10.5, 30.2
print(type(posicion))


print(registro_pago[0])
print(registro_pago[-1])
print(registro_pago[1:])


id_ticket, monto, fecha = registro_pago
print(id_ticket, monto, fecha)


unidad_principal, *unidades_secundarias = ("M-01", "M-02", "M-03", "M-04")
print(unidad_principal)
print(unidades_secundarias)

*ruta_previa, destino_final = ("Terminal S", "Parada 1", "Parada 2", "Terminal N")
print(ruta_previa)
print(destino_final)


def verificar_saldo(saldo, costo):
    if saldo < costo:
        return False, "Saldo insuficiente"
    return True, "Saldo OK"

estado, msg = verificar_saldo(0.10, 0.35)
print(f"Estado: {estado}, Mensaje: {msg}")


red_transporte = {(-0.21, -78.50): "Estación Sur", (0.00, -78.45): "Estación Central"}
print(red_transporte[(-0.21, -78.50)])