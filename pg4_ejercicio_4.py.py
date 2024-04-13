# Captura de la cantidad de pasajeros para cada día y servicio
pasajeros_semana = []
for dia in range(5):
    pasajeros_dia = []
    print(f"\nIngrese la cantidad de pasajeros para el día {dia + 1}:")
    for servicio in range(4):
        while True:
            cantidad = int(input(f"Ingrese la cantidad de pasajeros para el servicio {servicio + 1}: "))
            if cantidad <= 60:
                pasajeros_dia.append(cantidad)
                break
            else:
                print("La cantidad de pasajeros no puede ser mayor a 60.")
    pasajeros_semana.append(pasajeros_dia)

# Calcula el promedio de pasajeros por día
promedios_dia = [sum(dia) / len(dia) for dia in pasajeros_semana]

# Calcula el promedio general de pasajeros
total_pasajeros = sum(sum(dia) for dia in pasajeros_semana)
total_servicios = len(pasajeros_semana) * len(pasajeros_semana[0])
promedio_total = total_pasajeros / total_servicios

# Muestra los resultados
print("\n--- Resultados ---")
for dia, promedio in enumerate(promedios_dia):
    print(f"Promedio de pasajeros para el día {dia + 1}: {promedio}")
print(f"Promedio general de pasajeros: {promedio_total}")
