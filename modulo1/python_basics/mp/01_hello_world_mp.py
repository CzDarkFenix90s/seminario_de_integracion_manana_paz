print("Sistema de Gestión de Transporte Público")

capacidad = 160
unidad = "Bus Articulado C-20"

print(f"Vehículo: {unidad} | Capacidad: {capacidad} pasajeros.")
print("Unidad:", unidad, "Capacidad Máxima:", capacidad)
id_ruta = 450198
print("El {} tiene una capacidad de {} personas.".format(unidad, capacidad))
print(unidad, capacidad, id_ruta, sep=" - ")
print(unidad, end= " | ")
print(capacidad, end= " | ")
print(id_ruta, end= " | ")

print(f"\nTarifa: {0.350:.2f}")
print(f"Validaciones anuales: {12550800:,}")