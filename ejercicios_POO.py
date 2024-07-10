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

    def mostrar_prestamos(self):
        print(f"{self.nombre} ha tomado prestado los siguientes titulos:")
        for publicacion in self._prestamos:
            publicacion.mostrar_informacion()


#clase biblioteca para gestionar publicacion y usuarios.
class Biblioteca:
    def __init__(self):
        self._catalogo = []
        self._ususarios = []

    def agregar_publicacion(self, publicacion):
        self._catalogo.append(publicacion)
        print(f"Se ha agredado '{publicacion._titulo}' al catalogo.")
    
    def registrar_usuario(self, usuario):
        self._ususarios.append(usuario)
        print(f"Usuario: '{usuario.nombre}' ha sido registrado")

    def buscar_por_titulo(self, titulo):
        resultados = [pub for pub in self._catalogo if pub.titulo.lower() == titulo.lower()]
        self._mostrar_resultados_busqueda(resultados)

    def buscar_por_autor(self, autor):
        resultados = [pub for pub in self._catalogo if pub.autor.lower() == autor.lower()]
        self._mostrar_resultados_busqueda(resultados)

    def buscar_por_año(self, año):
        resultados = [pub for pub in self._catalogo if pub.año.lower() == año()]
        self._mostrar_resultados_busqueda(resultados)

    def _mostrar_resultados_busqueda(self, resultados):
        if resultados:
            print("Resultados de la busqueda")
            for pub in resultados:  
                pub.mostar_informacion()

        else:
            print("no se encontraron resultados:")

#funcion para mostrar informacion de cualquier publicacion.

def mostrar_publicacion(publicacion):
    publicacion.mostrar_informacion() 

#crear las instancias de libros y revista

libro1 = Libro("El principito", "Antoine de Saint-Exupery", 1943, "ficcion")

revista1 = Revista("National geographic", "varios Autores", 2021, 7)

libro2 = Libro("1984", "george Orwell", 1949, "Dístopia")

revista2 = Revista("Science", "Varios Autores", 2023, 12)

#crear instancia de usuario

usuario1 = Usuario("Juan Pérez")
usuario2 = Usuario("ana gomez")

#crear instancia de biblioteca

biblioteca = Biblioteca()

#gregar publicaciones al catalogo de la biblioteca
biblioteca.agregar_publicacion(libro1)
biblioteca.agregar_publicacion(libro2)
biblioteca.agregar_publicacion(revista1)
biblioteca.agregar_publicacion(revista2)

#registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

#mostrar informacion de publicaciones
mostrar_publicacion(libro1)
mostrar_publicacion(revista1)

#gestionar prestamos
usuario1.tomar_prestamos(libro1)
usuario1.tomar_prestamos(revista2)
usuario1.mostrar_prestamos()
usuario1.devolver_publicacion(libro1)
usuario1.mostrar_prestamos()

#busquedas en el catalogo de la biblioteca
print("\nBusqueda por titulo")
biblioteca.buscar_por_titulo("1984")
print("\nBusqueda por autor")
biblioteca.buscar_por_autor("Antoine de Saint-exupery")
print("\nBusqueda por año:")
biblioteca.buscar_por_año(2021)
