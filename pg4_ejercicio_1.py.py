def ingresar_notas():
    notas = []
    for i in range(3):  # 3 cursos
        curso_notas = []
        print(f"Ingrese las notas del curso {i + 1}:")
        for j in range(5):  # 5 estudiantes por curso
            nota = float(input(f"Nota del estudiante {j + 1}: "))
            curso_notas.append(nota)
        notas.append(curso_notas)
    return notas

def calcular_promedio_global(notas):
    total_notas = sum([nota for curso in notas for nota in curso])
    total_estudiantes = sum([len(curso) for curso in notas])
    return total_notas / total_estudiantes

def calcular_promedio_por_curso(notas):
    promedios = []
    for i, curso in enumerate(notas):
        promedio_curso = sum(curso) / len(curso)
        promedios.append(promedio_curso)
    return promedios

def calcular_porcentaje_aprobados(notas):
    aprobados_por_curso = []
    for curso in notas:
        aprobados = sum(1 for nota in curso if nota >= 70)
        porcentaje_aprobados = (aprobados / len(curso)) * 100
        aprobados_por_curso.append(porcentaje_aprobados)
    return aprobados_por_curso

def obtener_max_min_por_curso(notas):
    max_min_por_curso = []
    for curso in notas:
        max_nota = max(curso)
        min_nota = min(curso)
        max_min_por_curso.append((max_nota, min_nota))
    return max_min_por_curso

def escribir_resultados(notas):
    with open("resultados.txt", "w") as file:
        file.write("Resultados de Control de Notas\n\n")

        file.write("1. Nota promedio global:\n")
        file.write(str(calcular_promedio_global(notas)) + "\n\n")

        file.write("2. Promedio por curso:\n")
        for i, promedio in enumerate(calcular_promedio_por_curso(notas)):
            file.write(f"Curso {i + 1}: {promedio}\n")
        file.write("\n")

        file.write("3. Porcentaje de estudiantes aprobados por curso:\n")
        for i, porcentaje in enumerate(calcular_porcentaje_aprobados(notas)):
            file.write(f"Curso {i + 1}: {porcentaje}%\n")
        file.write("\n")

        file.write("4. Nota maxima y minima por curso:\n")
        for i, (max_nota, min_nota) in enumerate(obtener_max_min_por_curso(notas)):
            file.write(f"Curso {i + 1}: maxima - {max_nota}, minima - {min_nota}\n")

if __name__ == "__main__":
    notas = ingresar_notas()
    escribir_resultados(notas)
    print("Los resultados han sido guardados en el archivo 'resultados.txt'.")
