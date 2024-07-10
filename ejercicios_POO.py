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
        resultados = [pub for pub in self._catalogo if pub.año.lower() == año.lower()]
        self._mostrar_resultados_busqueda(resultados)

    def _mostrar_resultados_busqueda(self, resultados):
        if resultados:
            print("Resultados de la busqueda")
            for pub in resultados:  
                pub.mostar_informacion()

        else:
            print("no se encontraron resultados:")