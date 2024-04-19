def calcular_desglose(salario):
    denominaciones = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    desglose = {}
    for denominacion in denominaciones:
        cantidad = salario // denominacion
        salario -= cantidad * denominacion
        desglose[denominacion] = cantidad
    return desglose

def acumular_desgloses(desgloses):
    desglose_total = {}
    for desglose in desgloses:
        for denominacion, cantidad in desglose.items():
            if denominacion in desglose_total:
                desglose_total[denominacion] += cantidad
            else:
                desglose_total[denominacion] = cantidad
    return desglose_total

def escribir_resultados(desglose_total):
    with open("resultados_desglose.txt", "w") as file:
        file.write("Desglose acumulado de todos los jugadores:\n")
        for denominacion, cantidad in desglose_total.items():
            file.write(f"Denominacion {denominacion}: Cantidad {cantidad}\n")
if __name__ == "__main__":
    jugadores = int(input("Ingrese la cantidad de jugadores: "))
    salarios = []
    desgloses = []
    for jugador in range(1, jugadores + 1):
        salario = float(input(f"Ingrese el salario del jugador {jugador}: ₡"))
        salarios.append(salario)
        desglose = calcular_desglose(salario)
        desgloses.append(desglose)
    desglose_total = acumular_desgloses(desgloses)
    escribir_resultados(desglose_total)
    print("El desglose acumulado ha sido guardado en el archivo 'resultados.txt'.")
