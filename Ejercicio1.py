"""
En un zoologico se necesitan agregar dos arrays todas las personas y animales que ingresen y vivan dentro.

Personas -> nombre, id, edad, fecha de acceso
-> tipos de personas: trabajador, niñon y adulto

Animales -> nombre, color, altura, peso, id, dieta, mantenimiento y comportamiento unico
"""
#Importes
import uuid

#Constantes
DIETAS = ["herbivoro", "omnivoro", "carnivoro"]
CATEGORIAS = ["Visitante", "Trabajador"]

#Listas base
listUser = []
listAnimal = []
contador = 0

#Creacion de la Funcion que calcule el costo x animal
def valor_mantenimiento(dieta, peso):
    try:
        if dieta not in DIETAS:
            raise ValueError("Dieta no recocida")

        if dieta.lower() == "carnivoro":
            return peso * 1000
        elif dieta.lower() == "omnivoro":
            return peso * 750
        else:
            return peso * 500

    except ValueError as e:
        print("Dieta no disponible: ", e)

#Creacion de la funcion de eleccion segun categoria
def eleccion_categoria():
    try:
        nombre = input("Nombre: ")
        edad = int(input("edad: "))
        fecha_ingreso = input("Fecha_ingreso (DD/MM/AA): ")
        categoria = input("Categoria: ")

        if categoria not in CATEGORIAS:
            raise ValueError

        if categoria == "visitante" and edad < 18:
            grado_escolar = int(input("Grado escolar: "))
            return niño(nombre, edad, fecha_ingreso, grado_escolar)

        elif categoria == "visitante" and edad >= 18:
            trabajo = int(input("Trabajo: "))
            return adulto(nombre, edad, fecha_ingreso, trabajo)

        else:
            horas_labolares = int(input("Horas laborales: "))
            return trabajador(nombre, edad, fecha_ingreso, horas_labolares)
    except ValueError as e:
        print("Eleccion no reconocida")

#creacion superclase persona
class persona:

    def __init__(self, nombre, edad, fecha_ingreso):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso
        self.id = uuid.uuid4()
        self.add()
        
    #Funcion de añadir personas al array
    def add(self):
        listUser.append(
            {
                "Nombre": self.nombre,
                "edad": self.edad,
                "id": self.id,
                "fecha de ingreso": self.fecha_ingreso,
            }
        )
        
    #Funcion de remover personas al array
    def remove(persona_remover):
        for persona in listUser:
            if persona["name"] == persona_remover:
                listUser.remove(persona)

#Creacion sunclase persona
class niño(persona):

    def __init__(self, nombre, edad, fecha_ingreso, grado_escolar):
        super().__init__(nombre, edad, fecha_ingreso)
        self.grado_escolar = grado_escolar
        self.addPlus()

    def addPlus(self):
        listUser[-1]["Grado escolar"] = self.grado_escolar

#Cracion subclase adulto
class adulto(persona):

    def __init__(self, nombre, edad, fecha_ingreso, trabajo):
        super().__init__(nombre, edad, fecha_ingreso)
        self.trabajo = trabajo
        self.addPlus()

    def addPlus(self):
        listUser[-1]["Trabajo"] = self.trabajo

#Creacion subclase trabajador
class trabajador(persona):

    def __init__(self, nombre, edad, fecha_ingreso, horas_laborales):
        super().__init__(nombre, edad, fecha_ingreso)
        self.horas_laborales = horas_laborales
        self.addPlus()

    def addPlus(self):
        listUser[-1]["Horas Laborales"] = self.horas_laborales

#Creacion superclase animal
class animal:
    def __init__(self, nombre, color, altura, peso, dieta, comportamiento):
        self.nombre = nombre
        self.color = color
        self.altura = altura
        self.peso = peso
        self.dieta = dieta
        self.__mantenimiento = valor_mantenimiento(self.dieta, self.peso)
        self.comportamiento = comportamiento
        self.id = uuid.uuid4()
        self.add()
        print(f"El/la {self.nombre} sabe {self.comportamiento}")
        
    #Funcion de adicion al array
    def add(self):
        listAnimal.append(
            {
                "Nombre": self.nombre,
                "Color": self.color,
                "altura": self.altura,
                "peso": self.peso,
                "mantenimiento": self.__mantenimiento,
                "comportamiento": self.comportamiento,
                "id": self.id
            }
        )
    
    #Funcion de eliminacion
    def remove(self, animal_remover):
        for animal in listAnimal:
            if animal["name"] or animal["id"] == animal_remover:
                listAnimal.remove(animal)

#Bucle principal
while True:
    opcion = int(input("Opciones:\n1. Usuario \n2. Animal\n"))

    if opcion != 1 and opcion != 2:
        print("Opcion no disponible")
        continue

    # Funciones usuario
    if opcion == 1:
        contador += 1
        opciones = [1, 2, 3]
        opcion = int(input("Opciones: \n1. Agregar\n2. Remover\n3. Visualizar\n"))

        if opcion not in opciones:
            print("Opcion no disponible")
            continue

        # Agregar
        if opcion == 1:
            usuario = eleccion_categoria()

        # Remover
        elif opcion == 2:
            persona_remover = input("Nombre ersona que sale: ")
            persona.remove(persona_remover)

        # Visualizar
        else:
            print(listUser)
    
    # Funciones animal
    else:
        opciones = [1, 2, 3]
        opcion = int(input("Opciones: \n1. Agregar\n2. Remover\n3. Visualizar\n"))

        if opcion not in opciones:
            print("Opcion no disponible")
            continue
        
        # Agregar
        if opcion == 1:
            nombre = input("Nombre del animal: ")
            altura = float(input("Altura del animal:"))
            color = input("Color del animal: ")
            peso = float(input("Peso: "))
            dieta = input("Dieta (carnivoro, omnivoro, herbivoro): ")
            comportamiento = input("Comportamiento especial: ")
            animal = animal(nombre, color, altura, peso, dieta, comportamiento)
        
        # Remover
        elif opcion == 2:
            animal_remover = input("Animal a remover (nombre o id: )")
            animal.remove(animal_remover)
        
        # Visualizar
        else:
            print(listAnimal)