print("condicionales simples")
capacidad_actual = input("Cuántos pasajeros hay en la unidad? ")
if(int(capacidad_actual) >= 160):
    print("Unidad al límite de capacidad")

print("condicionales dos caminos")
saldo_tarjeta = input("¿Cuál es el saldo de su tarjeta? ")
if(float(saldo_tarjeta) >= 0.35):
    print("Acceso concedido")
else:
    print("Saldo insuficiente")

print("condicionales multiples")
distancia = input("Cuántos kilómetros recorrió la unidad? ")
distancia_val = int(distancia)
if(distancia_val >= 100):
    print("Requiere mantenimiento preventivo")
elif(distancia_val >= 50):
    print("Ruta de larga distancia completada")
elif(distancia_val >= 10):
    print("Ruta urbana estándar completada")
else:
    print("Movimiento técnico o corto")

print("condicionales if anidados")
unidad_disponible = True
combustible = 40
tipo_servicio = 'Expreso'
if(unidad_disponible):
    if(combustible >= 30):
        if(tipo_servicio == 'Expreso'):
            print("Unidad asignada a ruta Expreso, despacho confirmado")
        else:
            print("Servicio regular disponible")
    else:
        print("Combustible insuficiente para la ruta")
else:    
    print("No hay unidades disponibles en terminal")

print("Calculo de subsidio:")
antiguedad_unidad = input("Ingrese años de antigüedad del vehículo: ")
if(int(antiguedad_unidad) > 5):
    estado_mecanico = input("Ingrese calificación técnica (1-10): ")
    if(int(estado_mecanico) >= 7):
        costo_operativo = input("Ingrese costo operativo mensual: ")
        if(int(costo_operativo) < 5000):
            print("Subsidio asignado: $500")
            print(f"Presupuesto final: {int(costo_operativo) + 500}")
        if(int(costo_operativo) >= 5000):
            print("Subsidio asignado: $1000")
            print(f"Presupuesto final: {int(costo_operativo) + 1000}")
    else:
        print("Vehículo no apto para subsidio por estado técnico")