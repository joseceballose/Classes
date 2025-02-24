from tkinter import *
import tkinter as tk

class Calculadora():
    def __init__(self, win):
        self.win = win
        self.win.title("Calculadora")
        self.win.geometry("450x300")
        self.win.configure(bg="#2E2E2E")

        self.Widgets()
            
    def show(self, text):
        if text == "=":
            try:
                result = str(eval(self.cuadro_texto.cget("text")))
                self.cuadro_texto.config(text=result)
            except Exception as e:
                self.cuadro_texto.config(text="Error")
        elif text == "CE":
            try:
                self.cuadro_texto.config(text="")
            except Exception as e:
                self.cuadro_texto.config(text="error")
                            
        else:
            new_text = self.cuadro_texto.cget("text") + text
            self.cuadro_texto.config(text=new_text)
        
    def Widgets(self):
        self.cuadro_texto = tk.Label(win, font=("Helvetica", 16), text="", )
        self.cuadro_texto.grid(row=0, column=1, columnspan=3, padx=2, pady=2, sticky="nsew")
        self.clear_button = tk.Button(win, text="CE", command=lambda: self.show("CE"),  bg="grey", fg="white",).grid(row=0, column=0, padx=2, pady=2)

        botones = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row, filas in enumerate(botones):
            for column, text in enumerate(filas):
                button = tk.Button(win, text=f"{text}", bg="grey", fg="white", command= lambda t=text: self.show(t))
                button.grid(row=row+1, column=column, padx=2, pady=2, sticky="nsew")
                win.grid_rowconfigure(row+1, weight=1)
                win.grid_columnconfigure(column, weight=1)

if __name__ == "__main__":
    win = Tk()
    app = Calculadora(win)
    win.mainloop()
    
