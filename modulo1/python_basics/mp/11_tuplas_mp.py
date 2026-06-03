vacia = ()
unitaria = ("Plan-01",)
coordenada = (-0.21, -78.50)
consulta_info = (45.00, "USD", "Quito")
registro_pago = ("ID-998", 45.00, "2026-05-08")

posicion = 10.5, 30.2
print(type(posicion))

print(registro_pago[0])
print(registro_pago[-1])
print(registro_pago[1:])

id_paciente, monto, fecha = registro_pago
print(id_paciente, monto, fecha)

plan_principal, *planes_secundarios = ("Plan-Keto", "Plan-Vegano", "Plan-Hipertrofia", "Plan-Déficit")
print(plan_principal)
print(planes_secundarios)

*evaluacion_previa, diagnostico_final = ("Sobrepeso", "Pre-diabetes", "Resistencia Insulina", "Metabolismo Optimizado")
print(evaluacion_previa)
print(diagnostico_final)

def verificar_cupo(pacientes_agendados, limite_maximo):
    if pacientes_agendados >= limite_maximo:
        return False, "Consultorio lleno"
    return True, "Cupo disponible OK"

estado, msg = verificar_cupo(160, 160)
print(f"Estado: {estado}, Mensaje: {msg}")

red_consultorios = {(-0.21, -78.50): "Sucursal Sur", (0.00, -78.45): "Sucursal Central"}
print(red_consultorios[(-0.21, -78.50)])