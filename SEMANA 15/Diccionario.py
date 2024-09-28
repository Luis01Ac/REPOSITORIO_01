# Crear un diccionario con información personal
informacion_personal = {"nombre": "Juan Aldaz","ciudad": "Ambato","profesion": "Tecnico industrial","edad": 32  # Inicialmente incluimos la edad
}

# Cambiamos la ciudad de Ambato a Latacunga
informacion_personal["ciudad"] = "Latacunga"

# Revisamos si ya existe un teléfono; si no, lo añadimos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "03-2758963"

# Cambiamos la profesión a Mecanico
informacion_personal["profesion"] = "Mecanico"

# Quitamos la edad del diccionario creado
del informacion_personal["edad"]

# imprimimos la información final resultante
print(informacion_personal)