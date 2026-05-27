print('Funciones de python')
print('Funcion basica')

def iniciar_sistema():
    print('Sistema de Transporte Público de Quito activado')

iniciar_sistema()


print('Funcion con parametros')
def registrar_conductor(nombre):
    print(f'Unidad asignada a: {nombre}, ¿listo para la ruta?')

registrar_conductor('Danna')
registrar_conductor('Mateo')
    
print('Funcion que devuelve valor con return')
def calcular_pasaje(adultos, niños):
    return (adultos * 0.35) + (niños * 0.17)

total = calcular_pasaje(10, 5)
print(f"Recaudación en parada: ${total}")

print('Funcion con valor por posicion')
def registrar_parada(nombre, capacidad, sector):
    print(f'Estación: {nombre}, Aforo: {capacidad}, Ubicación: {sector}')

registrar_parada('Quitumbe', 2500, 'Sur')  
registrar_parada(sector='Norte', nombre='Carcelén', capacidad=1800) 

print('Funcion con valor por defecto')
def notificar_alerta(unidad, mensaje="En ruta", prioridad="Baja"):
    print(f'Unidad {unidad}: {mensaje} [Prioridad: {prioridad}]')

notificar_alerta('Metro-01', "Mantenimiento", "Alta")  
notificar_alerta("Trole-15", prioridad="Media")
notificar_alerta("Bus-202", "Retraso por tráfico")


print('Funcion parametros posicionales')
def sumar_pasajeros(*buses):
    print(f"Pasajeros por unidad recibidos: {buses}")
    return sum(buses)

print(sumar_pasajeros(45, 60, 30))
print(sumar_pasajeros(120, 150, 140, 110))


print('Funcion parametros combinados con posicional')
def lista_estaciones(linea, *paradas):
    print(f"Línea: {linea}")
    for parada in paradas:
        print(f"  - Estación: {parada}")
    
lista_estaciones("Línea 1 Metro", "Magdalena", "San Francisco", "Ejido", "Carolina")

print('Funcion parametros con clave valor variables')
def crear_bitacora(**detalles):
    print("Resumen de turno:")
    for clave, valor in detalles.items():
        print(f" {clave.capitalize()}: {valor}")
    
crear_bitacora(unidad="Metro-Q05", conductor="Danna Gonzalez", km_inicio=12500, estado="Óptimo")


print("Funcion parametros combinacion de todos los tipos")
def configurar_terminal(id_terminal, *anden, activo=True, **servicios):
    print(f"Terminal ID: {id_terminal}")
    print(f"Andenes operativos: {anden}")
    print(f"Estado: {activo}")
    print(f"Servicios extra: {servicios}")

configurar_terminal("T-SUR", 1, 2, 3, 4, activo=True, wifi=True, encomiendas=False)

print("Devolver multiples valores")
def rango_pasajeros(registros):
    return min(registros), max(registros)

min_p, max_p = rango_pasajeros([15, 80, 160, 45, 200])
print(f"Carga máxima: {max_p}, Carga mínima: {min_p}")


print("Devolver un diccionario en el caso de muchos valores")
def analizar_flota(kilometrajes):
    total = sum(kilometrajes)
    n = len(kilometrajes)

    return {
        "total_km": total,
        "promedio": total/n if n > 0 else 0,
        "menor_recorrido": min(kilometrajes) if kilometrajes else 0,
        "mayor_recorrido": max(kilometrajes) if kilometrajes else 0,
        "unidades_contadas": n
    }

datos_flota = [120, 450, 320, 800, 210]
stats = analizar_flota(datos_flota)
print(f"Kilometraje Total: {stats['total_km']}")
print(f"Promedio por Unidad: {stats['promedio']:.2f} km")
print(f"Diferencia: {stats['mayor_recorrido'] - stats['menor_recorrido']} km")

print("Funciones Lambdas")
iva_transporte = lambda precio: precio * 1.15 
descuento_estudiante = lambda tarifa: tarifa / 2

print(f"Precio con IVA: {iva_transporte(100)}")
print(f"Tarifa preferencial: {descuento_estudiante(0.35)}")