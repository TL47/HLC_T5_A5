class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        return(f"Hola, me llamo {self.nombre}, tengo {self.edad} y soy {self.profesion}.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, curso):
        super().__init__(nombre, edad, profesion)
        self.curso = curso
    
    def presentarse(self):
        return(f"Hola, me llamo {self.nombre}, tengo {self.edad} y estudio {self.curso}.")

Ana = Persona("Ana", 27, "camarera")
print(Ana.presentarse())
Carlos = Estudiante("Carlos", 22, "Estudiante", "Matemáticas")
print(Carlos.presentarse())