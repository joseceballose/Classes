import tkinter as tk

win = tk.Tk()
win.geometry("800x600")  # Puedes ajustar el tamaño de la ventana según tus necesidades

# Crear un cuadro de texto en la parte superior
cuadro_texto = tk.Label(win, font=("Helvetica", 16), text="")
cuadro_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

# Lista de botones de la calculadora
botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Función para actualizar el cuadro de texto
def function(text):
    if text == "=":
        try:
            # Evaluar la expresión matemática contenida en el cuadro de texto
            result = str(eval(cuadro_texto.cget("text")))
            cuadro_texto.config(text=result)
        except Exception as e:
            # Manejar cualquier error de evaluación y mostrar el error en el cuadro de texto
            cuadro_texto.config(text="Error")
    else:
        # Concatenar el nuevo texto al texto existente en el cuadro de texto
        new_text = cuadro_texto.cget("text") + text
        cuadro_texto.config(text=new_text)

# Crear y colocar los botones en la interfaz
for row, filas in enumerate(botones):
    for column, text in enumerate(filas):
        button = tk.Button(win, text=f"{text}", command=lambda t=text: function(t))
        button.grid(row=row+1, column=column, padx=5, pady=5, sticky="nsew")  # Desplazar las filas hacia abajo
        win.grid_rowconfigure(row+1, weight=1)
        win.grid_columnconfigure(column, weight=1)

if __name__ == "__main__":
    win.mainloop()

