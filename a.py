import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Selección única con Combobox")

opciones = ["Python", "Java", "C++", "JavaScript"]

combo = ttk.Combobox(root, values=opciones, state="readonly")
combo.set("Selecciona un lenguaje")
combo.pack(padx=10, pady=10)

def mostrar():
    print("Seleccionado:", combo.get())

ttk.Button(root, text="Mostrar selección", command=mostrar).pack()

root.mainloop()