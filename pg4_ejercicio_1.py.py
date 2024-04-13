def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio
#Funcion para calcular el promedio de los estudiantes
def calcular_porcentaje_aprobados(notas):
    aprobados = sum(1 for nota in notas if nota >= 70)
    porcentaje = (aprobados / len(notas)) * 100
    return porcentaje

curso_programacion = {
    "Estudiante1": [80, 75, 85, 90, 88],
    "Estudiante2": [70, 65, 75, 80, 72],
    "Estudiante3": [90, 85, 95, 88, 92],
    "Estudiante4": [60, 75, 70, 68, 72],
    "Estudiante5": [85, 90, 88, 92, 86]
}
#Funcion para cacular el promedio general de los estudiantes
notas_totales = [nota for notas in curso_programacion.values() for nota in notas]
promedio_general = calcular_promedio(notas_totales)
print("Promedio general del curso:", promedio_general)

for estudiante, notas in curso_programacion.items():
    promedio_estudiante = calcular_promedio(notas)
    print(f"Promedio de {estudiante}: {promedio_estudiante}")
 
porcentaje_aprobados = calcular_porcentaje_aprobados(notas_totales)
print("Porcentaje de estudiantes aprobados:", porcentaje_aprobados)
