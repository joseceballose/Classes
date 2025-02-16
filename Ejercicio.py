'''
En un zoologico, se debe almacenar en un array todas las personas que ingresan al lugar
persona: nombre, edad, fecha de acceso
otras:
trabajadores
niños
adultos

tambien se debe registrar los animales del lugar
- color, altura, peso 
funcion que, segun el peso y la dieta, muestre el mantenimiento

cada uno tiene un comportamiento distinto x cada animal
- cuando se cree al animal se debe ejecutar la caracteriostica propia

ademas, cada animal tiene un costo mensual de mantenimiento, tiene q ser privada
ej: print(mono.mantenimiento) -> error en un try catch

'''

DIETAS = ['herbivoro', 'omnivoro', 'carnivoro']

listUser = []
listAnimal = []

def valor_mantenimiento(dieta, peso):
    try:
        if dieta not in DIETAS:
            raise ValueError("Dieta no recocida")
            
        if dieta.lower() == 'carnivoro':
            return peso * 1000
        elif dieta.lower() == 'omnivoro':
            return peso * 750
        else:
            return peso * 500
         
    except ValueError as e:
        print('Dieta no disponible: ', e)

class persona:
    
    def __init__(self, nombre, edad, fecha_ingreso):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso
    

class niño(persona):
    
    def __init__(self, nombre, edad, fecha_ingreso, grado_escolar):
        super().__init__(nombre, edad, fecha_ingreso)
        self.grado_escolar = grado_escolar
    

class adultos(persona):
    
    def __init__(self, nombre, edad, fecha_ingreso, trabajo):
        super().__init__(nombre, edad, fecha_ingreso)
        self.trabajo = trabajo


class trabajador(persona):
    
    def __init__(self, nombre, edad, fecha_ingreso, horas_laborales):
        super().__init__(nombre, edad, fecha_ingreso)
        self.horas_laborales = horas_laborales

class animal:
    def __init__(self, color, altura, peso, dieta):
        self.color = color
        self.altura = altura
        self.peso = peso
        self.dieta = dieta
        self.mantenimiento = valor_mantenimiento(self.dieta, self.peso)
        self.add()
        
    def add(self):
        listAnimal.append({ 
                  "Color": self.color,
                  "altura": self.altura,
                  "peso": self.peso,
                  "mantenimiento": self.mantenimiento
                 })
        
animal1 = animal('blanco', 1.80, 80, 'carnivoro')
print(listAnimal)