def obtener_cantidad_actual():
    try:
        with open("cantidad_personas.txt", "r") as archivo:
            return int(archivo.readline().strip())
    except FileNotFoundError:
        return 0

def actualizar_cantidad_actual(cantidad):
    with open("cantidad_personas.txt", "w") as archivo:
        archivo.write(str(cantidad))

def registrar_ingreso():
    cantidad_actual = obtener_cantidad_actual()
    if cantidad_actual < 10:
        nombre = input("Ingrese el nombre de la persona que ingresa: ")
        cantidad_actual += 1
        actualizar_cantidad_actual(cantidad_actual)
        print("Se ha registrado el ingreso de una persona.")
        with open("registro_ingresos.txt", "a") as archivo:
            archivo.write(f"{nombre}\n")
    else:
        print("El abastecedor esta en su capacidad máxima.")

def registrar_egreso():
    cantidad_actual = obtener_cantidad_actual()
    if cantidad_actual > 0:
        cantidad_actual -= 1
        actualizar_cantidad_actual(cantidad_actual)
        print("Se ha registrado el egreso de una persona.")
    else:
        print("No hay campo para mas personas en el abastecedor para registrar egreso.")

if __name__ == "__main__":
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar ingreso de persona")
        print("2. Registrar egreso de persona")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            registrar_ingreso()
        elif opcion == "2":
            registrar_egreso()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
