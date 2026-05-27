contador_unidades = 1
while (contador_unidades <= 5):
    print(f"Despachando unidad N°: {contador_unidades}")
    contador_unidades += 1


print("control del ciclo")
print("continue")
i = 1
while (i <= 5):
    i += 1
    if i == 2:
        continue
    print(f"Unidad en ruta: {i}")

print("break")
i = 1
while (i <= 5):
    if i == 3:
        break
    print(f"Revisando sensor de parada {i}")
    i += 1

id_unidad = int(input("Ingrese ID de la unidad (0 para salir): "))
while id_unidad != 0:
    print("Monitoreando unidad:", id_unidad)
    id_unidad = int(input("Ingrese ID de la unidad (0 para salir): "))

contador_vueltas = 1
while (contador_vueltas <= 5):
    print(f"Vuelta de recorrido: {contador_vueltas}")
    contador_vueltas += 1
else:
    print("Jornada de la unidad finalizada")


contador_pasajeros = 1
while True:
    print(f"Pasajero N° {contador_pasajeros} ingresó")
    contador_pasajeros += 1
    if not (contador_pasajeros <= 5):
        break


codigo_acceso = "450"
while True:
    entrada = input("Ingrese código de validador: ")
    if entrada == codigo_acceso:
        print("Validador activado - Acceso permitido")
        break
    else:
        print("Código incorrecto - Intente de nuevo")