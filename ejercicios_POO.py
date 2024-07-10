#crear la clase publicacion. 

class Publicacion:
    def __init__(self, titulo, autor, año):
        self._titulo = titulo
        self._autor = autor
        self._año = año

    def mostrar_informacion(self):
        print(f"Publicación: {self._titulo}, Autor: {self._autor}, año: {self._año}")

#clase libro que hereda de publicacion.

class Libro(Publicacion):
    def __init__(self, titulo, autor, año, genero):
        super().__init__(titulo, autor, año)
        self._genero = genero 

    def mostrar_informacion(self):
        print(f"Libros: {self._titulo}, Autor: {self._autor}, Año: {self._año}, Genero: {self._genero}")

class Revista(Publicacion):
    def __init__(self, titulo, autor, año, numero_edicion):
        super().__init__(titulo, autor, año)
        self._numero_edicion = numero_edicion

    def mostrar_informacion(self):
        print(f"Revista: {self._titulo}, Autor: {self._autor}, Año: {self._año}, número de Edicion: {self._numero_edicion} ")

class Usuario: 
    def __init__(self, nombre):
        self.nombre = nombre
        self._prestamos = []

    def tomar_prestamo(self, publicacion):
        self._prestamos.append(publicacion)
        print(f"self.nombre ha tomado prestado'{publicacion._titulo}'")

    def devolver_publicacion(self, publicacion):
        if publicacion in self._prestamos:
            self._prestamos.remove(publicacion)
            print(f"{self.nombre} ha devuelto 'publicacion_titulo'")
        else:
                print (f"{self.nombre} no ha tomado prestado los siguientes titulos:")
                for publicacion in self._prestamos:
                    publicacion.mostrar_informacion()