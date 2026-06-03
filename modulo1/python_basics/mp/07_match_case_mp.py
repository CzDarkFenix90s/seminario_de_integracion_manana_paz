print("Match Case")
accion = input("Acción de la consulta (atender/agendar/cancelar): ")
match accion:
    case "atender":
        print("Paciente ingresando a evaluación nutricional")
    case "agendar":
        print("Buscando cupos disponibles en el calendario")
    case "cancelar":
        print("Liberando horario y notificando a lista de espera")
    case _:
        print(f"Estado '{accion}' no registrado en el sistema")

print("match condiciones")
calorias_dieta = 160
match calorias_dieta:
    case n if n < 0:
        print(f"Error: El consumo de {n} calorías no puede ser negativo")
    case 0:
        print("El paciente se encuentra en ayuno total")
    case n if n % 2 != 0:
        print(f"La meta de {n} calorías es un número impar")
    case n:
        print(f"La meta de {n} calorías es un valor estándar y par")