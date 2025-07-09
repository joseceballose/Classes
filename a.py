import tkinter as tk
from tkinter import ttk

def mostrar_opcion(event):
    seleccion = combo.get()
    label_resultado.config(text=f"La opción fue: {seleccion}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Combobox")
ventana.geometry("300x200")

# Combobox con opciones
opciones = ["A", "B", "C", "X"]
combo = ttk.Combobox(ventana, values=opciones, state="readonly")
combo.set("Seleccione una opción...")
combo.pack(pady=10)

# Label que se actualizará
label_resultado = tk.Label(ventana, text="La opcion fue: ")
label_resultado.pack(pady=10)

# Asociar evento
combo.bind("<<ComboboxSelected>>", mostrar_opcion)

ventana.mainloop()