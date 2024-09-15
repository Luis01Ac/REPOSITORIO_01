def calcular_temperatura_promedio(ciudades, dias_semana, temperaturas):
    num_semanas = len(temperaturas[0])
    num_dias = len(dias_semana)
    num_ciudades = len(ciudades)

    # creamos una lista para almacenar los promedios
    promedios_semanales = [[0] * num_semanas for _ in range(num_ciudades)]

    # Calculamos el promedio de temperaturas por ciudad y semana
    for ciudad in range(num_ciudades):
        for semana in range(num_semanas):
            temperaturas_semana = temperaturas[ciudad][semana]
            promedio_temperatura = sum(temperaturas_semana) / num_dias
            promedios_semanales[ciudad][semana] = promedio_temperatura

    return promedios_semanales

# Ejecucion usando los datos pdel anterior ejemplo
ciudades = ['Ambato', 'Latacunga', 'Quito', 'Riobamba']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

temperaturas = [
    [  # Ambato
        [20, 18, 22, 23, 24, 25, 26],  # Semana 1
        [21, 22, 23, 24, 25, 26, 27],  # Semana 2
        [22, 26, 22, 25, 26, 24, 28],  # Semana 3
        [23, 14, 25, 16, 18, 28, 22]   # Semana 4
    ],
    [  # Latacunga
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1
        [18, 17, 18, 18, 20, 21, 22],  # Semana 2
        [17, 18, 19, 22, 21, 22, 23],  # Semana 3
        [18, 22, 20, 21, 22, 23, 24]   # Semana 4
    ],
    [  # Quito
        [10, 21, 22, 13, 24, 15, 16],  # Semana 1
        [11, 22, 23, 14, 15, 16, 17],  # Semana 2
        [12, 13, 14, 25, 26, 27, 18],  # Semana 3
        [13, 14, 15, 16, 17, 18, 19]   # Semana 4
    ],
    [  # Riobamba
        [12, 16, 17, 28, 19, 10, 12],   # Semana 1
        [16, 17, 18, 19, 20, 11, 12],   # Semana 2
        [17, 18, 19, 20, 22, 22, 24],   # Semana 3
        [18, 15, 22, 24, 22, 15, 14]    # Semana 4
    ]
]

# Definimos la funcion para calcular y mostrar los promedios
promedios = calcular_temperatura_promedio(ciudades, dias_semana, temperaturas)

print("\nPromedios de Temperatura por Ciudad y Semana:")
for ciudad_index, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for semana in range(len(promedios[ciudad_index])):
        print(f"  Promedio de temperatura en Semana {semana + 1}: {promedios[ciudad_index][semana]:.2f}°C")