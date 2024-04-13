def calcular_total_pagos(jugadores):
    total = sum(jugadores.values())  # Calcula el total de pagos sumando los salarios de todos los jugadores
    return total

def desglosar_dinero(total):
    denominaciones = [50000, 20000, 10000, 5000, 2000, 1000, 500]
    desglose = {denom: total // denom for denom in denominaciones}
    return desglose

# Diccionario que contiene los nombres de los jugadores y sus salarios
jugadores = {
    "Juan": 1500000,
    "Pedro": 2000000,
    "María": 1800000,
    "Luis": 2200000,
    "Ana": 1900000
}

print("Información de los jugadores:")
for jugador, salario in jugadores.items():
    print(f"{jugador}: ₡{salario}")

cantidad_a_retirar = int(input("Ingrese la cantidad que desea retirar del banco: "))
total_pagos = calcular_total_pagos(jugadores)  # Calcula el total de pago
desglose_dinero = desglosar_dinero(cantidad_a_retirar)  # Hace un desglose de los billetes y monedas

print("\nMonto total a retirar del banco:", cantidad_a_retirar)  # Imprime el monto total a retirar del banco

# Imprime el desglose de billetes y monedas necesarios
print("\nDesglose de billetes y monedas necesarios:")
for denom, cantidad in desglose_dinero.items():
    print(f"{cantidad} billetes de ₡{denom}")
