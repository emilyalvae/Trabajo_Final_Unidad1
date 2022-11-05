


class Libro():

    def __init__(self, id=None,titulo=None,genero=None,ISBN=None ,editorial=None,autor=None):
        
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autor = autor         

    def leer_archivo(self):
        pass

    def listar_libros(self):
        pass

    def agregar_libros(self):
        pass

    def eliminar_libros(self):
        pass

    def buscar_libro_ISBN_título(self):
        pass

    def ordenar_libros(self):
        pass

    def buscar_libro_x_autor_editorial_género(self):
        pass

    def buscar_libro_x_numero_de_autores(self):
        pass

    def editar_libro(self):
        pass

    def guardar_libros(self):
        pass







continuar=True
while continuar:

    print("""Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
        Opción 2: Listar libros.
        Opción 3: Agregar libro.
        Opción 4: Eliminar libro.
        Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
        Opción 6: Ordenar libros por título.
        Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
        Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
        Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
        Opción 10: Guardar libros en archivo de disco duro (.txt o csv)
        Opcion 11: Salir """)

    numero=input("\n Ingrese una opcion (numero): ")

    while numero not in ["1","2","3","4","5","6","7","8","9","10","11"]:
        numero=input("\n ingrese una opcion CORRECTA (numero):  ")
    numero=int(numero)

    if numero==1:
        Autor=Libro()
        Autor.leer_archivo()

    if numero==2:
        Autor=Libro()
        Autor.listar_libros()

    if numero==3:
        Autor=Libro()
        Autor.agregar_libros()

    if numero==4:
        Autor=Libro()
        Autor.eliminar_libros()

    if numero==5:
        Autor=Libro()
        Autor.buscar_libro_ISBN_título()

    if numero==6:
        Autor=Libro()
        Autor.ordenar_libros()

    if numero==7:
        Autor=Libro()
        Autor.buscar_libro_ISBN_título()

    if numero==8:
        Autor=Libro()
        Autor.buscar_libro_x_numero_de_autores

    if numero==9:
        Autor=Libro()
        Autor.editar_libro()

    if numero==10:
        Autor=Libro()
        Autor.guardar_libros()

    if numero==11:
        continuar=False

