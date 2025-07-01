import tkinter as tk
from tkinter import ttk, messagebox, filedialog
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

class CentralWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú de inicio")
        self.geometry("300x400")
        tk.Button(self, text="Registrar Estudiante", width=20, height=3, font=(12), command=self.student_register).pack(padx=5, pady=5)
        tk.Button(self, text="Listar Estudiantes", width=20, height=3, font=(12)).pack(padx=5, pady=5)
        tk.Button(self, text="Comparar Estudiantes", width=20, height=3, font=(12)).pack(padx=5, pady=5)
        
    def student_register(self):
        self.withdraw()
        RegisterWindow(self)
            
            
class RegisterWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Registro de estudiante")
        self.geometry("400x500")
        
        #Columna 1:
        tk.Label(self, text="Nombres: ", font=("Arial", 14)).grid(column=0, row=0, padx=5, pady=5)
        tk.Label(self, text="Apellidos:", font=("Arial", 14)).grid(column=0, row=1, padx=5, pady=5)
        tk.Label(self, text="Edad:", font=("Arial", 14)).grid(column=0, row=2, padx=5, pady=5)
        tk.Label(self, text="curso:", font=("Arial", 14)).grid(column=0, row=3, padx=5, pady=5)
        tk.Label(self, text="Genero:", font=("Arial", 14)).grid(column=0, row=4, padx=5, pady=5)
        tk.Button(self, text="Imagen", font=("Arial", 14), command=self.get_image).grid(column=0, row=5, padx=5, pady=5)
        tk.Button(self, text="Registrar", font=("Arial", 14)).grid(column=0, row=6, padx=5, pady=5)
        
        #Columna 2:
        self.name = tk.Entry(self)
        self.name.grid(column=1, row=0, padx=5)
        self.last_name = tk.Entry(self)
        self.last_name.grid(column=1, row=1, padx=5)
        self.age = tk.Entry(self)
        self.age.grid(column=1, row=2, padx=5)
        self.degree = tk.Entry(self)
        self.degree.grid(column=1, row=3, padx=5)        
        self.gender = ("Masculino", "Femenino", "Otro")
        self.option = ttk.Combobox(self, values=self.gender, state="readonly")
        self.option.grid(column=1, row=4)
        tk.Button(self, text="Volver", font=("Arial", 14), command=self.go_back).grid(column=1, padx=5, sticky="s")
         
    def go_back(self):
        self.withdraw()
        CentralWindow()
    
    def save_data(self):
        name = self.name.get().strip().title()
        last_name = self.last_name.get().strip().title()
        age = self.age.get()
        degree = self.degree.get()
        image = self.ima
        
        if not all([name, last_name, age, degree]):
            messagebox.showerror("Error", "Datos insuficientes")            
    
    def get_image(self):
        rout = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp")])
    
        
        

if __name__ == "__main__":
    app = CentralWindow()
    app.mainloop()
    