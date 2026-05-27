print("Match Case")
accion = input("Acción de la unidad (despachar/estacionar/reparar): ")
match accion:
    case "despachar":
        print("Unidad saliendo a ruta asignada")
    case "estacionar":
        print("Unidad ingresando a zona de parqueo")
    case "reparar":
        print("Unidad enviada a talleres técnicos")
    case _:
        print(f"Estado '{accion}' no registrado en el sistema")

print("match condiciones")
capacidad_bus = 160
match capacidad_bus:
    case n if n < 0:
        print(f"Error: La capacidad {n} no puede ser negativa")
    case 0:
        print("La unidad está fuera de servicio o vacía")
    case n if n % 2 != 0:
        print(f"Capacidad {n} es un número de asientos impar")
    case n:
        print(f"Capacidad de {n} pasajeros es estándar y par")