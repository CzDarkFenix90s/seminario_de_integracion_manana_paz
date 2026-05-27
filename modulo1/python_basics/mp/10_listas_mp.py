print("Listas")
print("Crear Listas de Gestión de Transporte")
vacia = []
print(vacia)
unidades = [101, 102, 103, 104, 105, 106, 107]
print(unidades)
estaciones = ["Quitumbe", "Recreo", "Magdalena", "Ejido", "Carolina", "Labrador"]
print(estaciones)
registro_bus = [42, "Trole", "Ruta C1", True, None, 35.5]
print(registro_bus)
rutas_complejas = [1, [10, 20, [30, 40, 50]], 5, 7]
print(rutas_complejas)

print("Acceso a los elementos de la lista de estaciones")
print(estaciones[0])
print(estaciones[-1])
print(estaciones[1:4])
print(estaciones[::-1])

print("CRUD de una lista de flota")

unidades_activas = ['Metro-01', 'Trole-05', 'Bus-22', 'Ecobio-10']
unidades_activas.append('Metro-02')
print(unidades_activas)
unidades_activas.insert(1, 'Trole-01')
print(unidades_activas)
unidades_activas.extend(['Bus-50', 'Bus-51'])
print(unidades_activas)

unidades_activas[0] = "Metro-Q01"
print(unidades_activas)

unidades_activas.remove('Trole-05')
print(unidades_activas)
unidad_fuera = unidades_activas.pop()
print(unidades_activas)
unidad_fuera = unidades_activas.pop(0)
print(unidades_activas)
del unidades_activas[0]
print(unidades_activas)

print("Buscar valores en la lista de Buses ")
print("Bus-50" in unidades_activas)
print(unidades_activas.index('Bus-50'))
print(unidades_activas.count('Bus-50'))

print("Ordenar registros de Buses")
codigos_unidades = [302, 105, 600, 34, 9, 100, 15, 22]
print(codigos_unidades)
codigos_unidades.sort()
print(codigos_unidades)
codigos_unidades.sort(reverse=True)
print(codigos_unidades)
lista_ordenada = sorted(codigos_unidades)
print(codigos_unidades)
print(lista_ordenada)