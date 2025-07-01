import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys
import os
from PIL import Image, ImageTk

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

        self.grades = {
                            "Ingles": "base",
                            "Matematicas": "base",
                            "Ciencias Sociales": "base",
                            "Ciencias Naturales": "base"
                            }


        #Frame 1
        self.frame1 = tk.Frame(self)
        self.frame1.grid(column=0, row=0)
        
        #Columna 1:
        tk.Label(self.frame1, text="Nombres: ", font=("Arial", 14)).grid(column=0, row=0, padx=5, pady=5)
        tk.Label(self.frame1, text="Apellidos:", font=("Arial", 14)).grid(column=0, row=1, padx=5, pady=5)
        tk.Label(self.frame1, text="Edad:", font=("Arial", 14)).grid(column=0, row=2, padx=5, pady=5)
        tk.Label(self.frame1, text="curso:", font=("Arial", 14)).grid(column=0, row=3, padx=5, pady=5)
        tk.Label(self.frame1, text="Genero:", font=("Arial", 14)).grid(column=0, row=4, padx=5, pady=5)
        tk.Label(self.frame1, text="Materias:", font=("Arial", 14)).grid(column=0, row=5, padx=5, pady=5)
        tk.Button(self.frame1, text="Imagen", font=("Arial", 14), command=self.get_image).grid(column=0, row=6, padx=5, pady=5)
        
        #Columna 2:
        self.name = tk.Entry(self.frame1)
        self.name.grid(column=1, row=0, padx=5)
        self.last_name = tk.Entry(self.frame1)
        self.last_name.grid(column=1, row=1, padx=5)
        self.age = tk.Entry(self.frame1)
        self.age.grid(column=1, row=2, padx=5)
        self.degree = tk.Entry(self.frame1)
        self.degree.grid(column=1, row=3, padx=5)        
        self.gender = ("Masculino", "Femenino", "Otro")
        self.option_gender = ttk.Combobox(self.frame1, values=self.gender, state="readonly")
        self.option_gender.grid(column=1, row=4)
        self.subject = ("Ingles", "Matematicas", "Ciencias Naturales", "Ciencias Sociales")
        self.option_subject = ttk.Combobox(self.frame1, values=self.subject, state="readonly")
        self.option_subject.grid(column=1, row=5)

        #Columna 3
        self.subject = tk.Entry(self.frame1, width=5)
        self.subject.grid(column=2, row=5, padx=5)

        #Columna 4
        self.grade = tk.Button(self.frame1, text="Guardar", font=("Arial", 8), command=self.save_grade)
        self.grade.grid(column=3, row=5)


        #Frame 2
        self.frame2 = tk.Frame(self)
        self.frame2.grid(column=0, row=1)
        tk.Label(self.frame2, text="").grid(column=0, row=0, padx=5)
        tk.Label(self.frame2, text="").grid(column=0, row=1, padx=5)
        tk.Button(self.frame2, text="Registrar", font=("Arial", 14), command=self.save_data).grid(column=1, row=8, padx=5)
        tk.Button(self.frame2, text="Volver", font=("Arial", 14), command=self.go_back).grid(column=0, row=8, padx=5)
         


    def go_back(self):
        self.withdraw()
        CentralWindow()
    


    def save_data(self):
        name = self.name.get().strip().title()
        last_name = self.last_name.get().strip().title()
        age = self.age.get()
        degree = self.degree.get()
        grades = self.grades

        if not all([name, last_name, age, degree]):
            messagebox.showerror("Error", "Datos insuficientes")

        else:
            for clave, valor in grades.items():
                if valor == "base":
                    messagebox.showerror("Error", f"Falta por ingresar {clave}")
                    break     
           
    


    def get_image(self, aux=None):
        rout = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp")])

        if not rout:
            messagebox.showerror("Error", "Falta imagen")  

        image = Image.open(resource_path(rout))
        image.thumbnail((150, 150))
        photo = ImageTk.PhotoImage(image)
        logo = tk.Label(self.frame1, image=photo)
        logo.image = photo
        logo.grid(column=1, row=6)
    

    def save_grade(self):
        subject = self.option_subject.get().strip()
        grade = self.subject.get().strip()

        if not subject or not grade:
            messagebox.showerror("Error", "Informacion insuficiente")

        try:
            grade = int(grade)
            self.grades[subject] = grade         
        
        except ValueError:
            messagebox.showerror("Error", "Valor invalido")
        
        


    
        
if __name__ == "__main__":
    app = CentralWindow()
    app.mainloop()
    
        
        

if __name__ == "__main__":
    app = CentralWindow()
    app.mainloop()
    
