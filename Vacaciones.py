""" 
Una empresa requiere un sistema para calcular los días de vacaciones que le corresponden a sus empleados según su antigüedad y puesto.
El sistema debe permitir ingresar el nombre del empleado, su antigüedad en años y su puesto (Gerente, Supervisor, Empleado). Según estos datos, el sistema calculará los días de vacaciones correspondientes de la siguiente manera:
- Gerente: 12 días por 1 de antigüedad, 24 días por 2 años a 5 años de antigüedad, y 36 días por más de 5 años de antigüedad.
- Supervisor: 10 días por 1 de antigüedad, 20 días por 2 años a 5 años de antigüedad, y 30 días por más de 5 años de antigüedad.
- Empleado: 6 días por 1 año de antigüedad, 14 días por 2 años a 5 años de antigüedad, y 20 días por más de 5 años de antigüedad.


El sistema contará de 3 interfaces gráficas tkinter:
1. Una ventana principal que tendrá el logo de la empresa, icono de la aplicación, un campo donde se ingresará el nombre de la persona qué ingresará los datos, un botón para ingresar y un pie de pagina que contendrá el nombre de la empresa y el año actual.
2. Otra pantalla que será la de terminos y condiciones, donde se mostrará un texto con los términos y condiciones de la empresa, un checkbox para aceptar los términos y un botón para continuar, en caso de no aceptar, se mostrará un mensaje de error y no permitirá continuar.
3. Una pantalla final donde sé ingresan los nombres y apellidos de los empleados, su antigüedad y puesto, y se calcularán los días de vacaciones correspondientes. Esta pantalla tendrá un botón para calcular las vacaciones y otro para salir del sistema. Además, se mostrará un mensaje con el resultado del cálculo. recuerda qué pára el puesto debe ser seleccionado de una lista desplegable.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk

#
NAME_ENTERPRISE = 'PEPSI S.A.S'
CURRECT_YEAR = datetime.now().year


def calculate_values(puesto, antiguedad): 
    


class WindowCentral(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sitema Vacacional Pepsi")
        self.geometry("400x350")
        self.resizable(False, False)
        self.iconbitmap('icono.ico')
        img = Image.open('Pepsi.png')
        img = img.resize((100, 100))
        logo_img = ImageTk.PhotoImage(img)
        logo = tk.Label(self, image=logo_img)
        logo.image = logo_img
        logo.pack(pady=10)
        tk.Label(self, text="Bienvenido al sistema Vacacional",font=('Arial', 18)).pack(pady=5)
        tk.Label(self, text="Nombre de usuario:",).pack(pady=5)
        self.name_user = tk.Entry(self)
        self.name_user.pack(pady=5)
        tk.Button(self, text='Ingresar', command=self.login).pack(pady=10)

        pie = tk.Label(self,text=f"{NAME_ENTERPRISE} - {CURRECT_YEAR}", font=('Arial', 9), fg="gray")
        pie.pack(side="bottom", pady= 10)

    
    def login(self):
        name = self.name_user.get().strip()
        if not name: 
            messagebox.showerror("Error", "Por favor ingresa tú nombre")
            return
        self.withdraw()
        WindowTerms(self,name)

class WindowTerms(tk.Toplevel):
    def __init__(self, master, name_user):
        super().__init__(master)
        self.title('Términos y condiciones')
        self.geometry("400x300")
        self.iconbitmap('icono.ico')
        self.resizable(False, False)
        self.name_user = name_user
        text = f"{name_user} Aceptas qué al usar la aplicación debe ingresar datos personales qué serán     unicamenten usados para el cáculo den vacaciones según la politica de la empresa"
        tk.Label(self, text=text, wraplength=350, justify='left').pack(pady=15)
        self.term = tk.BooleanVar()
        tk.Checkbutton(self, text="Acepto los terminos", variable=self.term).pack(pady=10)
        tk.Button(self, text='Continuar', command=self.nextSteep).pack(pady=10)

    def nextSteep(self): 
        if not self.term.get(): 
            messagebox.showerror("Error", "Debes aceptar los terminos")
            return

if __name__ == "__main__":
    app = WindowCentral()
    app.mainloop()