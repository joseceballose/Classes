# Desarrolla un sistema de gestión para un hospital que permita realizar las siguientes funcionalidades:

# 1.Gestión de Pacientes:Cada paciente tiene un nombre, un ID, una fecha de nacimiento y una lista de enfermedades.Los pacientes pueden ser añadidos, eliminados y listados.

# 2.Gestión de MédicosLos médicos pueden ser añadidos, eliminados y listados.

# 3.Citas Médicas:Los pacientes pueden solicitar citas con médicos.Las citas deben tener una fecha y una hora, y deben estar asociadas a un paciente y un médico.El sistema debe permitir cancelar citas.

# 4.Tratamientos:Los médicos pueden prescribir tratamientos a los pacientes.Cada tratamiento tiene un nombre, una descripción y un estado (pendiente o completado).Los tratamientos deben poder ser añadidos, eliminados y listados.

# 5.Reportes:Generar un reporte de todos los pacientes y sus enfermedades.Generar un reporte de todos los médicos y sus pacientes asignados.Generar un reporte de todas las citas programadas.

# Todos los datos como nombres, fechas y edades deben ser ingresadas por el usuario y validada correctamente. El sistema no puede dejar de funcionar si escribo de manera incorrecta algún dato, además de ello los ID deben ser autogenerados y único se recomienda el uso de la librería UUID.

# En este ejercicio existe una clase que encierra todo el sistema, dicha clase debe ser llamada Hospital la cual gestionará todas las listas necesarias a usar en el sistema.
# Ese ejercicio está un poco extenso y te va a tomar un poco
# https://www.uuidgenerator.net/dev-corner/python



import uuid
from datetime import datetime


class Paciente: 
    def __init__(self, name, date_brirthaday, diseases= None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.date_brirthaday = date_brirthaday
        self.diseases = diseases if diseases else []


class Medico: 
    def __init__(self, name, department):
        self.id = str(uuid.uuid4())
        self.name = name
        self.department = department

class Cita: 
    def __init__(self, pacienteId, medicoId, date_hour):
        self.id = str(uuid.uuid4())
        self.paciente_id = pacienteId
        self.medico_id = medicoId
        self.date_hour = date_hour


class Tratamiento: 
    def __init__(self, pacienteId, medicoId, name, description, status = 'pendiente'):
        self.id = str(uuid.uuid4())
        self.paciente_id = pacienteId
        self.medico_id = medicoId
        self.name = name 
        self.description = description
        self.status = status


class Hospital: 
    def __init__(self):
        self.pacientes = {}
        self.medicos = {}
        self.citas = {}
        self.tratameintos = {}

    def agregar_paciente(self, name, date_brirthaday, diseases= None):
        try: 
            datetime.strptime(date_brirthaday, '%Y-%m-%d')
        except Exception: 
            print("La fecha ingresada no es válida. FoRmato (YYYY-MM-DD)")
            return None
        
        paciente = Paciente(name,date_brirthaday,diseases)
        self.pacientes[paciente.id] = paciente
        print(f'Paciente añadido con exito con el ID: {paciente.id}')
        return paciente.id

    def eliminar_paciente(self,pacienteId):
        if pacienteId in self.pacientes:
            del self.pacientes[pacienteId]
            print("Paciente Eliminado")
        else:
            print("Paciente no encontrado")

    def listar_pacientes(self):
        for p in self.pacientes.values():
            print(f'Id {p.id}, Nombre {p.name}, Fecha Nac {p.date_brirthaday}')

    def agendar_cita(self,pacienteId, medicoId,date_hour):
        if pacienteId not in self.pacientes:
            print("Paciente No encontrado")
            return None
        if medicoId not in self.medicos:
            print("Médico No encontrado")
            return None
        
        try: 
            datetime.strptime(date_hour, '%Y-%m-%d %H:%M')
        except Exception: 
            print("La fecha ingresada no es válida. FoRmato (YYYY-MM-DD HH:MM)")
            return None

        if date_hour < datetime.now():
            print("La fecha no puede ser menor a la actual")
            return None
        
        
        cita = Cita(pacienteId,medicoId,date_hour)
        self.citas[cita.id] = cita
        self.medicos[medicoId].pacientes.add(pacienteId)
        print("Cita agendada correctamente")
    

def main(): 

    hospital = Hospital()
    
    while True: 
        print("\n --- Sitema de Gestión del Hospital")
        print("1. Agregar Paciente")
        print("2. Eliminar Paciente")
        print("3. Listas Pacientes")
        print("4. Agregar Médico")
        print("5. Eliminar Médico")
        print("6. Listar Médicos")
        print("7. Agregar Cita")
        print("8. Cancelar Cita")
        print("9. Listar Citas")
        print("10. Salir")

        option = input("Seleccione una opción:")

        if option == '1': 
            name = input("Nombre del paciente")
            date_brirthaday = input("Fecha de nacimiento (YYYY-MM-DD)")
            diseases = input("Enfermedades (Separadas por coma)").split(',')
            hospital.agregar_paciente(name, date_brirthaday, diseases)

        elif option == '2':
            paciente_id = input("Id del paciente:")
            hospital.eliminar_paciente(paciente_id)

        elif option == '3':
            hospital.listar_pacientes()

        if option == '7': 
            paciente_id = input("Id del paciente:")
            medico_id = input("Id del médico:")
            date_hour = input("Fecha y Hora (YYYY-MM-DD HH:MM):")
            hospital.agendar_cita(paciente_id,medico_id,date_hour)

        elif option == '10':
            print("Saliendo del sistema....")
            break   
        else: 
            print("Opción no válida")

if __name__ == '__main__':
    main()