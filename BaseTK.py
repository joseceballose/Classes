from tkinter import *

# crear dos columnas para ingresar el nombre y la edad de una persona


class BaseTK:
    def __init__(self, win):
        self.win = win
        self.win.title("Prueba")
        self.win.geometry("450x270")
        self.win.configure(bg = "grey")

        self._inputName = StringVar()

    def command(self, value):
        print(value)

    def operation(self, value):
        print(value)

    def create_widgets(self):
        label = Label(self.win, text="Nombre", bg="grey", fg="black", font=("Arial", 12))
        label.grid(row=0, column=4, padx=5, pady=5)
        
        displayName = Entry(self.win, bg="white", fg="black", font=("Arial", 12), textvariable=self._inputName, justify="center")

        buttons = [
            ("7", 2, 0, self.command),("8", 2, 1, self.command),("9", 2, 2, self.command),("/", 2, 3, self.operation),
            ("4", 3, 0),( "5", 3, 1),( "6", 3, 2),( "-", 3, 3),
            ("1", 4, 0),( "2", 4, 1),( "3", 4, 2),( "+", 4, 3),
            ("+/-", 5, 0),( "0", 5, 1),( ".", 5, 2),( "=", 5, 3),
            
        ]

        for (text, row, column) in buttons:
            button = Button(self.win, text=text, bg="grey", fg="black", font=("Arial", 12))
            button.grid(row=row, column=column, padx=5, pady=5)

if __name__ == "__main__":
    win = Tk()
    app = BaseTK(win)
    win.mainloop()