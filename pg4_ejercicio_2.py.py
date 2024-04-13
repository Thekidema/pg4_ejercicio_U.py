# Funcion para interpretar  la cantida de pasajeros de cada servicio  en base a una semana 
def capturar_pasajeros():
    pasajeros = []
    for dia in range(5):
        pasajeros_dia = [int(input(f"Ingrese pasajeros para día {dia + 1}, servicio {servicio + 1}: ")) for servicio in range(4) if (cantidad := int(input(f"Ingrese pasajeros para día {dia + 1}, servicio {servicio + 1}: "))) <= 60]
        pasajeros.append(pasajeros_dia)
    return pasajeros

# Funcion que sirve para calcular el promedio de las personas o pasajeros 
def promedio_por_dia(pasajeros):
    return [sum(dia) / len(dia) for dia in pasajeros]

# }Esta  funcion nos sirve   para calcular el promedio de general de los pasajeros 
def promedio_general(pasajeros):
    return sum(sum(dia) for dia in pasajeros) / (len(pasajeros) * len(pasajeros[0]))
# Captura de datos
pasajeros_semana = capturar_pasajeros()
# Procesamiento de los datos
promedios_dia = promedio_por_dia(pasajeros_semana)
promedio_total = promedio_general(pasajeros_semana)
# Resultados
print("\n--- Resultados ---")
for dia, promedio in enumerate(promedios_dia):
    print(f"Promedio de pasajeros para el día {dia + 1}: {promedio}")
print(f"Promedio general de pasajeros: {promedio_total}")                 