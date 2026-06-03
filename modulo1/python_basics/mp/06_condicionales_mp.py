print("condicionales simples")
pacientes_hoy = input("¿Cuántos pacientes hay agendados hoy? ")
if int(pacientes_hoy) >= 160:
    print("Consultorio al límite de capacidad")

print("condicionales dos caminos")
saldo_paciente = input("¿Cuál es el saldo a favor del paciente? ")
if float(saldo_paciente) >= 0.35:
    print("Acceso concedido")
else:
    print("Saldo insuficiente")

print("condicionales multiples")
calorias = input("¿Cuántas calorías consumió el paciente? ")
calorias_val = int(calorias)
if calorias_val >= 1000:
    print("Requiere plan de déficit calórico estricto")
elif calorias_val >= 500:
    print("Plan de mantenimiento completado")
elif calorias_val >= 10:
    print("Plan de déficit leve completado")
else:
    print("Ayuno prolongado detectado")

print("condicionales if anidados")
nutricionista_disponible = True
tiempo_consulta = 40
tipo_plan = 'Personalizado'
if nutricionista_disponible:
    if tiempo_consulta >= 30:
        if tipo_plan == 'Personalizado':
            print("Especialista asignado a plan Personalizado, cita confirmada")
        else:
            print("Consulta de seguimiento regular disponible")
    else:
        print("Tiempo insuficiente para la consulta")
else:    
    print("No hay nutricionistas disponibles en la clínica")

print("Calculo de subsidio:")
antiguedad_paciente = input("Ingrese meses de antigüedad del paciente: ")
if int(antiguedad_paciente) > 5:
    apego_plan = input("Ingrese calificación de apego al plan (1-10): ")
    if int(apego_plan) >= 7:
        costo_tratamiento = input("Ingrese costo del tratamiento mensual: ")
        if int(costo_tratamiento) < 5000:
            print("Descuento asignado: $500")
            print(f"Costo final: {int(costo_tratamiento) - 500}")
        if int(costo_tratamiento) >= 5000:
            print("Descuento asignado: $1000")
            print(f"Costo final: {int(costo_tratamiento) - 1000}")
    else:
        print("Paciente no apto para beneficio por bajo apego técnico")