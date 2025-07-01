import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

frame = tk.Frame(root, bg="lightgray")
frame.grid(row=0, column=0, sticky="nsew")

boton = tk.Button(frame, text="Abajo")
boton.grid(row=0, column=0, sticky="s")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()