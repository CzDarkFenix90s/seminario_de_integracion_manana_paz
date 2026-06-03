print('Funciones de python')
print('Funcion basica')

def iniciar_sistema():
    print('Sistema de Consultorio Dietético activado')

iniciar_sistema()


print('Funcion con parametros')
def registrar_nutricionista(nombre):
    print(f'Consultorio asignado a: {nombre}, ¿listo para la consulta?')

registrar_nutricionista('Danna')
registrar_nutricionista('Mateo')
    
print('Funcion que devuelve valor con return')
def calcular_ingreso(adultos, niños):
    return (adultos * 45.00) + (niños * 25.00)

total = calcular_ingreso(10, 5)
print(f"Recaudación en caja: ${total}")

print('Funcion con valor por posicion')
def registrar_sucursal(nombre, capacidad, sector):
    print(f'Clínica: {nombre}, Aforo: {capacidad}, Ubicación: {sector}')

registrar_sucursal('Quitumbe', 2500, 'Sur')  
registrar_sucursal(sector='Norte', nombre='Carcelén', capacidad=1800) 

print('Funcion con valor por defecto')
def notificar_alerta(paciente, mensaje="En tratamiento", prioridad="Baja"):
    print(f'Paciente {paciente}: {mensaje} [Prioridad: {prioridad}]')

notificar_alerta('Paciente-01', "Modificación de dieta", "Alta")  
notificar_alerta("Paciente-15", prioridad="Media")
notificar_alerta("Paciente-202", "Retraso en cita")


print('Funcion parametros posicionales')
def sumar_calorias(*comidas):
    print(f"Calorías por comida recibidas: {comidas}")
    return sum(comidas)

print(sumar_calorias(450, 600, 300))
print(sumar_calorias(120, 150, 140, 110))


print('Funcion parametros combinados con posicional')
def lista_alimentos(plan, *ingredientes):
    print(f"Plan: {plan}")
    for ingrediente in ingredientes:
        print(f"  - Ingrediente: {ingrediente}")
    
lista_alimentos("Dieta Mediterránea", "Pollo", "Aceite de Oliva", "Espinaca", "Almendras")

print('Funcion parametros con clave valor variables')
def crear_bitacora(**detalles):
    print("Resumen de consulta:")
    for clave, valor in detalles.items():
        print(f" {clave.capitalize()}: {valor}")
    
crear_bitacora(paciente="Paciente-Q05", nutricionista="Danna Gonzalez", peso_inicio=75.5, estado="Óptimo")


print("Funcion parametros combinacion de todos los tipos")
def configurar_consultorio(id_consultorio, *box, activo=True, **servicios):
    print(f"Consultorio ID: {id_consultorio}")
    print(f"Boxes operativos: {box}")
    print(f"Estado: {activo}")
    print(f"Servicios extra: {servicios}")

configurar_consultorio("C-SUR", 1, 2, 3, 4, activo=True, bioimpedancia=True, psicologia=False)

print("Devolver multiples valores")
def rango_calorico(registros):
    return min(registros), max(registros)

min_c, max_c = rango_calorico([1500, 1800, 1600, 1450, 2200])
print(f"Consumo máximo: {max_c}, Consumo mínimo: {min_c}")


print("Devolver un diccionario en el caso de muchos valores")
def analizar_pacientes(pesos):
    total = sum(pesos)
    n = len(pesos)

    return {
        "peso_total": total,
        "promedio": total/n if n > 0 else 0,
        "menor_peso": min(pesos) if pesos else 0,
        "mayor_peso": max(pesos) if pesos else 0,
        "pacientes_contados": n
    }

datos_pesos = [62, 75, 88, 54, 91]
stats = analizar_pacientes(datos_pesos)
print(f"Peso Total del Grupo: {stats['peso_total']} kg")
print(f"Promedio de Peso: {stats['promedio']:.2f} kg")
print(f"Diferencia de Rango: {stats['mayor_peso'] - stats['menor_peso']} kg")

print("Funciones Lambdas")
iva_suplementos = lambda precio: precio * 1.15 
descuento_seguimiento = lambda tarifa: tarifa / 2

print(f"Suplemento con IVA: {iva_suplementos(100)}")
print(f"Tarifa de seguimiento: {descuento_seguimiento(45.00)}")