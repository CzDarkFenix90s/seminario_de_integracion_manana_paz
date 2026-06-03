print("ciclo for")
unidades = ["Bus-01", "Bus-02", "Metro-01", "Trole-05"]
for unidad in unidades:
    print(unidad)

print("Recorrer palabras")
for letra in "METRO":
    print(letra)

print("Recorrer rango")
for i in range(1, 6):
    print(f"Parada {i}")

print("Recorrer rango configurar paso")
for i in range(2, 11, 2):
    print(f"Unidad de refuerzo cada {i} horas")

print("Enumerar Lista")
for i, unidad in enumerate(unidades):
    print(f"Andén {i}: {unidad}")

print("Dos listas a la vez")
conductores = ["Juan", "Dae"]
turnos = ["Mañana", "Tarde"]
for conductor, turno in zip(conductores, turnos):
    print(f"Conductor: {conductor} | Turno: {turno}")

print("control del ciclo")
for i in range(10):
    if i == 3:
        break
    print(f"Validando unidad {i}")

print("continue")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"Estación {i} operativa")

print("for anidado")
for ruta in range(1, 3):
    for unidad in range(1, 3):
        print(f"Ruta {ruta} - Unidad {unidad}")

print("Lista comprehension forms corta")        
tarifas_dinamicas = [t * 1.10 for t in [0.35, 0.45, 0.60]]
print(tarifas_dinamicas)

print("Recorrer números y multiplicar")
for i in range(1, 11):
    recaudacion = i * 0.35
    print(f" {i} pasajes x $0.35 = ${recaudacion:.2f}")

print("")
print("Ejercicio 2 - Gestión de Pasajeros y Subsidios")
conteos_pasajeros = [120, 80, 200, 50, 300]  
unidades_eficientes = 0

for pasajeros in conteos_pasajeros:
    if pasajeros > 100:
        if pasajeros > 250:
            print("Incentivo por alta demanda $30")
        else: 
            print("Incentivo por demanda media $10")
        unidades_eficientes += 1
    else:
        print("Demanda baja: sin incentivo")

incentivo_acumulado = 0
for pasajeros in conteos_pasajeros:
    if pasajeros > 100:
        if pasajeros > 250:
            incentivo_acumulado += 30
        else:
            incentivo_acumulado += 10

print(f"El incentivo acumulado total es: ${incentivo_acumulado}")
print(f"Total de unidades eficientes: {unidades_eficientes}")