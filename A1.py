class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        return(f"Hola, me llamo {self.nombre}, tengo {self.edad} y soy {self.profesion}.")

Ana = Persona("Ana", 27, "camarera")
print(Ana.presentarse())