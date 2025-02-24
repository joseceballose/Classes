import tkinter as tk
win = tk.Tk()
win.geometry("")
botones = [
    ['a'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]


for row, filas in enumerate(botones):
    for column, text in enumerate(filas):
        button = tk.Button(win, text=f"{text}")
        if text == 'a':
            text = tk.Label(win, text="operacion")
            text.grid(row=row, column=column, columnspan=4, padx=5, pady=5, sticky="nsew")
        else:
            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
        win.grid_rowconfigure(row, weight=1)
        win.grid_columnconfigure(column, weight=1)


if __name__ == "__main__":
    win.mainloop()