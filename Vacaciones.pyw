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
import sys
import os

# Función para obtener la ruta correcta de los recursos
def resource_path(relative_path):
    """Obtiene la ruta absoluta de un recurso, funciona tanto en desarrollo como en PyInstaller"""
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


#
NAME_ENTERPRISE = 'PEPSI S.A.S'
CURRECT_YEAR = datetime.now().year


def calculate_values(name, last_name, puesto, antiguedad): 
    if puesto == "Gerente":
        if antiguedad == 1:
            days = 12
        elif antiguedad < 5:
            days = 24
        else:
            days = 36
            
    if puesto == "Supervisor":
        if antiguedad == 1:
            days = 10
        elif antiguedad < 5:
            days = 20
        else:
            days = 30
            
    else:
        if antiguedad == 1:
            days = 6
        elif antiguedad < 5:
            days = 14
        else:
            days = 20
            
    messagebox.showinfo("Informacion", f"{name} {last_name} tiene {days} días de descanso")

class WindowCentral(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sitema Vacacional Pepsi")
        self.geometry("400x350")
        self.resizable(False, False)
        self.iconbitmap(resource_path('icono.ico'))
        img = Image.open(resource_path('Pepsi.png'))
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
        name = self.name_user.get().strip().title()
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
        self.iconbitmap(resource_path('icono.ico'))
        self.resizable(False, False)
        self.name_user = name_user
        text = f"{name_user} aceptas qué al usar la aplicación debe ingresar datos personales qué serán unicamenten usados para el cáculo den vacaciones según la politica de la empresa"
        tk.Label(self, text=text, wraplength=350, justify='center').pack(pady=15)
        self.term = tk.BooleanVar()
        tk.Checkbutton(self, text="Acepto los terminos", variable=self.term, font="5").pack(pady=10)
        tk.Button(self, text='Continuar', command=self.nextSteep).pack(pady=10)

    def nextSteep(self): 
        if not self.term.get(): 
            messagebox.showerror("Error", "Debes aceptar los terminos")
            return
        self.withdraw()
        WindowCalculate(self)


class WindowCalculate(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('Cálculo días de vacaciones')
        self.geometry('400x300')
        self.iconbitmap(resource_path('icono.ico'))
        self.resizable(False, False)

        # Frame 1: Datos personales
        self.frame1 = tk.Frame(self)
        self.frame1.grid(column=0, row=0, padx=5, sticky="w")

        tk.Label(self.frame1, text="Nombres: ", font="Arial, 11").grid(column=0, row=0, padx=5, pady=5)
        self.name = tk.Entry(self.frame1)
        self.name.grid(column=1, row=0)

        tk.Label(self.frame1, text="Apellidos: ", font="Arial, 11").grid(column=0, row=1, padx=5, pady=5)
        self.last_name = tk.Entry(self.frame1)
        self.last_name.grid(column=1, row=1)

        tk.Label(self.frame1, text="Estatus: ", font="Arial, 11").grid(column=0, row=2, padx=5, pady=5)
        self.status = ("Gerente", "Supervisor", "Empleado")
        self.option = ttk.Combobox(self.frame1, values=self.status, state="readonly")
        self.option.grid(column=1, row=2)

        # Frame 2: Antigüedad
        self.frame2 = tk.Frame(self)
        self.frame2.grid(column=0, row=1, padx=5, sticky="w")

        tk.Label(self.frame2, text="Años trabajados: ", font="Arial, 11").grid(column=0, row=0, padx=5, pady=5)
        self.age = tk.Entry(self.frame2)
        self.age.grid(column=1, row=0)

        # Botones
        self.frame3 = tk.Frame(self)
        self.frame3.grid(column=0, row=2, pady=15)

        self.calculate = tk.Button(self.frame3, text="Calcular", command=self.calcular)
        self.calculate.grid(column=2, row=0, padx=10)

        self.exit = tk.Button(self.frame3, text="Salir", command=self.quit)
        self.exit.grid(column=2, row=1, padx=10, pady=10)

    def calcular(self):
        name = self.name.get().strip().title()
        last_name = self.last_name.get().strip().title()
        puesto = self.option.get()
        antiguedad = self.age.get()
        if not name or not last_name or not puesto or not antiguedad:
            messagebox.showerror("error", "Datos insuficientes")
        antiguedad = int(antiguedad)
        if antiguedad < 1:
            messagebox.showerror("error", "Antiguedad insuficiente")
        calculate_values(name, last_name, puesto, antiguedad)

    
       


if __name__ == "__main__":
    app = WindowCentral()
    app.mainloop()