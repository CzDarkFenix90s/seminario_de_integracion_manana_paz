print("Sistema de Gestión de Consultorio Dietético")

# Variables adaptadas
capacidad = 160  # Cupos disponibles al mes
unidad = "Plan Nutricional Avanzado"  # Nombre del servicio/programa

print(f"Servicio: {unidad} | Capacidad: {capacidad} pacientes.")
print("Programa:", unidad, "Capacidad Máxima:", capacidad)

id_ruta = 450198  # Se convierte en el ID de la Consulta o Paciente
print("El {} tiene una capacidad de {} personas.".format(unidad, capacidad))
print(unidad, capacidad, id_ruta, sep=" - ")

# Impresión en la misma línea con separadores
print(unidad, end=" | ")
print(capacidad, end=" | ")
print(id_ruta, end=" | ")

# Formatos de números (Tarifa de consulta y citas anuales)
print(f"\nCosto de Consulta: ${55.500:.2f}")
print(f"Consultas anuales atendidas: {12550800:,}")