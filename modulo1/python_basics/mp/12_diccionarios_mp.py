vacio = {}
unidad = {"id": "Metro-Q01", "pasajeros": 450, "estacion": "Quitumbe"}
config_red = dict(servidor="192.168.1.10", puerto=8080, activo=True)


print(unidad["id"])
print(unidad.get("conductor"))
print(unidad.get("conductor", "No asignado"))


unidad["conductor"] = "Dae Muñoz"
unidad["pasajeros"] = 480
del unidad["estacion"]
valor_eliminado = unidad.pop("conductor")
print(unidad)


print("id" in unidad)
print("estacion" in unidad)


print(unidad.keys())
print(unidad.values())
print(unidad.items())


for clave, valor in unidad.items():
    print(f"  {clave}: {valor}")


unidad.update({"estacion": "Recreo", "nivel_bateria": "85%"})
print(unidad)


datos_extra = {"tipo": "Articulado", "en_servicio": True}
registro_completo = unidad | datos_extra
print(registro_completo)


sistema_transporte = {
    "empresa": "Metro de Quito",
    "flota": {
        101: {"modelo": "Tren-S1", "estado": "operativo"},
        102: {"modelo": "Tren-S1", "estado": "mantenimiento"},
    },
    "lineas": ["Línea 1", "Línea 2"]
}

print(sistema_transporte["flota"][101]["modelo"])
sistema_transporte["flota"][103] = {"modelo": "Tren-S2", "estado": "operativo"}


unidad.setdefault("pais", "Ecuador")
unidad.setdefault("id", "BUS-999")