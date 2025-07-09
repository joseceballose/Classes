import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys
import os
from PIL import Image, ImageTk
from uuid import uuid4
import json
import shutil

# Función para obtener la ruta correcta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Funcíon para organizar los datos --> diccionario
def organize_data(name, last_name, age, degree, grades, image_rout):
    extention = os.path.splitext(image_rout)[1]
    Id = f"{uuid4()}{extention}"
    save_image(image_rout, Id)
    data = {
        "name": name,
        "last name": last_name,
        "age": age,
        "degree": degree,
        "grades": grades,
        "image rout": Id,
    }
    return data

# Función para guardar la imagen
def save_image(rout, Id):
    final_folder = "Proyecto Estudiantes/Images"
    os.makedirs(final_folder, exist_ok=True)
    final_rout = os.path.join(final_folder, Id)
    shutil.copy(rout, final_rout)

# Función que recupere la info del JSON
def recover_data():
    file = os.path.join(os.path.abspath("."), "Proyecto Estudiantes")
    os.makedirs(file, exist_ok=True)
    json_rout = os.path.join(file, "Data.json")
    if os.path.exists(json_rout):
         with open(json_rout, "r", encoding="utf-8") as archive:
            try:
                data = json.load(archive)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    return data

# Ventana Principal
class CentralWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú de inicio")
        self.geometry("300x400")

        tk.Button(self, text="Registrar Estudiante", width=20, height=3, font=(12), command=self.student_register).pack(padx=5, pady=5)
        tk.Button(self, text="Listar Estudiantes", width=20, height=3, font=(12), command=self.student_lister).pack(padx=5, pady=5)
        tk.Button(self, text="Comparar Estudiantes", width=20, height=3, font=(12)).pack(padx=5, pady=5)
        
    # Función para abrir RegisterWindow
    def student_register(self):
        self.withdraw()
        RegisterWindow(self)
    
    # Función para abrir ListerWindow
    def student_lister(self):
        self.withdraw()
        data = recover_data()
        ListerWindow(self, data)

# Ventana de registro de estudiantes
class RegisterWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Registro de estudiante")
        self.geometry("400x500")
        self.image_rout = ""
        self.grades = {
            "Ingles": "base",
            "Matematicas": "base",
            "Ciencias Sociales": "base",
            "Ciencias Naturales": "base",
        }

        # Frame 1
        self.frame1 = tk.Frame(self)
        self.frame1.grid(column=0, row=0)
        
        # Columna 1
        tk.Label(self.frame1, text="Nombres: ", font=("Arial", 14)).grid(column=0, row=0, padx=5, pady=5)
        tk.Label(self.frame1, text="Apellidos:", font=("Arial", 14)).grid(column=0, row=1, padx=5, pady=5)
        tk.Label(self.frame1, text="Edad:", font=("Arial", 14)).grid(column=0, row=2, padx=5, pady=5)
        tk.Label(self.frame1, text="curso:", font=("Arial", 14)).grid(column=0, row=3, padx=5, pady=5)
        tk.Label(self.frame1, text="Genero:", font=("Arial", 14)).grid(column=0, row=4, padx=5, pady=5)
        tk.Label(self.frame1, text="Materias:", font=("Arial", 14)).grid(column=0, row=5, padx=5, pady=5)
        tk.Button(self.frame1, text="Imagen", font=("Arial", 14), command=self.get_image).grid(column=0, row=6, padx=5, pady=5)
        
        
        # columna 2
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

        self.subjects = ("Ingles", "Matematicas", "Ciencias Naturales", "Ciencias Sociales")
        self.option_subject = ttk.Combobox(self.frame1, values=self.subjects, state="readonly")
        self.option_subject.grid(column=1, row=5)
        
        # Columna 3
        self.subject = tk.Entry(self.frame1, width=5)
        self.subject.grid(column=2, row=5, padx=5)
        
        # Columna 4
        self.grade = tk.Button(self.frame1, text="Guardar", font=("Arial", 8), command=self.save_grade)
        self.grade.grid(column=3, row=5)
        
        
        # Frame 2
        self.frame2 = tk.Frame(self)
        self.frame2.grid(column=0, row=1)
        
        tk.Label(self.frame2, text="").grid(column=0, row=0, padx=5)
        tk.Label(self.frame2, text="").grid(column=0, row=1, padx=5)

        tk.Button(self.frame2, text="Registrar", font=("Arial", 14), command=self.save_data).grid(column=1, row=8, padx=5)
        tk.Button(self.frame2, text="Volver", font=("Arial", 14), command=self.go_back).grid(column=0, row=8, padx=5)

    # Función para volver a CentralWindow
    def go_back(self):
        self.withdraw()
        CentralWindow()
        
    # Función para guardar la información
    def save_data(self):
        name = self.name.get().strip().title()
        last_name = self.last_name.get().strip().title()
        age = self.age.get()
        degree = self.degree.get()
        grades = self.grades
        image_rout = self.image_rout
        
        self.aux = False
        self.errors(name, last_name, age, degree, grades)
        if self.aux == False:
            print("a")
            return

        self.new_student = organize_data(name, last_name, age, degree, grades, image_rout)

        carpeta = os.path.join(os.path.abspath("."), "Proyecto Estudiantes")
        os.makedirs(carpeta, exist_ok=True)
        rout_json = os.path.join(carpeta, "Data.json")

        if os.path.exists(rout_json):
            with open(rout_json, "r", encoding="utf-8") as archivo:
                try:
                    students = json.load(archivo)
                except json.JSONDecodeError:
                    students = []
        else:
            students = []

        students.append(self.new_student)

        with open(rout_json, "w", encoding="utf-8") as archivo:
            json.dump(students, archivo, ensure_ascii=False, indent=4)

        messagebox.showinfo("Éxito", "Estudiante registrado correctamente")
        self.reset()
        
    # Función para limpiar la pantalla 
    def reset(self):
        self.name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.age.delete(0, tk.END)
        self.degree.delete(0, tk.END)
        self.option_gender.set("")
        self.option_subject.set("")
        self.subject.delete(0, tk.END)
        self.image_rout = ""
        self.grades = {
            "Ingles": "base",
            "Matematicas": "base",
            "Ciencias Sociales": "base",
            "Ciencias Naturales": "base"
        }

        for widget in self.frame1.grid_slaves(row=6, column=1):
            widget.destroy()
            
    # Función para obtener la imagen ingresada
    def get_image(self):
        rout = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp")],
        )

        if not rout:
            messagebox.showerror("Error", "Falta imagen")
            return

        self.image_rout = rout

        image = Image.open(rout)
        image.thumbnail((150, 150))
        photo = ImageTk.PhotoImage(image)
        logo = tk.Label(self.frame1, image=photo)
        logo.image = photo
        logo.grid(column=1, row=6)
        
    # Función para diccionalizar las notas x materia
    def save_grade(self):
        subject = self.option_subject.get().strip()
        grade = self.subject.get().strip()

        if not subject or not grade:
            messagebox.showerror("Error", "Informacion insuficiente")
            return

        try:
            grade = int(grade)
            self.grades[subject] = grade
        except ValueError:
            messagebox.showerror("Error", "Valor invalido")
            
    # Función que compruebe datos ingresados
    def errors(self, name, last_name, age, degree, grades):
 
        # Error x falta de datos
        if not all([name, last_name, age, degree]):
            messagebox.showerror("Error", "Datos insuficientes")
            return        
        
        # Error x valores incorretos
        try:
            age = int(age)
            degree = int(degree)
        except ValueError:
            messagebox.showerror("Error", "Algun parametro requiere valores numericos")
            return
        
        # Error x exceso de limites (grades)
        for clave, valor in grades.items():
            try:
                nota = int(valor)
                if nota < 0 or nota > 5:
                    messagebox.showerror("Error", f"Ingrese nota entre 0-5 en {clave}")
                    return
            except ValueError:
                messagebox.showerror("Error", f"La nota en {clave} no es válida")
                return

        
        # Error x exceso de limites (degree)
        if degree < 1 or degree > 12:
            messagebox.showerror("Error", "Ingrese un grado valido (1-12)")
            return
        self.aux = True
        return self.aux


class ListerWindow(tk.Toplevel):
    def __init__(self, master, data):
        super().__init__(master)
        self.geometry("300x400")
        self.title("Lista de estudiantes")
        self.data = data
        
        # Frame 1
        self.frame1 = tk.Frame(self)
        self.frame1.pack()
        
        tk.Label(self.frame1, text="Estudiantes", font=("Arial", 16)).pack(pady=5)
        self.names = self.recover_names()
        print(self.names)
        self.name = ttk.Combobox(self.frame1, values=self.names, state="readonly")
        self.name.pack(pady=5)
        
        # Frame 2
        self.frame2 = tk.Frame(self)
        self.frame2.pack()
        
        self.label_name = tk.Label(self.frame2, text="Nombres: ")
        self.label_name.pack()

        self.label_lastname = tk.Label(self.frame2, text="Apellidos: ")
        self.label_lastname.pack()

        self.label_age = tk.Label(self.frame2, text="Edad: ")
        self.label_age.pack()

        self.label_gender = tk.Label(self.frame2, text="Género: ")
        self.label_gender.pack()

        self.label_degree = tk.Label(self.frame2, text="Grado: ")
        self.label_degree.pack()
        
        self.name.bind("<<ComboboxSelected>>", self.get_info)
    
    def get_info(self, event):
        selected_name = self.name.get()
        for estudiante in self.data:
            full_name = f"{estudiante['name']} {estudiante['last name']}"
            if full_name == selected_name:
                self.label_name.config(text=f"Nombres: {estudiante["name"]}")
                self.label_lastname.config(text=f"Apellidos: {estudiante["last name"]}")
                self.label_age.config(text=f"Edad: {estudiante["age"]}")
                self.label_gender.config(text=f"Genero: {estudiante["gender"]}")
                self.label_degree.config(text=f"Grado: {estudiante["degree"]}")
                
        
    def recover_names(self):
        names = []
        for student in self.data:
            complet_name = ""
            for clave, valor in student.items():
                if clave == "name":
                    complet_name = valor
                elif clave  == "last name":
                    complet_name = complet_name + " " + valor
            names.append(complet_name)
        names = sorted(names)
        return names


# Bucle central
if __name__ == "__main__":
    app = CentralWindow()
    app.mainloop()