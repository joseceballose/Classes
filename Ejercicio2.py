"""
Realizar un programa en el cual se declaren dos valores enteros por teclado. 
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.
"""

class calculadora():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.all()
    
    def sumar(self):
        return print(self.numero1+self.numero2)
    
    def restar(self):
        return print(self.numero1-self.numero2)

    def multiplicar(self):
        return print(self.numero1*self.numero2)

    def dividir(self):
        return print(self.numero1/self.numero2) 
    
    def all(self):
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()  

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
print(calculadora(numero1, numero2))     