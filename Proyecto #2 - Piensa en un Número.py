'''
Proyecto #2 - Piensa en un Número

Desarrollar un Juego Interactivo llamado 'Pienssa en un Número'

El usuario debe ser invitado a pensar en un numero secreto, y el programa
intentara adivinarlo haciendo preguntas astutas.
'''
import random

print("Piensa en un Número entre 1 y 100. Yo Tratare de Adivinarlo.")

intentos = 0
adivinanza_minima = 1
adivinanza_maxima = 100
adivinanza_actual = 0

while True:
    intentos += 1
    adivinanza_actual = random.randint(adivinanza_minima, adivinanza_maxima)

    print(f"¿Es {adivinanza_actual} tu número?")
    respuesta = input("Ingresa 'mayor', 'menor' o 'correcto': ").lower()

    if respuesta == "correcto":
        print(f"¡Adiviné tu Número ({adivinanza_actual}) en {intentos} intentos!")
        break
    elif respuesta == "mayor":
        adivinanza_minima = adivinanza_actual + 1
    elif respuesta == "menor":
        adivinanza_maxima = adivinanza_actual - 1
    else:
        print("Respuesta no Válida. Ingrese 'mayor', 'menor' o 'correcto'.")

input("Presiona Enter para salir")
