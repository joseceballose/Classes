import tkinter

win = tkinter.Tk()

win.geometry("450x270")
win.configure(bg = "#fff")
win.title("Text Widget")
text = tkinter.Entry()

def funcion_edad():
    window = tkinter.Tk()
    window.geometry("200x150")
    boxtext = tkinter.Entry(window)
    boxtext.pack()
    
    def mostrar():
       return print(boxtext.get())
    boton1 = tkinter.Button(window, text="click", command=mostrar)
    boton1.pack()

boton = tkinter.Button(win, text="click", command=funcion_edad)
boton.pack()

tkinter.mainloop()