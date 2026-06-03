vacio = {}
paciente = {"id": "PAC-Q01", "calorias": 1850, "sucursal": "Quitumbe"}
config_clinica = dict(servidor="192.168.1.10", puerto=8080, activo=True)

print(paciente["id"])
print(paciente.get("nutricionista"))
print(paciente.get("nutricionista", "No asignado"))

paciente["nutricionista"] = "Dae Muñoz"
paciente["calorias"] = 1950
del paciente["sucursal"]
valor_eliminado = paciente.pop("nutricionista")
print(paciente)

print("id" in paciente)
print("sucursal" in paciente)

print(paciente.keys())
print(paciente.values())
print(paciente.items())

for clave, valor in paciente.items():
    print(f"  {clave}: {valor}")

paciente.update({"sucursal": "Recreo", "nivel_hidratacion": "85%"})
print(paciente)

datos_extra = {"tipo_plan": "Hipertrofia", "activo": True}
registro_completo = paciente | datos_extra
print(registro_completo)

sistema_consultorio = {
    "empresa": "Nutri-Salud Quito",
    "expedientes": {
        101: {"plan": "Keto-S1", "estado": "activo"},
        102: {"plan": "Vegano-S1", "estado": "pausado"},
    },
    "sucursales": ["Línea Norte", "Línea Sur"]
}

print(sistema_consultorio["expedientes"][101]["plan"])
sistema_consultorio["expedientes"][103] = {"plan": "Déficit-S2", "estado": "activo"}

paciente.setdefault("pais", "Ecuador")
paciente.setdefault("id", "PAC-999")