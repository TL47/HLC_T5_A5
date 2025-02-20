class Libro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca():
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        i = 1
        for libro in self.libros:
            print(f"{i}. {libro.titulo} - {libro.autor}")
            i += 1

biblio = Biblioteca()
biblio.agregar_libro(Libro("1984", "George Orwell"))
biblio.agregar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
biblio.mostrar_libros()