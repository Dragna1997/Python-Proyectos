'''
Proyecto #1 - Adivina el Número Secreto

Desarrollar un juego interactivo llamado "Adivina el Número Secreto"

El programa seleccionará aleatoriamente un número entre un rango especificado y
el jugador deberá adivinar el "número secreto" en un numero limitado de intentos
'''
import random

print("Bienvenido a 'Adivina el Número Secreto'")
print("He Seleccionado un Número Entre 1 y 100. ¡Adivina cúal es!")

numero_secreto = random.randint(1, 100)
intentos_maximos = 10
adivinanza = 0

for intento in range(1, intentos_maximos + 1):
    print(f"\nIntento {intento}/{intentos_maximos}")

    try:

        adivinanza = int(input("Prueba tu Suerte, Intenta Adivinar el Número Secreto: "))

        if adivinanza < numero_secreto:
            print("El Número es mayor.")
        elif adivinanza > numero_secreto:
            print("El Numero es Menor.")
        else:
            print(f"¡Felicidades! ¡Has Adivinado el Número Secreto ({numero_secreto}) en {intento} intentos!")
            break

    except ValueError:
        print("Debes Ingresar un Número Entero.")
    except Exception as e:
        print(f"Debes Ingresar un Número Entero: {e}")

if adivinanza != numero_secreto:
    print(f"\nLo Siento, el Número secreto era {numero_secreto} ¡Mejor Suerte la Proxima Vez!")

input("Presiona Enter para Salir.")
