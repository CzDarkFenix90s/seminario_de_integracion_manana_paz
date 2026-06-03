contador_pacientes = 1
while contador_pacientes <= 5:
    print(f"Atendiendo paciente N°: {contador_pacientes}")
    contador_pacientes += 1


print("control del ciclo")
print("continue")
i = 1
while i <= 5:
    i += 1
    if i == 2:
        continue
    print(f"Paciente en consulta: {i}")

print("break")
i = 1
while i <= 5:
    if i == 3:
        break
    print(f"Revisando expediente del paciente {i}")
    i += 1

id_paciente = int(input("Ingrese ID del paciente (0 para salir): "))
while id_paciente != 0:
    print("Monitoreando evolución del paciente:", id_paciente)
    id_paciente = int(input("Ingrese ID del paciente (0 para salir): "))

contador_citas = 1
while contador_citas <= 5:
    print(f"Cita de seguimiento: {contador_citas}")
    contador_citas += 1
else:
    print("Jornada del consultorio finalizada")


contador_calorias = 1
while True:
    print(f"Caloría N° {contador_calorias} registrada")
    contador_calorias += 1
    if not (contador_calorias <= 5):
        break


codigo_acceso = "450"
while True:
    entrada = input("Ingrese código de nutricionista: ")
    if entrada == codigo_acceso:
        print("Báscula inteligente activada - Acceso permitido")
        break
    else:
        print("Código incorrecto - Intente de nuevo")