from enum import nonmember


class animal():
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza
    
    def saludar(self):
        print(f"hola, soy {self.nombre} de raza {self.raza}")



class gato(animal):
    def __init__(self, nombre, raza, color):
        super().__init__(nombre, raza)
        self.color=color
    
    def saludar(self):
        print(f"gola soy el gat {self.nombre} de raza {self.raza} de color {self.color}")

animal1=animal("pepe","perro")
animal1.saludar()
gato1= gato("pepe", "criolla","amarillo")
gato1.saludar()
