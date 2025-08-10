import tkinter as tk

# Funciones de conversión
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def km_a_millas(km):
    return km * 0.621371

def millas_a_km(mi):
    return mi / 0.621371

def pesos_a_dolares(pesos, tasa=900):  # Cambiá la tasa según el cambio actual
    return pesos / tasa

def dolares_a_pesos(dolares, tasa=900):
    return dolares * tasa

# Función para manejar conversiones
def convertir():
    try:
        valor = float(entrada_valor.get())
        tipo = variable_conversion.get()

        if tipo == "Celsius → Fahrenheit":
            resultado.set(f"{celsius_a_fahrenheit(valor):.2f} °F")
        elif tipo == "Fahrenheit → Celsius":
            resultado.set(f"{fahrenheit_a_celsius(valor):.2f} °C")
        elif tipo == "Kilómetros → Millas":
            resultado.set(f"{km_a_millas(valor):.2f} mi")
        elif tipo == "Millas → Kilómetros":
            resultado.set(f"{millas_a_km(valor):.2f} km")
        elif tipo == "Pesos → Dólares":
            resultado.set(f"${pesos_a_dolares(valor):.2f} USD")
        elif tipo == "Dólares → Pesos":
            resultado.set(f"${dolares_a_pesos(valor):.2f} ARS")
    except ValueError:
        resultado.set("Error: valor inválido")

# Crear ventana
ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Campo de entrada
tk.Label(ventana, text="Valor a convertir:", font=("Arial", 12)).pack(pady=5)
entrada_valor = tk.Entry(ventana, font=("Arial", 14))
entrada_valor.pack(pady=5)

# Lista de conversiones
opciones = [
    "Celsius → Fahrenheit",
    "Fahrenheit → Celsius",
    "Kilómetros → Millas",
    "Millas → Kilómetros",
    "Pesos → Dólares",
    "Dólares → Pesos"
]

variable_conversion = tk.StringVar(ventana)
variable_conversion.set(opciones[0])  # Valor inicial
tk.OptionMenu(ventana, variable_conversion, *opciones).pack(pady=5)

# Botón de conversión
tk.Button(ventana, text="Convertir", font=("Arial", 12), command=convertir).pack(pady=10)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 16, "bold")).pack(pady=10)

# Ejecutar ventana
ventana.mainloop()