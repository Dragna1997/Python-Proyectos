import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "agenda.json"

def cargar_agenda():
    if not os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def guardar_agenda():
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(agenda, f, ensure_ascii=False, indent=2)
    except IOError:
        messagebox.showerror("Error", "No se pudo guardar la agenda en disco.")

def refrescar_lista():
    listbox.delete(0, tk.END)
    for nombre in sorted(agenda.keys(), key=lambda s: s.lower()):
        tel = agenda[nombre].get("telefono", "")
        mail = agenda[nombre].get("correo", "")
        listbox.insert(tk.END, f"{nombre} — {tel} — {mail}")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_correo.delete(0, tk.END)

def agregar_contacto():
    nombre = entry_nombre.get().strip()
    telefono = entry_telefono.get().strip()
    correo = entry_correo.get().strip()

    if not nombre:
        messagebox.showwarning("Aviso", "El nombre es obligatorio.")
        return

    # Guardamos o actualizamos
    agenda[nombre] = {"telefono": telefono, "correo": correo}
    guardar_agenda()
    refrescar_lista()
    limpiar_campos()

def buscar_contacto():
    termino = entry_nombre.get().strip()
    if not termino:
        messagebox.showinfo("Buscar", "Escribí el nombre a buscar en el campo Nombre.")
        return

    # búsqueda case-insensitive (coincidencia exacta o parcial)
    encontrados = {n: v for n, v in agenda.items() if termino.lower() in n.lower()}
    if not encontrados:
        messagebox.showinfo("Buscar", "No se encontraron contactos.")
        return

    # Si hay varios, mostrar el primero en la lista y rellenar campos
    nombres = sorted(encontrados.keys(), key=lambda s: s.lower())
    elegido = nombres[0]
    datos = agenda[elegido]
    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, elegido)
    entry_telefono.delete(0, tk.END)
    entry_telefono.insert(0, datos.get("telefono", ""))
    entry_correo.delete(0, tk.END)
    entry_correo.insert(0, datos.get("correo", ""))

    # Seleccionar en la listbox
    for i in range(listbox.size()):
        if listbox.get(i).startswith(elegido + " " ) or listbox.get(i).startswith(elegido + "—") or listbox.get(i).startswith(elegido + " —"):
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(i)
            listbox.see(i)
            break

def borrar_contacto():
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showinfo("Borrar", "Escribí el nombre del contacto a borrar en el campo Nombre.")
        return

    # buscar coincidencias exactas case-insensitive
    matches = [n for n in agenda.keys() if n.lower() == nombre.lower()]
    if not matches:
        messagebox.showinfo("Borrar", "No se encontró un contacto con ese nombre exacto.")
        return

    nombre_real = matches[0]
    if messagebox.askyesno("Confirmar", f"¿Querés borrar '{nombre_real}'?"):
        del agenda[nombre_real]
        guardar_agenda()
        refrescar_lista()
        limpiar_campos()

def seleccionar_desde_lista(_):
    sel = listbox.curselection()
    if not sel:
        return
    texto = listbox.get(sel[0])
    # formato: "Nombre — telefono — correo"
    nombre = texto.split("—")[0].strip()
    datos = agenda.get(nombre, {})
    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, nombre)
    entry_telefono.delete(0, tk.END)
    entry_telefono.insert(0, datos.get("telefono", ""))
    entry_correo.delete(0, tk.END)
    entry_correo.insert(0, datos.get("correo", ""))

# --- UI ---
root = tk.Tk()
root.title("Agenda de Contactos")
root.geometry("520x380")
root.resizable(False, False)

frame_inputs = tk.Frame(root, padx=10, pady=10)
frame_inputs.pack(fill="x")

tk.Label(frame_inputs, text="Nombre:", width=10, anchor="w").grid(row=0, column=0, pady=4)
entry_nombre = tk.Entry(frame_inputs, width=40)
entry_nombre.grid(row=0, column=1, pady=4, columnspan=3)

tk.Label(frame_inputs, text="Teléfono:", width=10, anchor="w").grid(row=1, column=0, pady=4)
entry_telefono = tk.Entry(frame_inputs, width=40)
entry_telefono.grid(row=1, column=1, pady=4, columnspan=3)

tk.Label(frame_inputs, text="Correo:", width=10, anchor="w").grid(row=2, column=0, pady=4)
entry_correo = tk.Entry(frame_inputs, width=40)
entry_correo.grid(row=2, column=1, pady=4, columnspan=3)

frame_buttons = tk.Frame(root, padx=10)
frame_buttons.pack(fill="x")

btn_add = tk.Button(frame_buttons, text="Agregar / Actualizar", width=18, command=agregar_contacto)
btn_add.grid(row=0, column=0, padx=5, pady=8)

btn_search = tk.Button(frame_buttons, text="Buscar (por nombre)", width=18, command=buscar_contacto)
btn_search.grid(row=0, column=1, padx=5, pady=8)

btn_delete = tk.Button(frame_buttons, text="Borrar (nombre exacto)", width=18, command=borrar_contacto)
btn_delete.grid(row=0, column=2, padx=5, pady=8)

frame_list = tk.Frame(root, padx=10, pady=8)
frame_list.pack(fill="both", expand=True)

listbox = tk.Listbox(frame_list, height=10, width=70)
listbox.pack(side="left", fill="both", expand=True)
listbox.bind("<<ListboxSelect>>", seleccionar_desde_lista)

scroll = tk.Scrollbar(frame_list, command=listbox.yview)
scroll.pack(side="right", fill="y")
listbox.config(yscrollcommand=scroll.set)

# Cargar agenda y mostrar
agenda = cargar_agenda()
refrescar_lista()

root.mainloop()