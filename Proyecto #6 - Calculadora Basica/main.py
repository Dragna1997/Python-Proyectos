import tkinter as tk

# Función para agregar números o símbolos al campo de entrada
def click_boton(valor):
    entrada_texto.set(entrada_texto.get() + str(valor))

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.set(str(resultado))
    except (SyntaxError, ZeroDivisionError, NameError):
        entrada_texto.set("Error")

# Función para borrar
def borrar():
    entrada_texto.set("")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.resizable(False, False)

# Variable para mostrar texto
entrada_texto = tk.StringVar()

# Campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 20), textvariable=entrada_texto, justify="right")
entrada.pack(fill="both", ipadx=8, ipady=8, pady=10, padx=10)

# Frame para botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

# Lista de botones
botones = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 2), ("=", 3, 3)
]

# Crear botones
for (texto, fila, columna) in botones:
    if texto == "=":
        tk.Button(frame_botones, text=texto, width=5, height=2,
                  command=calcular).grid(row=fila, column=columna, padx=5, pady=5)
    else:
        tk.Button(frame_botones, text=texto, width=5, height=2,
                  command=lambda t=texto: click_boton(t)).grid(row=fila, column=columna, padx=5, pady=5)

# Botón borrar
tk.Button(ventana, text="Borrar", width=25, height=2, command=borrar).pack(pady=5)

# Ejecutar ventana
ventana.mainloop()