"""
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés.
Tendrá un método para obtener el importe del interés (cantidad*interés/100)
y otro método para mostrar la información, datos del titular plazo, interés y total de interés.
-> Array para multiples usuarios
-> Funcion de add, remove and visualize
-> Funcion para calcular el total que posee el banco
"""

lista_clientes = []
OPCIONES = [1, 2, 3, 4]


class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def add(self):
        lista_clientes.append(
            {
                "Titular": self.titular,
                "Cantidad": self.cantidad,
            }
        )

    def mostrar(self):
        print(lista_clientes)
    
    def remove(nombre):
        for cliente in lista_clientes:
            if cliente["Titular"] == nombre:
                lista_clientes.remove(cliente)
        
    def calcular_total(self):
        for cliente in lista_clientes:
            total += cliente["Cantidad"]


class Plazo_Fijo(Cuenta):
    def __init__(self, titular, cantidad = 0, plazo = 0, interes = 0):
        super().__init__(titular, cantidad)     
        self.plazo = plazo
        self.interes = interes
        
    def add(self):
        for cliente in lista_clientes:
            if cliente["Titular"] == self.titular:
                cliente["Interes"] = self.interes
                cliente["Plazo"] = self.plazo
                
                

    
class Caja_Ahorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    
    def mostrar(self):
        print(lista_clientes)
        
while True:
    print("1. Agregar cliente")
    print("2. Remover cliente")
    print("3. Crear CDT")
    print("4. VIsualizar")
    opcion = int(input("Opcion: "))
    
    if opcion not in OPCIONES:
        print("Opcion no valida")
        continue
    
    if opcion == 1:
        titular = input("Nombre del titular: ")
        cantidad = int(input("Cantidad: "))
        client =  Cuenta(titular, cantidad)
        client.add()
        
    elif opcion == 2:
        nombre = input("Nombre a remover: ")
        Cuenta.remove(nombre)
        
    elif opcion == 3:
        titular = input("Nombre: ")
        plazo = int(input("Meses para el CDT: "))
        interes = float(input("Interes: "))

        print("interes: ", interes)
        print("plazo: ", plazo)

        for cliente in lista_clientes:
            if cliente["Titular"] == titular:
                cantidad = cliente["Cantidad"]
                cdt = Plazo_Fijo("TEST", cantidad, plazo, interes)
                cdt.add()
        
    else:
        print(lista_clientes)

