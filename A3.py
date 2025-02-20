class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        return(f"Hola, me llamo {self.nombre}, tengo {self.edad} y soy {self.profesion}.")

class Trabajador(Persona):
    def __init__(self, nombre, edad, profesion, trabajo):
        super().__init__(nombre, edad, profesion)
        self.trabajo = trabajo

    def presentarse(self):
        return(f"Hola, me llamo {self.nombre}, tengo {self.edad}, soy {self.profesion} y trabajo en {self.trabajo}.")

Ana = Persona("Ana", 27, "camarera")
print(Ana.presentarse())
Elena = Trabajador("Elena", 22, "Arquitecta", "Construcciones XYZ")
print(Elena.presentarse())