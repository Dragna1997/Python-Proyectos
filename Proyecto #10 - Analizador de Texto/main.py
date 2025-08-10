import tkinter as tk
from tkinter import messagebox
from collections import Counter
import re
import matplotlib.pyplot as plt


def analizar_texto():
    texto = entrada_texto.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning("Advertencia", "Por favor ingrese un texto.")
        return

    # Contar letras
    letras = len(re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÑñ]", texto))

    # Contar palabras
    palabras = re.findall(r"\b\w+\b", texto.lower())
    cantidad_palabras = len(palabras)

    # Contar frases
    frases = re.split(r"[.!?]+", texto)
    frases = [f.strip() for f in frases if f.strip()]
    cantidad_frases = len(frases)

    # Top 5 palabras más frecuentes
    contador = Counter(palabras)
    top_5 = contador.most_common(5)

    # Mostrar resultados
    resultado_var.set(
        f"📄 Letras: {letras}\n"
        f"📝 Palabras: {cantidad_palabras}\n"
        f"📢 Frases: {cantidad_frases}\n"
        f"⭐ Top 5 palabras: {', '.join([f'{p} ({c})' for p, c in top_5])}"
    )

    # Mostrar gráfico
    if top_5:
        palabras_grafico, frecuencias = zip(*top_5)
        plt.figure(figsize=(6, 4))
        plt.bar(palabras_grafico, frecuencias, color="skyblue")
        plt.title("Top 5 palabras más frecuentes")
        plt.xlabel("Palabras")
        plt.ylabel("Frecuencia")
        plt.show()


# ---------------- INTERFAZ ----------------
root = tk.Tk()
root.title("Analizador de Texto Avanzado")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Ingrese su texto:").grid(row=0, column=0, sticky="w")

entrada_texto = tk.Text(frame, width=50, height=10)
entrada_texto.grid(row=1, column=0, pady=5)

tk.Button(frame, text="Analizar", command=analizar_texto).grid(row=2, column=0, pady=5)

resultado_var = tk.StringVar()
tk.Label(frame, textvariable=resultado_var, justify="left").grid(row=3, column=0, pady=10, sticky="w")

root.mainloop()