def capturar_pasajeros():
    pasajeros = []
    for dia in range(1, 6):  # 5 días de la semana
        print(f"Dia {dia}:")
        pasajeros_dia = []
        for servicio in range(1, 5):  # 4 servicios
            while True:
                cantidad = int(input(f"Ingrese la cantidad de pasajeros para el servicio {servicio}: "))
                if cantidad <= 60:
                    pasajeros_dia.append(cantidad)
                    break
                else:
                    print("La cantidad ingresada supera la capacidad máxima del autobús (60 pasajeros).")
        pasajeros.append(pasajeros_dia)
    return pasajeros

def calcular_promedio_por_dia(pasajeros):
    promedios = []
    for dia in pasajeros:
        promedio_dia = sum(dia) / len(dia)
        promedios.append(promedio_dia)
    return promedios

def calcular_promedio_general(pasajeros):
    total_pasajeros = sum(sum(dia) for dia in pasajeros)
    total_dias = len(pasajeros)
    return total_pasajeros / (total_dias * 4)  # 4 servicios por día

def mejor_servicio(pasajeros):
    max_pasajeros = max(sum(dia) for dia in pasajeros)
    for i, dia in enumerate(pasajeros, start=1):
        for j, pasajeros_servicio in enumerate(dia, start=1):
            if sum(dia) == max_pasajeros:
                return f"El mejor servicio es el {j} en el dia {i}"

def momento_menos_pasajeros(pasajeros):
    min_pasajeros = min(sum(dia) for dia in pasajeros)
    for i, dia in enumerate(pasajeros, start=1):
        for j, pasajeros_servicio in enumerate(dia, start=1):
            if sum(dia) == min_pasajeros:
                return f"El momento con menos pasajeros es el servicio {j} en el dia {i}"

def escribir_resultados(promedios_por_dia, promedio_general, mejor_serv, menos_pasajeros):
    with open("resultados.txt", "w") as file:
        file.write("Promedio de pasajeros por dia:\n")
        for i, promedio in enumerate(promedios_por_dia, start=1):
            file.write(f"Dia {i}: {promedio}\n")
        file.write("\n")

        file.write(f"Promedio general de pasajeros: {promedio_general}\n\n")
        file.write(f"{mejor_serv}\n\n")
        file.write(f"{menos_pasajeros}\n")
if __name__ == "__main__":
    pasajeros = capturar_pasajeros()
    promedios_por_dia = calcular_promedio_por_dia(pasajeros)
    promedio_general = calcular_promedio_general(pasajeros)
    mejor_serv = mejor_servicio(pasajeros)
    menos_pasajeros = momento_menos_pasajeros(pasajeros)
    escribir_resultados(promedios_por_dia, promedio_general, mejor_serv, menos_pasajeros)
    print("Los resultados han sido guardados en el archivo 'resultados.txt'.")
